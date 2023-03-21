############################################################################
# Copyright(c) Open Law Library. All rights reserved.                      #
# See ThirdPartyNotices.txt in the project root for additional notices.    #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
import asyncio
import enum
import functools
import json
import logging
import re
import sys
import uuid
from collections import namedtuple
from concurrent.futures import Future
from functools import partial
from itertools import zip_longest
from typing import Callable, List, Optional

from pygls.capabilities import ServerCapabilitiesBuilder
from pygls.constants import ATTR_FEATURE_TYPE
from pygls.exceptions import (JsonRpcException, JsonRpcInternalError, JsonRpcInvalidParams,
                              JsonRpcMethodNotFound, JsonRpcRequestCancelled,
                              MethodTypeNotRegisteredError, FeatureNotificationError,
                              FeatureRequestError)
from pygls.feature_manager import (FeatureManager, assign_help_attrs, get_help_attrs,
                                   is_thread_function)
from pygls.lsp import (JsonRPCNotification, JsonRPCRequestMessage, JsonRPCResponseMessage,
                       get_method_params_type, get_method_return_type, is_instance)
from pygls.lsp.methods import (CANCEL_REQUEST, CLIENT_REGISTER_CAPABILITY,
                               CLIENT_UNREGISTER_CAPABILITY, EXIT, INITIALIZE, INITIALIZED,
                               LOG_TRACE_NOTIFICATION, SET_TRACE_NOTIFICATION, SHUTDOWN,
                               TEXT_DOCUMENT_DID_CHANGE, TEXT_DOCUMENT_DID_CLOSE,
                               TEXT_DOCUMENT_DID_OPEN, TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS,
                               WINDOW_LOG_MESSAGE, WINDOW_SHOW_DOCUMENT, WINDOW_SHOW_MESSAGE,
                               WORKSPACE_APPLY_EDIT, WORKSPACE_CONFIGURATION,
                               WORKSPACE_DID_CHANGE_WORKSPACE_FOLDERS, WORKSPACE_EXECUTE_COMMAND,
                               WORKSPACE_SEMANTIC_TOKENS_REFRESH)
from pygls.lsp.types import (ApplyWorkspaceEditParams, ApplyWorkspaceEditResponse, Diagnostic,
                             DidChangeTextDocumentParams, DidChangeWorkspaceFoldersParams,
                             DidCloseTextDocumentParams, DidOpenTextDocumentParams,
                             ExecuteCommandParams, InitializeParams, InitializeResult,
                             LogMessageParams, MessageType, PublishDiagnosticsParams,
                             RegistrationParams, ServerInfo, ShowMessageParams,
                             UnregistrationParams, WorkspaceEdit)
from pygls.lsp.types.basic_structures import (ConfigCallbackType, LogTraceParams, SetTraceParams,
                                              Trace)
from pygls.lsp.types.window import ShowDocumentCallbackType, ShowDocumentParams
from pygls.lsp.types.workspace import ConfigurationParams
from pygls.uris import from_fs_path
from pygls.workspace import Workspace

logger = logging.getLogger(__name__)


def call_user_feature(base_func, method_name):
    """Wraps generic LSP features and calls user registered feature
    immediately after it.
    """
    @functools.wraps(base_func)
    def decorator(self, *args, **kwargs):
        ret_val = base_func(self, *args, **kwargs)

        try:
            user_func = self.fm.features[method_name]
            self._execute_notification(user_func, *args, **kwargs)
        except KeyError:
            pass
        except Exception:
            logger.exception('Failed to handle user defined notification "%s": %s',
                             method_name, args)

        return ret_val

    return decorator


def dict_to_object(**d):
    """Create nested objects (namedtuple) from dict."""
    type_name = d.pop('type_name', 'Object')
    return json.loads(
        json.dumps(d),
        object_hook=lambda p: namedtuple(type_name, p.keys(), rename=True)(*p.values())
    )


def default_serializer(o):
    """JSON serializer for complex objects that do not extend pydantic BaseModel class."""
    if isinstance(o, enum.Enum):
        return o.value
    return o.__dict__


