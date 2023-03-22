# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

"""An implementation of the session and presentation layers as used in the Debug
Adapter Protocol (DAP): channels and their lifetime, JSON messages, requests,
responses, and events.

https://microsoft.github.io/debug-adapter-protocol/overview#base-protocol
"""

import collections
import contextlib
import functools
import itertools
import os
import socket
import sys
import threading

from debugpy.common import compat, fmt, json, log
from debugpy.common.compat import unicode


class JsonIOError(IOError):
    """Indicates that a read or write operation on JsonIOStream has failed.
    """

    def __init__(self, *args, **kwargs):
        stream = kwargs.pop("stream")
        cause = kwargs.pop("cause", None)
        if not len(args) and cause is not None:
            args = [str(cause)]
        super(JsonIOError, self).__init__(*args, **kwargs)

        self.stream = stream
        """The stream that couldn't be read or written.

        Set by JsonIOStream.read_json() and JsonIOStream.write_json().

        JsonMessageChannel relies on this value to decide whether a NoMoreMessages
        instance that bubbles up to the message loop is related to that loop.
        """

        self.cause = cause
        """The underlying exception, if any."""


class NoMoreMessages(JsonIOError, EOFError):
    """Indicates that there are no more messages that can be read from or written
    to a stream.
    """

    def __init__(self, *args, **kwargs):
        args = args if len(args) else ["No more messages"]
        super(NoMoreMessages, self).__init__(*args, **kwargs)


class JsonIOStream(object):
    """Implements a JSON value stream over two byte streams (input and output).

    Each value is encoded as a DAP packet, with metadata headers and a JSON payload.
    """

    MAX_BODY_SIZE = 0xFFFFFF

    json_decoder_factory = json.JsonDecoder
    """Used by read_json() when decoder is None."""

    json_encoder_factory = json.JsonEncoder
    """Used by write_json() when encoder is None."""

    @classmethod
    def from_stdio(cls, name="stdio"):
        """Creates a new instance that receives messages from sys.stdin, and sends
        them to sys.stdout.

        On Win32, this also sets stdin and stdout to binary mode, since the protocol
        requires that to work properly.
        """
        if sys.version_info >= (3,):
            stdin = sys.stdin.buffer
            stdout = sys.stdout.buffer
        else:
            stdin = sys.stdin
            stdout = sys.stdout
            if sys.platform == "win32":
                import os, msvcrt

                msvcrt.setmode(stdin.fileno(), os.O_BINARY)
                msvcrt.setmode(stdout.fileno(), os.O_BINARY)
        return cls(stdin, stdout, name)

    @classmethod
    def from_process(cls, process, name="stdio"):
        """Creates a new instance that receives messages from process.stdin, and sends
        them to process.stdout.
        """
        return cls(process.stdout, process.stdin, name)

    @classmethod
    def from_socket(cls, sock, name=None):
        """Creates a new instance that sends and receives messages over a socket.
        """
        sock.settimeout(None)  # make socket blocking
        if name is None:
            name = repr(sock)

        # TODO: investigate switching to buffered sockets; readline() on unbuffered
        # sockets is very slow! Although the implementation of readline() itself is
        # native code, it calls read(1) in a loop - and that then ultimately calls
        # SocketIO.readinto(), which is implemented in Python.
        socket_io = sock.makefile("rwb", 0)

        # SocketIO.close() doesn't close the underlying socket.
        def cleanup():
            try:
                sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            sock.close()

        return cls(socket_io, socket_io, name, cleanup)

    def __init__(self, reader, writer, name=None, cleanup=lambda: None):
        """Creates a new JsonIOStream.

        reader must be a BytesIO-like object, from which incoming messages will be
        read by read_json().

        writer must be a BytesIO-like object, into which outgoing messages will be
        written by write_json().

        cleanup must be a callable; it will be invoked without arguments when the
        stream is closed.

        reader.readline() must treat "\n" as the line terminator, and must leave "\r"
        as is - it must not replace "\r\n" with "\n" automatically, as TextIO does.
        """

        if name is None:
            name = fmt("reader={0!r}, writer={1!r}", reader, writer)

        self.name = name
        self._reader = reader
        self._writer = writer
        self._cleanup = cleanup
        self._closed = False

    def close(self):
        """Closes the stream, the reader, and the writer.
        """

        if self._closed:
            return
        self._closed = True

        log.debug("Closing {0} message stream", self.name)
        try:
            try:
                # Close the writer first, so that the other end of the connection has
                # its message loop waiting on read() unblocked. If there is an exception
                # while closing the writer, we still want to try to close the reader -
                # only one exception can bubble up, so if both fail, it'll be the one
                # from reader.
                try:
                    self._writer.close()
                finally:
                    if self._reader is not self._writer:
                        self._reader.close()
            finally:
                self._cleanup()
        except Exception:
            # On Python 2, close() will raise an exception if there is a concurrent
            # read() or write(), which is a common and expected occurrence with
            # JsonMessageChannel, so don't even bother logging it.
            if sys.version_info >= (3,):
                log.reraise_exception(
                    "Error while closing {0} message stream", self.name
                )

    def _log_message(self, dir, data, logger=log.debug):
        format_string = "{0} {1} " + (
            "{2!j:indent=None}" if isinstance(data, list) else "{2!j}"
        )
        return logger(format_string, self.name, dir, data)

    def _read_line(self, reader):
        line = b""
        while True:
            try:
                line += reader.readline()
            except Exception as exc:
                raise NoMoreMessages(str(exc), stream=self)
            if not line:
                raise NoMoreMessages(stream=self)
            if line.endswith(b"\r\n"):
                line = line[0:-2]
                return line

    def read_json(self, decoder=None):
        """Read a single JSON value from reader.

        Returns JSON value as parsed by decoder.decode(), or raises NoMoreMessages
        if there are no more values to be read.
        """

        decoder = decoder if decoder is not None else self.json_decoder_factory()
        reader = self._reader
        read_line = functools.partial(self._read_line, reader)

        # If any error occurs while reading and parsing the message, log the original
        # raw message data as is, so that it's possible to diagnose missing or invalid
        # headers, encoding issues, JSON syntax errors etc.
        def log_message_and_reraise_exception(format_string="", *args, **kwargs):
            if format_string:
                format_string += "\n\n"
            format_string += "{name} -->\n{raw_lines}"

            raw_lines = b"".join(raw_chunks).split(b"\n")
            raw_lines = "\n".join(repr(line) for line in raw_lines)

            log.reraise_exception(
                format_string, *args, name=self.name, raw_lines=raw_lines, **kwargs
            )

        raw_chunks = []
        headers = {}

        while True:
            try:
                line = read_line()
            except Exception:
                # Only log it if we have already read some headers, and are looking
                # for a blank line terminating them. If this is the very first read,
                # there's no message data to log in any case, and the caller might
                # be anticipating the error - e.g. NoMoreMessages on disconnect.
                if headers:
                    log_message_and_reraise_exception(
                        "Error while reading message headers:"
                    )
                else:
                    raise

            raw_chunks += [line, b"\n"]
            if line == b"":
                break

            key, _, value = line.partition(b":")
            headers[key] = value

        try:
            length = int(headers[b"Content-Length"])
            if not (0 <= length <= self.MAX_BODY_SIZE):
                raise ValueError
        except (KeyError, ValueError):
            try:
                raise IOError("Content-Length is missing or invalid:")
            except Exception:
                log_message_and_reraise_exception()

        body_start = len(raw_chunks)
        body_remaining = length
        while body_remaining > 0:
            try:
                chunk = reader.read(body_remaining)
                if not chunk:
                    raise EOFError
            except Exception as exc:
                # Not logged due to https://github.com/microsoft/ptvsd/issues/1699
                raise NoMoreMessages(str(exc), stream=self)

            raw_chunks.append(chunk)
            body_remaining -= len(chunk)
        assert body_remaining == 0

        body = b"".join(raw_chunks[body_start:])
        try:
            body = body.decode("utf-8")
        except Exception:
            log_message_and_reraise_exception()

        try:
            body = decoder.decode(body)
        except Exception:
            log_message_and_reraise_exception()

        # If parsed successfully, log as JSON for readability.
        self._log_message("-->", body)
        return body

    def write_json(self, value, encoder=None):
        """Write a single JSON value into writer.

        Value is written as encoded by encoder.encode().
        """

        if self._closed:
            # Don't log this - it's a common pattern to write to a stream while
            # anticipating EOFError from it in case it got closed concurrently.
            raise NoMoreMessages(stream=self)

        encoder = encoder if encoder is not None else self.json_encoder_factory()
        writer = self._writer

        # Format the value as a message, and try to log any failures using as much
        # information as we already have at the point of the failure. For example,
        # if it fails after it is serialized to JSON, log that JSON.

        try:
            body = encoder.encode(value)
        except Exception:
            self._log_message("<--", value, logger=log.reraise_exception)
        if not isinstance(body, bytes):
            body = body.encode("utf-8")

        header = fmt("Content-Length: {0}\r\n\r\n", len(body))
        header = header.encode("ascii")

        data = header + body
        data_written = 0
        try:
            while data_written < len(data):
                written = writer.write(data[data_written:])
                # On Python 2, socket.makefile().write() does not properly implement
                # BytesIO.write(), and always returns None instead of the number of
                # bytes written - but also guarantees that it is always a full write.
                if written is None:
                    break
                data_written += written
            writer.flush()
        except Exception as exc:
            self._log_message("<--", value, logger=log.swallow_exception)
            raise JsonIOError(stream=self, cause=exc)

        self._log_message("<--", value)

    def __repr__(self):
        return fmt("{0}({1!r})", type(self).__name__, self.name)


