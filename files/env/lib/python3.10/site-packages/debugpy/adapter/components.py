# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

import functools

from debugpy.common import fmt, json, log, messaging, util


ACCEPT_CONNECTIONS_TIMEOUT = 10


class ComponentNotAvailable(Exception):
    def __init__(self, type):
        super(ComponentNotAvailable, self).__init__(
            fmt("{0} is not available", type.__name__)
        )


class Component(util.Observable):
    """A component managed by a debug adapter: client, launcher, or debug server.

    Every component belongs to a Session, which is used for synchronization and
    shared data.

    Every component has its own message channel, and provides message handlers for
    that channel. All handlers should be decorated with @Component.message_handler,
    which ensures that Session is locked for the duration of the handler. Thus, only
    one handler is running at any given time across all components, unless the lock
    is released explicitly or via Session.wait_for().

    Components report changes to their attributes to Session, allowing one component
    to wait_for() a change caused by another component.
    """

    def __init__(self, session, stream=None, channel=None):
        assert (stream is None) ^ (channel is None)

        try:
            lock_held = session.lock.acquire(blocking=False)
            assert lock_held, "__init__ of a Component subclass must lock its Session"
        finally:
            session.lock.release()

        super(Component, self).__init__()

        self.session = session

        if channel is None:
            stream.name = str(self)
            channel = messaging.JsonMessageChannel(stream, self)
            channel.start()
        else:
            channel.name = channel.stream.name = str(self)
            channel.handlers = self
        self.channel = channel
        self.is_connected = True

        # Do this last to avoid triggering useless notifications for assignments above.
        self.observers += [lambda *_: self.session.notify_changed()]

    def __str__(self):
        return fmt("{0}[{1}]", type(self).__name__, self.session.id)

    @property
    def client(self):
        return self.session.client

    @property
    def launcher(self):
        return self.session.launcher

    @property
    def server(self):
        return self.session.server

    def wait_for(self, *args, **kwargs):
        return self.session.wait_for(*args, **kwargs)

    @staticmethod
    def message_handler(f):
        """Applied to a message handler to automatically lock and unlock the session
        for its duration, and to validate the session state.

        If the handler raises ComponentNotAvailable or JsonIOError, converts it to
        Message.cant_handle().
        """

        @functools.wraps(f)
        def lock_and_handle(self, message):
            try:
                with self.session:
                    return f(self, message)
            except ComponentNotAvailable as exc:
                raise message.cant_handle("{0}", exc, silent=True)
            except messaging.MessageHandlingError as exc:
                if exc.cause is message:
                    raise
                else:
                    exc.propagate(message)
            except messaging.JsonIOError as exc:
                raise message.cant_handle(
                    "{0} disconnected unexpectedly", exc.stream.name, silent=True
                )

        return lock_and_handle

    def disconnect(self):
        with self.session:
            self.is_connected = False
            self.session.finalize(fmt("{0} has disconnected", self))


def missing(session, type):
    class Missing(object):
        """A dummy component that raises ComponentNotAvailable whenever some
        attribute is accessed on it.
        """

        __getattr__ = __setattr__ = lambda self, *_: report()
        __bool__ = __nonzero__ = lambda self: False

    def report():
        try:
            raise ComponentNotAvailable(type)
        except Exception as exc:
            log.reraise_exception("{0} in {1}", exc, session)

    return Missing()


class Capabilities(dict):
    """A collection of feature flags for a component. Corresponds to JSON properties
    in the DAP "initialize" request or response, other than those that identify the
    party.
    """

    PROPERTIES = {}
    """JSON property names and default values for the the capabilities represented
    by instances of this class. Keys are names, and values are either default values
    or validators.

    If the value is callable, it must be a JSON validator; see debugpy.common.json for
    details. If the value is not callable, it is as if json.default(value) validator
    was used instead.
    """

    def __init__(self, component, message):
        """Parses an "initialize" request or response and extracts the feature flags.

        For every "X" in self.PROPERTIES, sets self["X"] to the corresponding value
        from message.payload if it's present there, or to the default value otherwise.
        """

        assert message.is_request("initialize") or message.is_response("initialize")

        self.component = component

        payload = message.payload
        for name, validate in self.PROPERTIES.items():
            value = payload.get(name, ())
            if not callable(validate):
                validate = json.default(validate)

            try:
                value = validate(value)
            except Exception as exc:
                raise message.isnt_valid("{0!j} {1}", name, exc)

            assert value != (), fmt(
                "{0!j} must provide a default value for missing properties.", validate
            )
            self[name] = value

        log.debug("{0}", self)

    def __repr__(self):
        return fmt("{0}: {1!j}", type(self).__name__, dict(self))

    def require(self, *keys):
        for key in keys:
            if not self[key]:
                raise messaging.MessageHandlingError(
                    fmt("{0} does not have capability {1!j}", self.component, key)
                )