def deserialize_command(params):
    """Function used to deserialize command arguments to a specific class
    or a namedtuple."""
    # TODO: Register/Look up custom command arguments' types
    # Currently command parameters are type of 'any', but eventually we would
    # want to register an argument type of our custom command and to
    # deserialize it properly.
    temp_obj = dict_to_object(**params, type_name='CommandParams')

    params['arguments'] = getattr(temp_obj, 'arguments', None)
    return params


def deserialize_params(data, get_params_type):
    """Function used to deserialize params to a specific class."""
    try:
        method = data['method']
        params = data['params']

        if not isinstance(params, dict):
            return data

        try:
            params_type = get_params_type(method)
            if params_type is None:
                params_type = dict_to_object
            elif params_type.__name__ == ExecuteCommandParams.__name__:
                params = deserialize_command(params)

        except MethodTypeNotRegisteredError:
            params_type = dict_to_object

        try:
            data['params'] = params_type(**params)
        except TypeError:
            raise ValueError(
                f'Could not instantiate "{params_type.__name__}" from params: {params}')
    except KeyError:
        pass

    return data


def deserialize_message(data, get_params_type=get_method_params_type):
    """Function used to deserialize data received from client."""
    if 'jsonrpc' in data:
        try:
            deserialize_params(data, get_params_type)
        except ValueError:
            raise JsonRpcInvalidParams()

        if 'id' in data:
            if 'method' in data:
                return JsonRPCRequestMessage(**data)
            else:
                return JsonRPCResponseMessage(**data)
        else:
            return JsonRPCNotification(**data)

    return data