class MessageDict(collections.OrderedDict):
    """A specialized dict that is used for JSON message payloads - Request.arguments,
    Response.body, and Event.body.

    For all members that normally throw KeyError when a requested key is missing, this
    dict raises InvalidMessageError instead. Thus, a message handler can skip checks
    for missing properties, and just work directly with the payload on the assumption
    that it is valid according to the protocol specification; if anything is missing,
    it will be reported automatically in the proper manner.

    If the value for the requested key is itself a dict, it is returned as is, and not
    automatically converted to MessageDict. Thus, to enable convenient chaining - e.g.
    d["a"]["b"]["c"] - the dict must consistently use MessageDict instances rather than
    vanilla dicts for all its values, recursively. This is guaranteed for the payload
    of all freshly received messages (unless and until it is mutated), but there is no
    such guarantee for outgoing messages.
    """

    def __init__(self, message, items=None):
        assert message is None or isinstance(message, Message)

        if items is None:
            super(MessageDict, self).__init__()
        else:
            super(MessageDict, self).__init__(items)

        self.message = message
        """The Message object that owns this dict.

        For any instance exposed via a Message object corresponding to some incoming
        message, it is guaranteed to reference that Message object. There is no similar
        guarantee for outgoing messages.
        """

    def __repr__(self):
        return fmt("{0!j}", self)

    def __call__(self, key, validate, optional=False):
        """Like get(), but with validation.

        The item is first retrieved as if with self.get(key, default=()) - the default
        value is () rather than None, so that JSON nulls are distinguishable from
        missing properties.

        If optional=True, and the value is (), it's returned as is. Otherwise, the
        item is validated by invoking validate(item) on it.

        If validate=False, it's treated as if it were (lambda x: x) - i.e. any value
        is considered valid, and is returned unchanged. If validate is a type or a
        tuple, it's treated as json.of_type(validate). Otherwise, if validate is not
        callable(), it's treated as json.default(validate).

        If validate() returns successfully, the item is substituted with the value
        it returns - thus, the validator can e.g. replace () with a suitable default
        value for the property.

        If validate() raises TypeError or ValueError, raises InvalidMessageError with
        the same text that applies_to(self.messages).

        See debugpy.common.json for reusable validators.
        """

        if not validate:
            validate = lambda x: x
        elif isinstance(validate, type) or isinstance(validate, tuple):
            validate = json.of_type(validate, optional=optional)
        elif not callable(validate):
            validate = json.default(validate)

        value = self.get(key, ())
        try:
            value = validate(value)
        except (TypeError, ValueError) as exc:
            message = Message if self.message is None else self.message
            err = fmt("{0}", exc)
            if not err.startswith("["):
                err = " " + err
            raise message.isnt_valid("{0!j}{1}", key, err)
        return value

    def _invalid_if_no_key(func):
        def wrap(self, key, *args, **kwargs):
            try:
                return func(self, key, *args, **kwargs)
            except KeyError:
                message = Message if self.message is None else self.message
                raise message.isnt_valid("missing property {0!r}", key)

        return wrap

    __getitem__ = _invalid_if_no_key(collections.OrderedDict.__getitem__)
    __delitem__ = _invalid_if_no_key(collections.OrderedDict.__delitem__)
    pop = _invalid_if_no_key(collections.OrderedDict.pop)

    del _invalid_if_no_key


def _payload(value):
    """JSON validator for message payload.

    If that value is missing or null, it is treated as if it were {}.
    """

    if value is not None and value != ():
        if isinstance(value, dict):  # can be int, str, list...
            assert isinstance(value, MessageDict)
        return value

    # Missing payload. Construct a dummy MessageDict, and make it look like it was
    # deserialized. See JsonMessageChannel._parse_incoming_message for why it needs
    # to have associate_with().

    def associate_with(message):
        value.message = message

    value = MessageDict(None)
    value.associate_with = associate_with
    return value


class Message(object):
    """Represents a fully parsed incoming or outgoing message.

    https://microsoft.github.io/debug-adapter-protocol/specification#protocolmessage
    """

    def __init__(self, channel, seq, json=None):
        self.channel = channel

        self.seq = seq
        """Sequence number of the message in its channel.

        This can be None for synthesized Responses.
        """

        self.json = json
        """For incoming messages, the MessageDict containing raw JSON from which
        this message was originally parsed.
        """

    def __str__(self):
        return fmt("{0!j}", self.json) if self.json is not None else repr(self)

    def describe(self):
        """A brief description of the message that is enough to identify it.

        Examples:
        '#1 request "launch" from IDE'
        '#2 response to #1 request "launch" from IDE'.
        """
        raise NotImplementedError

    @property
    def payload(self):
        """Payload of the message - self.body or self.arguments, depending on the
        message type.
        """
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        """Same as self.payload(...)."""
        return self.payload(*args, **kwargs)

    def __contains__(self, key):
        """Same as (key in self.payload)."""
        return key in self.payload

    def is_event(self, *event):
        """Returns True if this message is an Event of one of the specified types.
        """
        if not isinstance(self, Event):
            return False
        return event == () or self.event in event

    def is_request(self, *command):
        """Returns True if this message is a Request of one of the specified types.
        """
        if not isinstance(self, Request):
            return False
        return command == () or self.command in command

    def is_response(self, *command):
        """Returns True if this message is a Response to a request of one of the
        specified types.
        """
        if not isinstance(self, Response):
            return False
        return command == () or self.request.command in command

    def error(self, exc_type, format_string, *args, **kwargs):
        """Returns a new exception of the specified type from the point at which it is
        invoked, with the specified formatted message as the reason.

        The resulting exception will have its cause set to the Message object on which
        error() was called. Additionally, if that message is a Request, a failure
        response is immediately sent.
        """

        assert issubclass(exc_type, MessageHandlingError)

        silent = kwargs.pop("silent", False)
        reason = fmt(format_string, *args, **kwargs)
        exc = exc_type(reason, self, silent)  # will log it

        if isinstance(self, Request):
            self.respond(exc)
        return exc

    def isnt_valid(self, *args, **kwargs):
        """Same as self.error(InvalidMessageError, ...).
        """
        return self.error(InvalidMessageError, *args, **kwargs)

    def cant_handle(self, *args, **kwargs):
        """Same as self.error(MessageHandlingError, ...).
        """
        return self.error(MessageHandlingError, *args, **kwargs)