class JsonRPCProtocol(asyncio.Protocol):
    """Json RPC protocol implementation using on top of `asyncio.Protocol`.

    Specification of the protocol can be found here:
        https://www.jsonrpc.org/specification

    This class provides bidirectional communication which is needed for LSP.
    """
    CHARSET = 'utf-8'
    CONTENT_TYPE = 'application/vscode-jsonrpc'

    MESSAGE_PATTERN = re.compile(
        rb'^(?:[^\r\n]+\r\n)*'
        + rb'Content-Length: (?P<length>\d+)\r\n'
        + rb'(?:[^\r\n]+\r\n)*\r\n'
        + rb'(?P<body>{.*)',
        re.DOTALL,
    )

    VERSION = '2.0'

    def __init__(self, server):
        self._server = server
        self._shutdown = False

        self._client_request_futures = {}
        self._server_request_futures = {}

        self.fm = FeatureManager(server)
        self.transport = None
        self._message_buf = []

        self._send_only_body = False

    def __call__(self):
        return self

    def _check_ret_type_and_send_response(self, method_name, method_type, msg_id, result):
        """Check if registered feature returns appropriate result type."""
        if method_type == ATTR_FEATURE_TYPE:
            return_type = get_method_return_type(method_name)
            if not is_instance(result, return_type):
                error = JsonRpcInternalError().to_dict()
                self._send_response(msg_id, error=error)

        self._send_response(msg_id, result=result)

    def _execute_notification(self, handler, *params):
        """Executes notification message handler."""
        if asyncio.iscoroutinefunction(handler):
            future = asyncio.ensure_future(handler(*params))
            future.add_done_callback(self._execute_notification_callback)
        else:
            if is_thread_function(handler):
                self._server.thread_pool.apply_async(handler, (*params, ))
            else:
                handler(*params)

    def _execute_notification_callback(self, future):
        """Success callback used for coroutine notification message."""
        if future.exception():

            try:
                raise future.exception()
            except Exception:
                error = JsonRpcInternalError.of(sys.exc_info()).to_dict()
                logger.exception('Exception occurred in notification: "%s"', error)

            # Revisit. Client does not support response with msg_id = None
            # https://stackoverflow.com/questions/31091376/json-rpc-2-0-allow-notifications-to-have-an-error-response
            # self._send_response(None, error=error)

    def _execute_request(self, msg_id, handler, params):
        """Executes request message handler."""
        method_name, method_type = get_help_attrs(handler)

        if asyncio.iscoroutinefunction(handler):
            future = asyncio.ensure_future(handler(params))
            self._client_request_futures[msg_id] = future
            future.add_done_callback(partial(self._execute_request_callback,
                                             method_name, method_type, msg_id))
        else:
            # Can't be canceled
            if is_thread_function(handler):
                self._server.thread_pool.apply_async(
                    handler, (params, ),
                    callback=partial(
                        self._check_ret_type_and_send_response,
                        method_name, method_type, msg_id,
                    ),
                    error_callback=partial(self._execute_request_err_callback, msg_id))
            else:
                self._check_ret_type_and_send_response(
                    method_name, method_type, msg_id, handler(params))

    def _execute_request_callback(self, method_name, method_type, msg_id, future):
        """Success callback used for coroutine request message."""
        try:
            if not future.cancelled():
                self._check_ret_type_and_send_response(
                    method_name, method_type, msg_id, result=future.result())
            else:
                self._send_response(
                    msg_id,
                    error=JsonRpcRequestCancelled(f'Request with id "{msg_id}" is canceled')
                )
            self._client_request_futures.pop(msg_id, None)
        except Exception:
            error = JsonRpcInternalError.of(sys.exc_info()).to_dict()
            logger.exception('Exception occurred for message "%s": %s', msg_id, error)
            self._send_response(msg_id, error=error)

    def _execute_request_err_callback(self, msg_id, exc):
        """Error callback used for coroutine request message."""
        exc_info = (type(exc), exc, None)
        error = JsonRpcInternalError.of(exc_info).to_dict()
        logger.exception('Exception occurred for message "%s": %s', msg_id, error)
        self._send_response(msg_id, error=error)

    def _get_handler(self, feature_name):
        """Returns builtin or used defined feature by name if exists."""
        try:
            return self.fm.builtin_features[feature_name]
        except KeyError:
            try:
                return self.fm.features[feature_name]
            except KeyError:
                raise JsonRpcMethodNotFound.of(feature_name)

    def _handle_cancel_notification(self, msg_id):
        """Handles a cancel notification from the client."""
        future = self._client_request_futures.pop(msg_id, None)

        if not future:
            logger.warning('Cancel notification for unknown message id "%s"', msg_id)
            return

        # Will only work if the request hasn't started executing
        if future.cancel():
            logger.info('Cancelled request with id "%s"', msg_id)

    def _handle_notification(self, method_name, params):
        """Handles a notification from the client."""
        if method_name == CANCEL_REQUEST:
            self._handle_cancel_notification(params.id)
            return

        try:
            handler = self._get_handler(method_name)
            self._execute_notification(handler, params)
        except (KeyError, JsonRpcMethodNotFound):
            logger.warning('Ignoring notification for unknown method "%s"', method_name)
        except Exception as error:
            logger.exception(
                'Failed to handle notification "%s": %s',
                method_name,
                params,
                exc_info=True
            )
            self._server._report_server_error(error, FeatureNotificationError)

    def _handle_request(self, msg_id, method_name, params):
        """Handles a request from the client."""
        try:
            handler = self._get_handler(method_name)

            # workspace/executeCommand is a special case
            if method_name == WORKSPACE_EXECUTE_COMMAND:
                handler(params, msg_id)
            else:
                self._execute_request(msg_id, handler, params)

        except JsonRpcException as error:
            logger.exception(
                'Failed to handle request %s %s %s',
                msg_id,
                method_name,
                params,
                exc_info=True
            )
            self._send_response(msg_id, None, error.to_dict())
            self._server._report_server_error(error, FeatureRequestError)
        except Exception as error:
            logger.exception(
                'Failed to handle request %s %s %s',
                msg_id,
                method_name,
                params,
                exc_info=True
            )
            err = JsonRpcInternalError.of(sys.exc_info()).to_dict()
            self._send_response(msg_id, None, err)
            self._server._report_server_error(error, FeatureRequestError)

    def _handle_response(self, msg_id, result=None, error=None):
        """Handles a response from the client."""
        future = self._server_request_futures.pop(msg_id, None)

        if not future:
            logger.warning('Received response to unknown message id "%s"', msg_id)
            return

        if error is not None:
            logger.debug('Received error response to message "%s": %s', msg_id, error)
            future.set_exception(JsonRpcException.from_dict(error))
        else:
            logger.debug('Received result for message "%s": %s', msg_id, result)
            future.set_result(result)

    def _procedure_handler(self, message):
        """Delegates message to handlers depending on message type."""

        if message.jsonrpc != JsonRPCProtocol.VERSION:
            logger.warning('Unknown message "%s"', message)
            return

        if self._shutdown and getattr(message, 'method', '') != EXIT:
            logger.warning('Server shutting down. No more requests!')
            return

        if isinstance(message, JsonRPCNotification):
            logger.debug('Notification message received.')
            self._handle_notification(message.method, message.params)
        elif isinstance(message, JsonRPCResponseMessage):
            logger.debug('Response message received.')
            self._handle_response(message.id, message.result, message.error)
        elif isinstance(message, JsonRPCRequestMessage):
            logger.debug('Request message received.')
            self._handle_request(message.id, message.method, message.params)

    def _send_data(self, data):
        """Sends data to the client."""
        if not data:
            return
        try:
            body = data.json(by_alias=True, exclude_unset=True, encoder=default_serializer)
            logger.info('Sending data: %s', body)

            body = body.encode(self.CHARSET)
            if not self._send_only_body:
                header = (
                    f'Content-Length: {len(body)}\r\n'
                    f'Content-Type: {self.CONTENT_TYPE}; charset={self.CHARSET}\r\n\r\n'
                ).encode(self.CHARSET)

                self.transport.write(header + body)
            else:
                self.transport.write(body.decode('utf-8'))
        except Exception as error:
            logger.exception("Error sending data", exc_info=True)
            self._server._report_server_error(error, JsonRpcInternalError)

    def _send_response(self, msg_id, result=None, error=None):
        """Sends a JSON RPC response to the client.

        Args:
            msg_id(str): Id from request
            result(any): Result returned by handler
            error(any): Error returned by handler
        """
        response = JsonRPCResponseMessage(id=msg_id,
                                          jsonrpc=JsonRPCProtocol.VERSION,
                                          result=result,
                                          error=error)

        if error is None:
            del response.error
        else:
            del response.result

        self._send_data(response)

    def connection_lost(self, exc):
        """Method from base class, called when connection is lost, in which case we
        want to shutdown the server's process as well.
        """
        logger.error('Connection to the client is lost! Shutting down the server.')
        sys.exit(1)

    def connection_made(self, transport: asyncio.BaseTransport):
        """Method from base class, called when connection is established"""
        self.transport = transport

    def data_received(self, data: bytes):
        try:
            self._data_received(data)
        except Exception as error:
            logger.exception("Error receiving data", exc_info=True)
            self._server._report_server_error(error, JsonRpcInternalError)

    def _data_received(self, data: bytes):
        """Method from base class, called when server receives the data"""
        logger.debug('Received %r', data)

        while len(data):
            # Append the incoming chunk to the message buffer
            self._message_buf.append(data)

            # Look for the body of the message
            message = b''.join(self._message_buf)
            found = JsonRPCProtocol.MESSAGE_PATTERN.fullmatch(message)

            body = found.group('body') if found else b''
            length = int(found.group('length')) if found else 1

            if len(body) < length:
                # Message is incomplete; bail until more data arrives
                return

            # Message is complete;
            # extract the body and any remaining data,
            # and reset the buffer for the next message
            body, data = body[:length], body[length:]
            self._message_buf = []

            # Parse the body
            self._procedure_handler(
                json.loads(body.decode(self.CHARSET),
                           object_hook=deserialize_message))

    def notify(self, method: str, params=None):
        """Sends a JSON RPC notification to the client."""
        logger.debug('Sending notification: "%s" %s', method, params)

        request = JsonRPCNotification(
            jsonrpc=JsonRPCProtocol.VERSION,
            method=method,
            params=params
        )

        self._send_data(request)

    def send_request(self, method, params=None, callback=None):
        """Sends a JSON RPC request to the client.

        Args:
            method(str): The method name of the message to send
            params(any): The payload of the message

        Returns:
            Future that will be resolved once a response has been received
        """
        msg_id = str(uuid.uuid4())
        logger.debug('Sending request with id "%s": %s %s', msg_id, method, params)

        request = JsonRPCRequestMessage(
            id=msg_id,
            jsonrpc=JsonRPCProtocol.VERSION,
            method=method,
            params=params
        )

        future = Future()
        # If callback function is given, call it when result is received
        if callback:
            def wrapper(future: Future):
                result = future.result()
                logger.info('Client response for %s received: %s', params, result)
                callback(result)
            future.add_done_callback(wrapper)

        self._server_request_futures[msg_id] = future
        self._send_data(request)

        return future

    def send_request_async(self, method, params=None):
        """Calls `send_request` and wraps `concurrent.futures.Future` with
        `asyncio.Future` so it can be used with `await` keyword.

        Args:
            method(str): The method name of the message to send
            params(any): The payload of the message

        Returns:
            `asyncio.Future` that can be awaited
        """
        return asyncio.wrap_future(self.send_request(method, params))

    def thread(self):
        """Decorator that mark function to execute it in a thread."""
        return self.fm.thread()