class Event(Message):
    """Represents an incoming event.

    https://microsoft.github.io/debug-adapter-protocol/specification#event

    It is guaranteed that body is a MessageDict associated with this Event, and so
    are all the nested dicts in it. If "body" was missing or null in JSON, body is
    an empty dict.

    To handle the event, JsonMessageChannel tries to find a handler for this event in
    JsonMessageChannel.handlers. Given event="X", if handlers.X_event exists, then it
    is the specific handler for this event. Otherwise, handlers.event must exist, and
    it is the generic handler for this event. A missing handler is a fatal error.

    No further incoming messages are processed until the handler returns, except for
    responses to requests that have wait_for_response() invoked on them.

    To report failure to handle the event, the handler must raise an instance of
    MessageHandlingError that applies_to() the Event object it was handling. Any such
    failure is logged, after which the message loop moves on to the next message.

    Helper methods Message.isnt_valid() and Message.cant_handle() can be used to raise
    the appropriate exception type that applies_to() the Event object.
    """

    def __init__(self, channel, seq, event, body, json=None):
        super(Event, self).__init__(channel, seq, json)

        self.event = event

        if isinstance(body, MessageDict) and hasattr(body, "associate_with"):
            body.associate_with(self)
        self.body = body

    def describe(self):
        return fmt("#{0} event {1!j} from {2}", self.seq, self.event, self.channel)

    @property
    def payload(self):
        return self.body

    @staticmethod
    def _parse(channel, message_dict):
        seq = message_dict("seq", int)
        event = message_dict("event", unicode)
        body = message_dict("body", _payload)
        message = Event(channel, seq, event, body, json=message_dict)
        channel._enqueue_handlers(message, message._handle)

    def _handle(self):
        channel = self.channel
        handler = channel._get_handler_for("event", self.event)
        try:
            try:
                result = handler(self)
                assert result is None, fmt(
                    "Handler {0} tried to respond to {1}.",
                    compat.srcnameof(handler),
                    self.describe(),
                )
            except MessageHandlingError as exc:
                if not exc.applies_to(self):
                    raise
                log.error(
                    "Handler {0}\ncouldn't handle {1}:\n{2}",
                    compat.srcnameof(handler),
                    self.describe(),
                    str(exc),
                )
        except Exception:
            log.reraise_exception(
                "Handler {0}\ncouldn't handle {1}:",
                compat.srcnameof(handler),
                self.describe(),
            )


NO_RESPONSE = object()
"""Can be returned from a request handler in lieu of the response body, to indicate
that no response is to be sent.

Request.respond() must be invoked explicitly at some later point to provide a response.
"""


class Request(Message):
    """Represents an incoming or an outgoing request.

    Incoming requests are represented directly by instances of this class.

    Outgoing requests are represented by instances of OutgoingRequest, which provides
    additional functionality to handle responses.

    For incoming requests, it is guaranteed that arguments is a MessageDict associated
    with this Request, and so are all the nested dicts in it. If "arguments" was missing
    or null in JSON, arguments is an empty dict.

    To handle the request, JsonMessageChannel tries to find a handler for this request
    in JsonMessageChannel.handlers. Given command="X", if handlers.X_request exists,
    then it is the specific handler for this request. Otherwise, handlers.request must
    exist, and it is the generic handler for this request. A missing handler is a fatal
    error.

    The handler is then invoked with the Request object as its sole argument.

    If the handler itself invokes respond() on the Request at any point, then it must
    not return any value.

    Otherwise, if the handler returns NO_RESPONSE, no response to the request is sent.
    It must be sent manually at some later point via respond().

    Otherwise, a response to the request is sent with the returned value as the body.

    To fail the request, the handler can return an instance of MessageHandlingError,
    or respond() with one, or raise one such that it applies_to() the Request object
    being handled.

    Helper methods Message.isnt_valid() and Message.cant_handle() can be used to raise
    the appropriate exception type that applies_to() the Request object.
    """

    def __init__(self, channel, seq, command, arguments, json=None):
        super(Request, self).__init__(channel, seq, json)

        self.command = command

        if isinstance(arguments, MessageDict) and hasattr(arguments, "associate_with"):
            arguments.associate_with(self)
        self.arguments = arguments

        self.response = None
        """Response to this request.

        For incoming requests, it is set as soon as the request handler returns.

        For outgoing requests, it is set as soon as the response is received, and
        before self._handle_response is invoked.
        """

    def describe(self):
        return fmt("#{0} request {1!j} from {2}", self.seq, self.command, self.channel)

    @property
    def payload(self):
        return self.arguments

    def respond(self, body):
        assert self.response is None
        d = {"type": "response", "request_seq": self.seq, "command": self.command}

        if isinstance(body, Exception):
            d["success"] = False
            err_text = str(body)
            try:
                err_text = compat.force_unicode(err_text, "utf-8")
            except Exception:
                # On Python 2, the error message might not be Unicode, and we don't
                # really know what encoding it is. So if treating it as UTF-8 failed,
                # use repr() as a fallback - it should escape all non-ASCII chars in
                # the string.
                err_text = compat.force_unicode(repr(body), "ascii", errors="replace")
            d["message"] = err_text
        else:
            d["success"] = True
            if body is not None and body != {}:
                d["body"] = body

        with self.channel._send_message(d) as seq:
            pass
        self.response = Response(self.channel, seq, self, body)

    @staticmethod
    def _parse(channel, message_dict):
        seq = message_dict("seq", int)
        command = message_dict("command", unicode)
        arguments = message_dict("arguments", _payload)
        message = Request(channel, seq, command, arguments, json=message_dict)
        channel._enqueue_handlers(message, message._handle)

    def _handle(self):
        channel = self.channel
        handler = channel._get_handler_for("request", self.command)
        try:
            try:
                result = handler(self)
            except MessageHandlingError as exc:
                if not exc.applies_to(self):
                    raise
                result = exc
                log.error(
                    "Handler {0}\ncouldn't handle {1}:\n{2}",
                    compat.srcnameof(handler),
                    self.describe(),
                    str(exc),
                )

            if result is NO_RESPONSE:
                assert self.response is None, fmt(
                    "Handler {0} for {1} must not return NO_RESPONSE if it has already "
                    "invoked request.respond().",
                    compat.srcnameof(handler),
                    self.describe(),
                )
            elif self.response is not None:
                assert result is None or result is self.response.body, fmt(
                    "Handler {0} for {1} must not return a response body if it has "
                    "already invoked request.respond().",
                    compat.srcnameof(handler),
                    self.describe(),
                )
            else:
                assert result is not None, fmt(
                    "Handler {0} for {1} must either call request.respond() before it "
                    "returns, or return the response body, or return NO_RESPONSE.",
                    compat.srcnameof(handler),
                    self.describe(),
                )
                try:
                    self.respond(result)
                except NoMoreMessages:
                    log.warning(
                        "Channel was closed before the response from handler {0} to {1} could be sent",
                        compat.srcnameof(handler),
                        self.describe(),
                    )

        except Exception:
            log.reraise_exception(
                "Handler {0}\ncouldn't handle {1}:",
                compat.srcnameof(handler),
                self.describe(),
            )