def lsp_method(method_name: str):
    def decorator(f):
        f.method_name = method_name
        return f
    return decorator


class LSPMeta(type):
    """Wraps LSP built-in features (`lsp_` naming convention).

    Built-in features cannot be overridden but user defined features with
    the same LSP name will be called after them.
    """
    def __new__(mcs, cls_name, cls_bases, cls):
        for attr_name, attr_val in cls.items():
            if callable(attr_val) and hasattr(attr_val, 'method_name'):
                method_name = attr_val.method_name
                wrapped = call_user_feature(attr_val, method_name)
                assign_help_attrs(wrapped, method_name, ATTR_FEATURE_TYPE)
                cls[attr_name] = wrapped

                logger.debug('Added decorator for lsp method: "%s"', attr_name)

        return super().__new__(mcs, cls_name, cls_bases, cls)


class LanguageServerProtocol(JsonRPCProtocol, metaclass=LSPMeta):
    """A class that represents language server protocol.

    It contains implementations for generic LSP features.

    Attributes:
        workspace(Workspace): In memory workspace
    """

    def __init__(self, server):
        super().__init__(server)

        self.workspace = None
        self.trace = None

        from pygls.progress import Progress
        self.progress = Progress(self)

        if server.name is None or server.version is None:
            self.server_info = None
            logger.warning("Name or version is not set. "
                           "This will be mandatory: "
                           "https://github.com/openlawlibrary/pygls/pull/276")
        else:
            self.server_info = ServerInfo(
                name=server.name,
                version=server.version,
            )

        self._register_builtin_features()

    def _register_builtin_features(self):
        """Registers generic LSP features from this class."""
        for name in dir(self):
            attr = getattr(self, name)
            if callable(attr) and hasattr(attr, 'method_name'):
                self.fm.add_builtin_feature(attr.method_name, attr)

    def apply_edit(self, edit: WorkspaceEdit, label: str = None) -> ApplyWorkspaceEditResponse:
        """Sends apply edit request to the client."""
        return self.send_request(WORKSPACE_APPLY_EDIT,
                                 ApplyWorkspaceEditParams(edit=edit, label=label))

    @lsp_method(EXIT)
    def lsp_exit(self, *args) -> None:
        """Stops the server process."""
        self.transport.close()
        sys.exit(0 if self._shutdown else 1)

    @lsp_method(INITIALIZE)
    def lsp_initialize(self, params: InitializeParams) -> InitializeResult:
        """Method that initializes language server.
        It will compute and return server capabilities based on
        registered features.
        """
        logger.info('Language server initialized %s', params)

        self._server.process_id = params.process_id

        # Initialize server capabilities
        self.client_capabilities = params.capabilities
        self.server_capabilities = ServerCapabilitiesBuilder(
            self.client_capabilities,
            {**self.fm.features, **self.fm.builtin_features}.keys(),
            self.fm.feature_options,
            list(self.fm.commands.keys()),
            self._server.sync_kind,
        ).build()
        logger.debug('Server capabilities: %s', self.server_capabilities.dict())

        root_path = params.root_path
        root_uri = params.root_uri or from_fs_path(root_path)

        # Initialize the workspace
        workspace_folders = params.workspace_folders or []
        self.workspace = Workspace(root_uri, self._server.sync_kind, workspace_folders)

        self.trace = Trace.Off

        return InitializeResult(
            capabilities=self.server_capabilities,
            server_info=self.server_info,
        )

    @lsp_method(INITIALIZED)
    def lsp_initialized(self, *args) -> None:
        """Notification received when client and server are connected."""
        pass

    @lsp_method(SHUTDOWN)
    def lsp_shutdown(self, *args) -> None:
        """Request from client which asks server to shutdown."""
        for future in self._client_request_futures.values():
            future.cancel()

        for future in self._server_request_futures.values():
            future.cancel()

        self._shutdown = True
        return None

    @lsp_method(TEXT_DOCUMENT_DID_CHANGE)
    def lsp_text_document__did_change(self, params: DidChangeTextDocumentParams) -> None:
        """Updates document's content.
        (Incremental(from server capabilities); not configurable for now)
        """
        for change in params.content_changes:
            self.workspace.update_document(params.text_document, change)

    @lsp_method(TEXT_DOCUMENT_DID_CLOSE)
    def lsp_text_document__did_close(self, params: DidCloseTextDocumentParams) -> None:
        """Removes document from workspace."""
        self.workspace.remove_document(params.text_document.uri)

    @lsp_method(TEXT_DOCUMENT_DID_OPEN)
    def lsp_text_document__did_open(self, params: DidOpenTextDocumentParams) -> None:
        """Puts document to the workspace."""
        self.workspace.put_document(params.text_document)

    @lsp_method(SET_TRACE_NOTIFICATION)
    def lsp_set_trace(self, params: SetTraceParams) -> None:
        """Changes server trace value."""
        self.trace = params.value

    @lsp_method(WORKSPACE_DID_CHANGE_WORKSPACE_FOLDERS)
    def lsp_workspace__did_change_workspace_folders(
            self, params: DidChangeWorkspaceFoldersParams) -> None:
        """Adds/Removes folders from the workspace."""
        logger.info('Workspace folders changed: %s', params)

        added_folders = params.event.added or []
        removed_folders = params.event.removed or []

        for f_add, f_remove in zip_longest(added_folders, removed_folders):
            if f_add:
                self.workspace.add_folder(f_add)
            if f_remove:
                self.workspace.remove_folder(f_remove.uri)

    @lsp_method(WORKSPACE_EXECUTE_COMMAND)
    def lsp_workspace__execute_command(self, params: ExecuteCommandParams, msg_id: str) -> None:
        """Executes commands with passed arguments and returns a value."""
        cmd_handler = self.fm.commands[params.command]
        self._execute_request(msg_id, cmd_handler, params.arguments)

    def get_configuration(self, params: ConfigurationParams,
                          callback: Optional[ConfigCallbackType] = None) -> Future:
        """Sends configuration request to the client.

        Args:
            params(ConfigurationParams): ConfigurationParams from lsp specs
            callback(callable): Callabe which will be called after
                                response from the client is received
        Returns:
            concurrent.futures.Future object that will be resolved once a
            response has been received
        """
        return self.send_request(WORKSPACE_CONFIGURATION, params, callback)

    def get_configuration_async(self, params: ConfigurationParams) -> asyncio.Future:
        """Calls `get_configuration` method but designed to use with coroutines

        Args:
            params(ConfigurationParams): ConfigurationParams from lsp specs
        Returns:
            asyncio.Future that can be awaited
        """
        return asyncio.wrap_future(self.get_configuration(params))

    def log_trace(self, message: str, verbose: Optional[str] = None) -> None:
        """Sends trace notification to the client."""
        if self.trace == Trace.Off:
            return

        params = LogTraceParams(message=message)
        if verbose and self.trace == Trace.Verbose:
            params.verbose = verbose

        self.notify(LOG_TRACE_NOTIFICATION, params)

    def publish_diagnostics(self, doc_uri: str, diagnostics: List[Diagnostic]) -> None:
        """Sends diagnostic notification to the client."""
        self.notify(TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS,
                    PublishDiagnosticsParams(uri=doc_uri, diagnostics=diagnostics))

    def register_capability(self, params: RegistrationParams,
                            callback: Optional[Callable[[], None]] = None) -> Future:
        """Register a new capability on the client.

        Args:
            params(RegistrationParams): RegistrationParams from lsp specs
            callback(callable): Callabe which will be called after
                                response from the client is received
        Returns:
            concurrent.futures.Future object that will be resolved once a
            response has been received
        """
        return self.send_request(CLIENT_REGISTER_CAPABILITY, params, callback)

    def register_capability_async(self, params: RegistrationParams) -> asyncio.Future:
        """Register a new capability on the client.

        Args:
            params(RegistrationParams): RegistrationParams from lsp specs

        Returns:
            asyncio.Future object that will be resolved once a
            response has been received
        """
        return asyncio.wrap_future(self.register_capability(params, None))

    def semantic_tokens_refresh(self, callback: Optional[Callable[[], None]] = None) -> Future:
        """Requesting a refresh of all semantic tokens.

        Args:
            callback(callable): Callabe which will be called after
                                response from the client is received

        Returns:
            concurrent.futures.Future object that will be resolved once a
            response has been received
        """
        return self.send_request(WORKSPACE_SEMANTIC_TOKENS_REFRESH, callback=callback)

    def semantic_tokens_refresh_async(self) -> asyncio.Future:
        """Requesting a refresh of all semantic tokens.

        Returns:
            asyncio.Future object that will be resolved once a
            response has been received
        """
        return asyncio.wrap_future(self.semantic_tokens_refresh(None))

    def show_document(self, params: ShowDocumentParams,
                      callback: Optional[ShowDocumentCallbackType] = None) -> Future:
        """Display a particular document in the user interface.

        Args:
            params(ShowDocumentParams): ShowDocumentParams from lsp specs
            callback(callable): Callabe which will be called after
                                response from the client is received

        Returns:
            concurrent.futures.Future object that will be resolved once a
            response has been received
        """
        return self.send_request(WINDOW_SHOW_DOCUMENT, params, callback)

    def show_document_async(self, params: ShowDocumentParams) -> asyncio.Future:
        """Display a particular document in the user interface.

        Args:
            params(ShowDocumentParams): ShowDocumentParams from lsp specs

        Returns:
            asyncio.Future object that will be resolved once a
            response has been received
        """
        return asyncio.wrap_future(self.show_document(params, None))

    def show_message(self, message, msg_type=MessageType.Info):
        """Sends message to the client to display message."""
        self.notify(WINDOW_SHOW_MESSAGE, ShowMessageParams(type=msg_type, message=message))

    def show_message_log(self, message, msg_type=MessageType.Log):
        """Sends message to the client's output channel."""
        self.notify(WINDOW_LOG_MESSAGE, LogMessageParams(type=msg_type, message=message))

    def unregister_capability(self, params: UnregistrationParams,
                              callback: Optional[Callable[[], None]] = None) -> Future:
        """Unregister a new capability on the client.

        Args:
            params(UnregistrationParams): UnregistrationParams from lsp specs
            callback(callable): Callabe which will be called after
                                response from the client is received
        Returns:
            concurrent.futures.Future object that will be resolved once a
            response has been received
        """
        return self.send_request(CLIENT_UNREGISTER_CAPABILITY, params, callback)

    def unregister_capability_async(self, params: UnregistrationParams) -> asyncio.Future:
        """Unregister a new capability on the client.

        Args:
            params(UnregistrationParams): UnregistrationParams from lsp specs
            callback(callable): Callabe which will be called after
                                response from the client is received
        Returns:
            asyncio.Future object that will be resolved once a
            response has been received
        """
        return asyncio.wrap_future(self.unregister_capability(params, None))