class OutgoingRequest(Request):
    """Represents an outgoing request, for which it is possible to wait for a
    response to be received, and register a response handler.
    """

    _parse = _handle = None

    def __init__(self, channel, seq, command, arguments):
        super(OutgoingRequest, self).__init__(channel, seq, command, arguments)
        self._response_handlers = []

    def describe(self):
        return fmt("#{0} request {1!j} to {2}", self.seq, self.command, self.channel)

    def wait_for_response(self, raise_if_failed=True):
        """Waits until a response is received for this request, records the Response
        object for it in self.response, and returns response.body.

        If no response was received from the other party before the channel closed,
        self.response is a synthesized Response with body=NoMoreMessages().

        If raise_if_failed=True and response.success is False, raises response.body
        instead of returning.
        """

        with self.channel:
            while self.response is None:
                self.channel._handlers_enqueued.wait()

        if raise_if_failed and not self.response.success:
            raise self.response.body
        return self.response.body

    def on_response(self, response_handler):
        """Registers a handler to invoke when a response is received for this request.
        The handler is invoked with Response as its sole argument.

        If response has already been received, invokes the handler immediately.

        It is guaranteed that self.response is set before the handler is invoked.
        If no response was received from the other party before the channel closed,
        self.response is a dummy Response with body=NoMoreMessages().

        The handler is always invoked asynchronously on an unspecified background
        thread - thus, the caller of on_response() can never be blocked or deadlocked
        by the handler.

        No further incoming messages are processed until the handler returns, except for
        responses to requests that have wait_for_response() invoked on them.
        """

        with self.channel:
            self._response_handlers.append(response_handler)
            self._enqueue_response_handlers()

    def _enqueue_response_handlers(self):
        response = self.response
        if response is None:
            # Response._parse() will submit the handlers when response is received.
            return

        def run_handlers():
            for handler in handlers:
                try:
                    try:
                        handler(response)
                    except MessageHandlingError as exc:
                        if not exc.applies_to(response):
                            raise
                        log.error(
                            "Handler {0}\ncouldn't handle {1}:\n{2}",
                            compat.srcnameof(handler),
                            response.describe(),
                            str(exc),
                        )
                except Exception:
                    log.reraise_exception(
                        "Handler {0}\ncouldn't handle {1}:",
                        compat.srcnameof(handler),
                        response.describe(),
                    )

        handlers = self._response_handlers[:]
        self.channel._enqueue_handlers(response, run_handlers)
        del self._response_handlers[:]


class Response(Message):
    """Represents an incoming or an outgoing response to a Request.

    https://microsoft.github.io/debug-adapter-protocol/specification#response

    error_message corresponds to "message" in JSON, and is renamed for clarity.

    If success is False, body is None. Otherwise, it is a MessageDict associated
    with this Response, and so are all the nested dicts in it. If "body" was missing
    or null in JSON, body is an empty dict.

    If this is a response to an outgoing request, it will be handled by the handler
    registered via self.request.on_response(), if any.

    Regardless of whether there is such a handler, OutgoingRequest.wait_for_response()
    can also be used to retrieve and handle the response. If there is a handler, it is
    executed before wait_for_response() returns.

    No further incoming messages are processed until the handler returns, except for
    responses to requests that have wait_for_response() invoked on them.

    To report failure to handle the event, the handler must raise an instance of
    MessageHandlingError that applies_to() the Response object it was handling. Any
    such failure is logged, after which the message loop moves on to the next message.

    Helper methods Message.isnt_valid() and Message.cant_handle() can be used to raise
    the appropriate exception type that applies_to() the Response object.
    """

    def __init__(self, channel, seq, request, body, json=None):
        super(Response, self).__init__(channel, seq, json)

        self.request = request
        """The request to which this is the response."""

        if isinstance(body, MessageDict) and hasattr(body, "associate_with"):
            body.associate_with(self)
        self.body = body
        """Body of the response if the request was successful, or an instance
        of some class derived from Exception it it was not.

        If a response was received from the other side, but request failed, it is an
        instance of MessageHandlingError containing the received error message. If the
        error message starts with InvalidMessageError.PREFIX, then it's an instance of
        the InvalidMessageError specifically, and that prefix is stripped.

        If no response was received from the other party before the channel closed,
        it is an instance of NoMoreMessages.
        """

    def describe(self):
        return fmt("#{0} response to {1}", self.seq, self.request.describe())

    @property
    def payload(self):
        return self.body

    @property
    def success(self):
        """Whether the request succeeded or not.
        """
        return not isinstance(self.body, Exception)

    @property
    def result(self):
        """Result of the request. Returns the value of response.body, unless it
        is an exception, in which case it is raised instead.
        """
        if self.success:
            return self.body
        else:
            raise self.body

    @staticmethod
    def _parse(channel, message_dict, body=None):
        seq = message_dict("seq", int) if (body is None) else None
        request_seq = message_dict("request_seq", int)
        command = message_dict("command", unicode)
        success = message_dict("success", bool)
        if body is None:
            if success:
                body = message_dict("body", _payload)
            else:
                error_message = message_dict("message", unicode)
                exc_type = MessageHandlingError
                if error_message.startswith(InvalidMessageError.PREFIX):
                    error_message = error_message[len(InvalidMessageError.PREFIX) :]
                    exc_type = InvalidMessageError
                body = exc_type(error_message, silent=True)

        try:
            with channel:
                request = channel._sent_requests.pop(request_seq)
                known_request = True
        except KeyError:
            # Synthetic Request that only has seq and command as specified in response
            # JSON, for error reporting purposes.
            request = OutgoingRequest(channel, request_seq, command, "<unknown>")
            known_request = False

        if not success:
            body.cause = request

        response = Response(channel, seq, request, body, json=message_dict)

        with channel:
            request.response = response
            request._enqueue_response_handlers()

        if known_request:
            return response
        else:
            raise response.isnt_valid(
                "request_seq={0} does not match any known request", request_seq
            )


class Disconnect(Message):
    """A dummy message used to represent disconnect. It's always the last message
    received from any channel.
    """

    def __init__(self, channel):
        super(Disconnect, self).__init__(channel, None)

    def describe(self):
        return fmt("disconnect from {0}", self.channel)


class MessageHandlingError(Exception):
    """Indicates that a message couldn't be handled for some reason.

    If the reason is a contract violation - i.e. the message that was handled did not
    conform to the protocol specification - InvalidMessageError, which is a subclass,
    should be used instead.

    If any message handler raises an exception not derived from this class, it will
    escape the message loop unhandled, and terminate the process.

    If any message handler raises this exception, but applies_to(message) is False, it
    is treated as if it was a generic exception, as desribed above. Thus, if a request
    handler issues another request of its own, and that one fails, the failure is not
    silently propagated. However, a request that is delegated via Request.delegate()
    will also propagate failures back automatically. For manual propagation, catch the
    exception, and call exc.propagate().

    If any event handler raises this exception, and applies_to(event) is True, the
    exception is silently swallowed by the message loop.

    If any request handler raises this exception, and applies_to(request) is True, the
    exception is silently swallowed by the message loop, and a failure response is sent
    with "message" set to str(reason).

    Note that, while errors are not logged when they're swallowed by the message loop,
    by that time they have already been logged by their __init__ (when instantiated).
    """

    def __init__(self, reason, cause=None, silent=False):
        """Creates a new instance of this class, and immediately logs the exception.

        Message handling errors are logged immediately unless silent=True, so that the
        precise context in which they occured can be determined from the surrounding
        log entries.
        """

        self.reason = reason
        """Why it couldn't be handled. This can be any object, but usually it's either
        str or Exception.
        """

        assert cause is None or isinstance(cause, Message)
        self.cause = cause
        """The Message object for the message that couldn't be handled. For responses
        to unknown requests, this is a synthetic Request.
        """

        if not silent:
            try:
                raise self
            except MessageHandlingError:
                log.swallow_exception()

    def __hash__(self):
        return hash((self.reason, id(self.cause)))

    def __eq__(self, other):
        if not isinstance(other, MessageHandlingError):
            return NotImplemented
        if type(self) is not type(other):
            return NotImplemented
        if self.reason != other.reason:
            return False
        if self.cause is not None and other.cause is not None:
            if self.cause.seq != other.cause.seq:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return str(self.reason)

    def __repr__(self):
        s = type(self).__name__
        if self.cause is None:
            s += fmt("(reason={0!r})", self.reason)
        else:
            s += fmt(
                "(channel={0!r}, cause={1!r}, reason={2!r})",
                self.cause.channel.name,
                self.cause.seq,
                self.reason,
            )
        return s

    def applies_to(self, message):
        """Whether this MessageHandlingError can be treated as a reason why the
        handling of message failed.

        If self.cause is None, this is always true.

        If self.cause is not None, this is only true if cause is message.
        """
        return self.cause is None or self.cause is message

    def propagate(self, new_cause):
        """Propagates this error, raising a new instance of the same class with the
        same reason, but a different cause.
        """
        raise type(self)(self.reason, new_cause, silent=True)


class InvalidMessageError(MessageHandlingError):
    """Indicates that an incoming message did not follow the protocol specification -
    for example, it was missing properties that are required, or the message itself
    is not allowed in the current state.

    Raised by MessageDict in lieu of KeyError for missing keys.
    """

    PREFIX = "Invalid message: "
    """Automatically prepended to the "message" property in JSON responses, when the
    handler raises InvalidMessageError.

    If a failed response has "message" property that starts with this prefix, it is
    reported as InvalidMessageError rather than MessageHandlingError.
    """

    def __str__(self):
        return InvalidMessageError.PREFIX + str(self.reason)


class JsonMessageChannel(object):
    """Implements a JSON message channel on top of a raw JSON message stream, with
    support for DAP requests, responses, and events.

    The channel can be locked for exclusive use via the with-statement::

        with channel:
            channel.send_request(...)
            # No interleaving messages can be sent here from other threads.
            channel.send_event(...)
    """

    def __init__(self, stream, handlers=None, name=None):
        self.stream = stream
        self.handlers = handlers
        self.name = name if name is not None else stream.name
        self.started = False
        self._lock = threading.RLock()
        self._closed = False
        self._seq_iter = itertools.count(1)
        self._sent_requests = {}  # {seq: Request}
        self._handler_queue = []  # [(what, handler)]
        self._handlers_enqueued = threading.Condition(self._lock)
        self._handler_thread = None
        self._parser_thread = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return fmt("{0}({1!r})", type(self).__name__, self.name)

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._lock.release()

    def close(self):
        """Closes the underlying stream.

        This does not immediately terminate any handlers that are already executing,
        but they will be unable to respond. No new request or event handlers will
        execute after this method is called, even for messages that have already been
        received. However, response handlers will continue to executed for any request
        that is still pending, as will any handlers registered via on_response().
        """
        with self:
            if not self._closed:
                self._closed = True
                self.stream.close()

    def start(self):
        """Starts a message loop which parses incoming messages and invokes handlers
        for them on a background thread, until the channel is closed.

        Incoming messages, including responses to requests, will not be processed at
        all until this is invoked.
        """

        assert not self.started
        self.started = True

        self._parser_thread = threading.Thread(
            target=self._parse_incoming_messages, name=fmt("{0} message parser", self)
        )
        self._parser_thread.pydev_do_not_trace = True
        self._parser_thread.is_pydev_daemon_thread = True
        self._parser_thread.daemon = True
        self._parser_thread.start()

    def wait(self):
        """Waits for the message loop to terminate, and for all enqueued Response
        message handlers to finish executing.
        """
        parser_thread = self._parser_thread
        try:
            if parser_thread is not None:
                parser_thread.join()
        except AssertionError:
            log.debug("Handled error joining parser thread.")
        try:
            handler_thread = self._handler_thread
            if handler_thread is not None:
                handler_thread.join()
        except AssertionError:
            log.debug("Handled error joining handler thread.")

    # Order of keys for _prettify() - follows the order of properties in
    # https://microsoft.github.io/debug-adapter-protocol/specification
    _prettify_order = (
        "seq",
        "type",
        "request_seq",
        "success",
        "command",
        "event",
        "message",
        "arguments",
        "body",
        "error",
    )

    def _prettify(self, message_dict):
        """Reorders items in a MessageDict such that it is more readable.
        """
        for key in self._prettify_order:
            if key not in message_dict:
                continue
            value = message_dict[key]
            del message_dict[key]
            message_dict[key] = value

    @contextlib.contextmanager
    def _send_message(self, message):
        """Sends a new message to the other party.

        Generates a new sequence number for the message, and provides it to the
        caller before the message is sent, using the context manager protocol::

            with send_message(...) as seq:
                # The message hasn't been sent yet.
                ...
            # Now the message has been sent.

        Safe to call concurrently for the same channel from different threads.
        """

        assert "seq" not in message
        with self:
            seq = next(self._seq_iter)

        message = MessageDict(None, message)
        message["seq"] = seq
        self._prettify(message)

        with self:
            yield seq
            self.stream.write_json(message)

    def send_request(self, command, arguments=None, on_before_send=None):
        """Sends a new request, and returns the OutgoingRequest object for it.

        If arguments is None or {}, "arguments" will be omitted in JSON.

        If on_before_send is not None, invokes on_before_send() with the request
        object as the sole argument, before the request actually gets sent.

        Does not wait for response - use OutgoingRequest.wait_for_response().

        Safe to call concurrently for the same channel from different threads.
        """

        d = {"type": "request", "command": command}
        if arguments is not None and arguments != {}:
            d["arguments"] = arguments

        with self._send_message(d) as seq:
            request = OutgoingRequest(self, seq, command, arguments)
            if on_before_send is not None:
                on_before_send(request)
            self._sent_requests[seq] = request
        return request

    def send_event(self, event, body=None):
        """Sends a new event.

        If body is None or {}, "body" will be omitted in JSON.

        Safe to call concurrently for the same channel from different threads.
        """

        d = {"type": "event", "event": event}
        if body is not None and body != {}:
            d["body"] = body

        with self._send_message(d):
            pass

    def request(self, *args, **kwargs):
        """Same as send_request(...).wait_for_response()
        """
        return self.send_request(*args, **kwargs).wait_for_response()

    def propagate(self, message):
        """Sends a new message with the same type and payload.

        If it was a request, returns the new OutgoingRequest object for it.
        """
        assert message.is_request() or message.is_event()
        if message.is_request():
            return self.send_request(message.command, message.arguments)
        else:
            self.send_event(message.event, message.body)

    def delegate(self, message):
        """Like propagate(message).wait_for_response(), but will also propagate
        any resulting MessageHandlingError back.
        """
        try:
            result = self.propagate(message)
            if result.is_request():
                result = result.wait_for_response()
            return result
        except MessageHandlingError as exc:
            exc.propagate(message)

    def _parse_incoming_messages(self):
        log.debug("Starting message loop for channel {0}", self)
        try:
            while True:
                self._parse_incoming_message()

        except NoMoreMessages as exc:
            log.debug("Exiting message loop for channel {0}: {1}", self, exc)
            with self:
                # Generate dummy responses for all outstanding requests.
                err_message = compat.force_unicode(str(exc), "utf-8", errors="replace")

                # Response._parse() will remove items from _sent_requests, so
                # make a snapshot before iterating.
                sent_requests = list(self._sent_requests.values())

                for request in sent_requests:
                    response_json = MessageDict(
                        None,
                        {
                            "seq": -1,
                            "request_seq": request.seq,
                            "command": request.command,
                            "success": False,
                            "message": err_message,
                        },
                    )
                    Response._parse(self, response_json, body=exc)
                assert not len(self._sent_requests)

                self._enqueue_handlers(Disconnect(self), self._handle_disconnect)
                self.close()

    _message_parsers = {
        "event": Event._parse,
        "request": Request._parse,
        "response": Response._parse,
    }

    def _parse_incoming_message(self):
        """Reads incoming messages, parses them, and puts handlers into the queue
        for _run_handlers() to invoke, until the channel is closed.
        """

        # Set up a dedicated decoder for this message, to create MessageDict instances
        # for all JSON objects, and track them so that they can be later wired up to
        # the Message they belong to, once it is instantiated.
        def object_hook(d):
            d = MessageDict(None, d)
            if "seq" in d:
                self._prettify(d)
            d.associate_with = associate_with
            message_dicts.append(d)
            return d

        # A hack to work around circular dependency between messages, and instances of
        # MessageDict in their payload. We need to set message for all of them, but it
        # cannot be done until the actual Message is created - which happens after the
        # dicts are created during deserialization.
        #
        # So, upon deserialization, every dict in the message payload gets a method
        # that can be called to set MessageDict.message for *all* dicts belonging to
        # that message. This method can then be invoked on the top-level dict by the
        # parser, after it has parsed enough of the dict to create the appropriate
        # instance of Event, Request, or Response for this message.
        def associate_with(message):
            for d in message_dicts:
                d.message = message
                del d.associate_with

        message_dicts = []
        decoder = self.stream.json_decoder_factory(object_hook=object_hook)
        message_dict = self.stream.read_json(decoder)
        assert isinstance(message_dict, MessageDict)  # make sure stream used decoder

        msg_type = message_dict("type", json.enum("event", "request", "response"))
        parser = self._message_parsers[msg_type]
        try:
            parser(self, message_dict)
        except InvalidMessageError as exc:
            log.error(
                "Failed to parse message in channel {0}: {1} in:\n{2!j}",
                self,
                str(exc),
                message_dict,
            )
        except Exception as exc:
            if isinstance(exc, NoMoreMessages) and exc.stream is self.stream:
                raise
            log.swallow_exception(
                "Fatal error in channel {0} while parsing:\n{1!j}", self, message_dict
            )
            os._exit(1)

    def _enqueue_handlers(self, what, *handlers):
        """Enqueues handlers for _run_handlers() to run.

        `what` is the Message being handled, and is used for logging purposes.

        If the background thread with _run_handlers() isn't running yet, starts it.
        """

        with self:
            self._handler_queue.extend((what, handler) for handler in handlers)
            self._handlers_enqueued.notify_all()

            # If there is anything to handle, but there's no handler thread yet,
            # spin it up. This will normally happen only once, on the first call
            # to _enqueue_handlers(), and that thread will run all the handlers
            # for parsed messages. However, this can also happen is somebody calls
            # Request.on_response() - possibly concurrently from multiple threads -
            # after the channel has already been closed, and the initial handler
            # thread has exited. In this case, we spin up a new thread just to run
            # the enqueued response handlers, and it will exit as soon as it's out
            # of handlers to run.
            if len(self._handler_queue) and self._handler_thread is None:
                self._handler_thread = threading.Thread(
                    target=self._run_handlers, name=fmt("{0} message handler", self)
                )
                self._handler_thread.pydev_do_not_trace = True
                self._handler_thread.is_pydev_daemon_thread = True
                self._handler_thread.start()

    def _run_handlers(self):
        """Runs enqueued handlers until the channel is closed, or until the handler
        queue is empty once the channel is closed.
        """

        while True:
            with self:
                closed = self._closed
            if closed:
                # Wait for the parser thread to wrap up and enqueue any remaining
                # handlers, if it is still running.
                self._parser_thread.join()
                # From this point on, _enqueue_handlers() can only get called
                # from Request.on_response().

            with self:
                if not closed and not len(self._handler_queue):
                    # Wait for something to process.
                    self._handlers_enqueued.wait()

                # Make a snapshot before releasing the lock.
                handlers = self._handler_queue[:]
                del self._handler_queue[:]

                if closed and not len(handlers):
                    # Nothing to process, channel is closed, and parser thread is
                    # not running anymore - time to quit! If Request.on_response()
                    # needs to call _enqueue_handlers() later, it will spin up
                    # a new handler thread.
                    self._handler_thread = None
                    return

            for what, handler in handlers:
                # If the channel is closed, we don't want to process any more events
                # or requests - only responses and the final disconnect handler. This
                # is to guarantee that if a handler calls close() on its own channel,
                # the corresponding request or event is the last thing to be processed.
                if closed and handler in (Event._handle, Request._handle):
                    continue

                with log.prefixed("/handling {0}/\n", what.describe()):
                    try:
                        handler()
                    except Exception:
                        # It's already logged by the handler, so just fail fast.
                        self.close()
                        os._exit(1)

    def _get_handler_for(self, type, name):
        """Returns the handler for a message of a given type.
        """

        with self:
            handlers = self.handlers

        for handler_name in (name + "_" + type, type):
            try:
                return getattr(handlers, handler_name)
            except AttributeError:
                continue

        raise AttributeError(
            fmt(
                "handler object {0} for channel {1} has no handler for {2} {3!r}",
                compat.srcnameof(handlers),
                self,
                type,
                name,
            )
        )

    def _handle_disconnect(self):
        handler = getattr(self.handlers, "disconnect", lambda: None)
        try:
            handler()
        except Exception:
            log.reraise_exception(
                "Handler {0}\ncouldn't handle disconnect from {1}:",
                compat.srcnameof(handler),
                self,
            )


class MessageHandlers(object):
    """A simple delegating message handlers object for use with JsonMessageChannel.
    For every argument provided, the object gets an attribute with the corresponding
    name and value.
    """

    def __init__(self, **kwargs):
        for name, func in kwargs.items():
            setattr(self, name, func)
