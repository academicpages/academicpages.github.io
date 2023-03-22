# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""Base Widget class.  Allows user to create widgets in the back-end that render
in the IPython notebook front-end.
"""

from contextlib import contextmanager
try:
    from collections.abc import Iterable
except ImportError:
    # Python 2.7
    from collections import Iterable

from IPython.core.getipython import get_ipython
from ipykernel.comm import Comm
from traitlets import (
    HasTraits, Unicode, Dict, Instance, List, Int, Set, Bytes, observe, default, Container,
    Undefined)
from ipython_genutils.py3compat import string_types, PY3
from IPython.display import display
from json import loads as jsonloads, dumps as jsondumps

from base64 import standard_b64encode

from .._version import __protocol_version__, __jupyter_widgets_base_version__
PROTOCOL_VERSION_MAJOR = __protocol_version__.split('.')[0]

def _widget_to_json(x, obj):
    if isinstance(x, dict):
        return {k: _widget_to_json(v, obj) for k, v in x.items()}
    elif isinstance(x, (list, tuple)):
        return [_widget_to_json(v, obj) for v in x]
    elif isinstance(x, Widget):
        return "IPY_MODEL_" + x.model_id
    else:
        return x

def _json_to_widget(x, obj):
    if isinstance(x, dict):
        return {k: _json_to_widget(v, obj) for k, v in x.items()}
    elif isinstance(x, (list, tuple)):
        return [_json_to_widget(v, obj) for v in x]
    elif isinstance(x, string_types) and x.startswith('IPY_MODEL_') and x[10:] in Widget.widgets:
        return Widget.widgets[x[10:]]
    else:
        return x

widget_serialization = {
    'from_json': _json_to_widget,
    'to_json': _widget_to_json
}

if PY3:
    _binary_types = (memoryview, bytearray, bytes)
else:
    _binary_types = (memoryview, bytearray)

def _put_buffers(state, buffer_paths, buffers):
    """The inverse of _remove_buffers, except here we modify the existing dict/lists.
    Modifying should be fine, since this is used when state comes from the wire.
    """
    for buffer_path, buffer in zip(buffer_paths, buffers):
        # we'd like to set say sync_data['x'][0]['y'] = buffer
        # where buffer_path in this example would be ['x', 0, 'y']
        obj = state
        for key in buffer_path[:-1]:
            obj = obj[key]
        obj[buffer_path[-1]] = buffer

def _separate_buffers(substate, path, buffer_paths, buffers):
    """For internal, see _remove_buffers"""
    # remove binary types from dicts and lists, but keep track of their paths
    # any part of the dict/list that needs modification will be cloned, so the original stays untouched
    # e.g. {'x': {'ar': ar}, 'y': [ar2, ar3]}, where ar/ar2/ar3 are binary types
    # will result in {'x': {}, 'y': [None, None]}, [ar, ar2, ar3], [['x', 'ar'], ['y', 0], ['y', 1]]
    # instead of removing elements from the list, this will make replacing the buffers on the js side much easier
    if isinstance(substate, (list, tuple)):
        is_cloned = False
        for i, v in enumerate(substate):
            if isinstance(v, _binary_types):
                if not is_cloned:
                    substate = list(substate) # shallow clone list/tuple
                    is_cloned = True
                substate[i] = None
                buffers.append(v)
                buffer_paths.append(path + [i])
            elif isinstance(v, (dict, list, tuple)):
                vnew = _separate_buffers(v, path + [i], buffer_paths, buffers)
                if v is not vnew: # only assign when value changed
                    if not is_cloned:
                        substate = list(substate) # clone list/tuple
                        is_cloned = True
                    substate[i] = vnew
    elif isinstance(substate, dict):
        is_cloned = False
        for k, v in substate.items():
            if isinstance(v, _binary_types):
                if not is_cloned:
                    substate = dict(substate) # shallow clone dict
                    is_cloned = True
                del substate[k]
                buffers.append(v)
                buffer_paths.append(path + [k])
            elif isinstance(v, (dict, list, tuple)):
                vnew = _separate_buffers(v, path + [k], buffer_paths, buffers)
                if v is not vnew: # only assign when value changed
                    if not is_cloned:
                        substate = dict(substate) # clone list/tuple
                        is_cloned = True
                    substate[k] = vnew
    else:
        raise ValueError("expected state to be a list or dict, not %r" % substate)
    return substate

def _remove_buffers(state):
    """Return (state_without_buffers, buffer_paths, buffers) for binary message parts

    A binary message part is a memoryview, bytearray, or python 3 bytes object.

    As an example:
    >>> state = {'plain': [0, 'text'], 'x': {'ar': memoryview(ar1)}, 'y': {'shape': (10,10), 'data': memoryview(ar2)}}
    >>> _remove_buffers(state)
    ({'plain': [0, 'text']}, {'x': {}, 'y': {'shape': (10, 10)}}, [['x', 'ar'], ['y', 'data']],
     [<memory at 0x107ffec48>, <memory at 0x107ffed08>])
    """
    buffer_paths, buffers = [], []
    state = _separate_buffers(state, [], buffer_paths, buffers)
    return state, buffer_paths, buffers

def _buffer_list_equal(a, b):
    """Compare two lists of buffers for equality.

    Used to decide whether two sequences of buffers (memoryviews,
    bytearrays, or python 3 bytes) differ, such that a sync is needed.

    Returns True if equal, False if unequal
    """
    if len(a) != len(b):
        return False
    if a == b:
        return True
    for ia, ib in zip(a, b):
        # Check byte equality, since bytes are what is actually synced
        # NOTE: Simple ia != ib does not always work as intended, as
        # e.g. memoryview(np.frombuffer(ia, dtype='float32')) !=
        # memoryview(np.frombuffer(b)), since the format info differs.
        if PY3:
            # compare without copying
            if memoryview(ia).cast('B') != memoryview(ib).cast('B'):
                return False
        else:
            # python 2 doesn't have memoryview.cast, so we may have to copy
            if isinstance(ia, memoryview) and ia.format != 'B':
                ia = ia.tobytes()
            if isinstance(ib, memoryview) and ib.format != 'B':
                ib = ib.tobytes()
            if ia != ib:
                return False
    return True


class LoggingHasTraits(HasTraits):
    """A parent class for HasTraits that log.
    Subclasses have a log trait, and the default behavior
    is to get the logger from the currently running Application.
    """
    log = Instance('logging.Logger')
    @default('log')
    def _log_default(self):
        from traitlets import log
        return log.get_logger()


class CallbackDispatcher(LoggingHasTraits):
    """A structure for registering and running callbacks"""
    callbacks = List()

    def __call__(self, *args, **kwargs):
        """Call all of the registered callbacks."""
        value = None
        for callback in self.callbacks:
            try:
                local_value = callback(*args, **kwargs)
            except Exception as e:
                ip = get_ipython()
                if ip is None:
                    self.log.warning("Exception in callback %s: %s", callback, e, exc_info=True)
                else:
                    ip.showtraceback()
            else:
                value = local_value if local_value is not None else value
        return value

    def register_callback(self, callback, remove=False):
        """(Un)Register a callback

        Parameters
        ----------
        callback: method handle
            Method to be registered or unregistered.
        remove=False: bool
            Whether to unregister the callback."""

        # (Un)Register the callback.
        if remove and callback in self.callbacks:
            self.callbacks.remove(callback)
        elif not remove and callback not in self.callbacks:
            self.callbacks.append(callback)

def _show_traceback(method):
    """decorator for showing tracebacks in IPython"""
    def m(self, *args, **kwargs):
        try:
            return(method(self, *args, **kwargs))
        except Exception as e:
            ip = get_ipython()
            if ip is None:
                self.log.warning("Exception in widget method %s: %s", method, e, exc_info=True)
            else:
                ip.showtraceback()
    return m


class WidgetRegistry(object):

    def __init__(self):
        self._registry = {}

    def register(self, model_module, model_module_version_range, model_name, view_module, view_module_version_range, view_name, klass):
        """Register a value"""
        model_module = self._registry.setdefault(model_module, {})
        model_version = model_module.setdefault(model_module_version_range, {})
        model_name = model_version.setdefault(model_name, {})
        view_module = model_name.setdefault(view_module, {})
        view_version = view_module.setdefault(view_module_version_range, {})
        view_version[view_name] = klass

    def get(self, model_module, model_module_version, model_name, view_module, view_module_version, view_name):
        """Get a value"""
        module_versions = self._registry[model_module]
        # The python semver module doesn't work well, for example, it can't do match('3', '*')
        # so we just take the first model module version.
        #model_names = next(v for k, v in module_versions.items()
        #                   if semver.match(model_module_version, k))
        model_names = list(module_versions.values())[0]
        view_modules = model_names[model_name]
        view_versions = view_modules[view_module]
        # The python semver module doesn't work well, so we just take the first view module version
        #view_names = next(v for k, v in view_versions.items()
        #                  if semver.match(view_module_version, k))
        view_names = list(view_versions.values())[0]
        widget_class = view_names[view_name]
        return widget_class

    def items(self):
        for model_module, mm in sorted(self._registry.items()):
            for model_version, mv in sorted(mm.items()):
                for model_name, vm in sorted(mv.items()):
                    for view_module, vv in sorted(vm.items()):
                        for view_version, vn in sorted(vv.items()):
                            for view_name, widget in sorted(vn.items()):
                                    yield (model_module, model_version, model_name, view_module, view_version, view_name), widget

def register(name=''):
    "For backwards compatibility, we support @register(name) syntax."
    def reg(widget):
        """A decorator registering a widget class in the widget registry."""
        w = widget.class_traits()
        Widget.widget_types.register(w['_model_module'].default_value,
                                    w['_model_module_version'].default_value,
                                    w['_model_name'].default_value,
                                    w['_view_module'].default_value,
                                    w['_view_module_version'].default_value,
                                    w['_view_name'].default_value,
                                    widget)
        return widget
    if isinstance(name, string_types):
        import warnings
        warnings.warn("Widget registration using a string name has been deprecated. Widget registration now uses a plain `@register` decorator.", DeprecationWarning)
        return reg
    else:
        return reg(name)


class Widget(LoggingHasTraits):
    #-------------------------------------------------------------------------
    # Class attributes
    #-------------------------------------------------------------------------
    _widget_construction_callback = None

    # widgets is a dictionary of all active widget objects
    widgets = {}

    # widget_types is a registry of widgets by module, version, and name:
    widget_types = WidgetRegistry()

    @classmethod
    def close_all(cls):
        for widget in list(cls.widgets.values()):
            widget.close()


    @staticmethod
    def on_widget_constructed(callback):
        """Registers a callback to be called when a widget is constructed.

        The callback must have the following signature:
        callback(widget)"""
        Widget._widget_construction_callback = callback

    @staticmethod
    def _call_widget_constructed(widget):
        """Static method, called when a widget is constructed."""
        if Widget._widget_construction_callback is not None and callable(Widget._widget_construction_callback):
            Widget._widget_construction_callback(widget)

    @staticmethod
    def handle_comm_opened(comm, msg):
        """Static method, called when a widget is constructed."""
        version = msg.get('metadata', {}).get('version', '')
        if version.split('.')[0] != PROTOCOL_VERSION_MAJOR:
            raise ValueError("Incompatible widget protocol versions: received version %r, expected version %r"%(version, __protocol_version__))
        data = msg['content']['data']
        state = data['state']

        # Find the widget class to instantiate in the registered widgets
        widget_class = Widget.widget_types.get(state['_model_module'],
                                               state['_model_module_version'],
                                               state['_model_name'],
                                               state['_view_module'],
                                               state['_view_module_version'],
                                               state['_view_name'])
        widget = widget_class(comm=comm)
        if 'buffer_paths' in data:
            _put_buffers(state, data['buffer_paths'], msg['buffers'])
        widget.set_state(state)

    @staticmethod
    def get_manager_state(drop_defaults=False, widgets=None):
        """Returns the full state for a widget manager for embedding

        :param drop_defaults: when True, it will not include default value
        :param widgets: list with widgets to include in the state (or all widgets when None)
        :return:
        """
        state = {}
        if widgets is None:
            widgets = Widget.widgets.values()
        for widget in widgets:
            state[widget.model_id] = widget._get_embed_state(drop_defaults=drop_defaults)
        return {'version_major': 2, 'version_minor': 0, 'state': state}

    def _get_embed_state(self, drop_defaults=False):
        state = {
            'model_name': self._model_name,
            'model_module': self._model_module,
            'model_module_version': self._model_module_version
        }
        model_state, buffer_paths, buffers = _remove_buffers(self.get_state(drop_defaults=drop_defaults))
        state['state'] = model_state
        if len(buffers) > 0:
            state['buffers'] = [{'encoding': 'base64',
                                 'path': p,
                                 'data': standard_b64encode(d).decode('ascii')}
                                for p, d in zip(buffer_paths, buffers)]
        return state

    def get_view_spec(self):
        return dict(version_major=2, version_minor=0, model_id=self._model_id)

    #-------------------------------------------------------------------------
    # Traits
    #-------------------------------------------------------------------------
    _model_name = Unicode('WidgetModel',
        help="Name of the model.", read_only=True).tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/base',
        help="The namespace for the model.", read_only=True).tag(sync=True)
    _model_module_version = Unicode(__jupyter_widgets_base_version__,
        help="A semver requirement for namespace version containing the model.", read_only=True).tag(sync=True)
    _view_name = Unicode(None, allow_none=True,
        help="Name of the view.").tag(sync=True)
    _view_module = Unicode(None, allow_none=True,
        help="The namespace for the view.").tag(sync=True)
    _view_module_version = Unicode('',
        help="A semver requirement for the namespace version containing the view.").tag(sync=True)

    _view_count = Int(None, allow_none=True,
        help="EXPERIMENTAL: The number of views of the model displayed in the frontend. This attribute is experimental and may change or be removed in the future. None signifies that views will not be tracked. Set this to 0 to start tracking view creation/deletion.").tag(sync=True)
    comm = Instance('ipykernel.comm.Comm', allow_none=True)

    keys = List(help="The traits which are synced.")

    @default('keys')
    def _default_keys(self):
        return [name for name in self.traits(sync=True)]

    _property_lock = Dict()
    _holding_sync = False
    _states_to_send = Set()
    _display_callbacks = Instance(CallbackDispatcher, ())
    _msg_callbacks = Instance(CallbackDispatcher, ())

    #-------------------------------------------------------------------------
    # (Con/de)structor
    #-------------------------------------------------------------------------
    def __init__(self, **kwargs):
        """Public constructor"""
        self._model_id = kwargs.pop('model_id', None)
        super(Widget, self).__init__(**kwargs)

        Widget._call_widget_constructed(self)
        self.open()

    def __del__(self):
        """Object disposal"""
        self.close()

    #-------------------------------------------------------------------------
    # Properties
    #-------------------------------------------------------------------------

    def open(self):
        """Open a comm to the frontend if one isn't already open."""
        if self.comm is None:
            state, buffer_paths, buffers = _remove_buffers(self.get_state())

            args = dict(target_name='jupyter.widget',
                        data={'state': state, 'buffer_paths': buffer_paths},
                        buffers=buffers,
                        metadata={'version': __protocol_version__}
                        )
            if self._model_id is not None:
                args['comm_id'] = self._model_id

            self.comm = Comm(**args)

    @observe('comm')
    def _comm_changed(self, change):
        """Called when the comm is changed."""
        if change['new'] is None:
            return
        self._model_id = self.model_id

        self.comm.on_msg(self._handle_msg)
        Widget.widgets[self.model_id] = self

    @property
    def model_id(self):
        """Gets the model id of this widget.

        If a Comm doesn't exist yet, a Comm will be created automagically."""
        return self.comm.comm_id

    #-------------------------------------------------------------------------
    # Methods
    #-------------------------------------------------------------------------

    def close(self):
        """Close method.

        Closes the underlying comm.
        When the comm is closed, all of the widget views are automatically
        removed from the front-end."""
        if self.comm is not None:
            Widget.widgets.pop(self.model_id, None)
            self.comm.close()
            self.comm = None
            self._ipython_display_ = None

    def send_state(self, key=None):
        """Sends the widget state, or a piece of it, to the front-end, if it exists.

        Parameters
        ----------
        key : unicode, or iterable (optional)
            A single property's name or iterable of property names to sync with the front-end.
        """
        state = self.get_state(key=key)
        if len(state) > 0:
            if self._property_lock:  # we need to keep this dict up to date with the front-end values
                for name, value in state.items():
                    if name in self._property_lock:
                        self._property_lock[name] = value
            state, buffer_paths, buffers = _remove_buffers(state)
            msg = {'method': 'update', 'state': state, 'buffer_paths': buffer_paths}
            self._send(msg, buffers=buffers)


    def get_state(self, key=None, drop_defaults=False):
        """Gets the widget state, or a piece of it.

        Parameters
        ----------
        key : unicode or iterable (optional)
            A single property's name or iterable of property names to get.

        Returns
        -------
        state : dict of states
        metadata : dict
            metadata for each field: {key: metadata}
        """
        if key is None:
            keys = self.keys
        elif isinstance(key, string_types):
            keys = [key]
        elif isinstance(key, Iterable):
            keys = key
        else:
            raise ValueError("key must be a string, an iterable of keys, or None")
        state = {}
        traits = self.traits()
        for k in keys:
            to_json = self.trait_metadata(k, 'to_json', self._trait_to_json)
            value = to_json(getattr(self, k), self)
            if not PY3 and isinstance(traits[k], Bytes) and isinstance(value, bytes):
                value = memoryview(value)
            if not drop_defaults or not self._compare(value, traits[k].default_value):
                state[k] = value
        return state

    def _is_numpy(self, x):
        return x.__class__.__name__ == 'ndarray' and x.__class__.__module__ == 'numpy'

    def _compare(self, a, b):
        if self._is_numpy(a) or self._is_numpy(b):
            import numpy as np
            return np.array_equal(a, b)
        else:
            return a == b

    def set_state(self, sync_data):
        """Called when a state is received from the front-end."""
        # The order of these context managers is important. Properties must
        # be locked when the hold_trait_notification context manager is
        # released and notifications are fired.
        with self._lock_property(**sync_data), self.hold_trait_notifications():
            for name in sync_data:
                if name in self.keys:
                    from_json = self.trait_metadata(name, 'from_json',
                                                    self._trait_from_json)
                    self.set_trait(name, from_json(sync_data[name], self))

    def send(self, content, buffers=None):
        """Sends a custom msg to the widget model in the front-end.

        Parameters
        ----------
        content : dict
            Content of the message to send.
        buffers : list of binary buffers
            Binary buffers to send with message
        """
        self._send({"method": "custom", "content": content}, buffers=buffers)

    def on_msg(self, callback, remove=False):
        """(Un)Register a custom msg receive callback.

        Parameters
        ----------
        callback: callable
            callback will be passed three arguments when a message arrives::

                callback(widget, content, buffers)

        remove: bool
            True if the callback should be unregistered."""
        self._msg_callbacks.register_callback(callback, remove=remove)

    def on_displayed(self, callback, remove=False):
        """(Un)Register a widget displayed callback.

        Parameters
        ----------
        callback: method handler
            Must have a signature of::

                callback(widget, **kwargs)

            kwargs from display are passed through without modification.
        remove: bool
            True if the callback should be unregistered."""
        self._display_callbacks.register_callback(callback, remove=remove)

    def add_traits(self, **traits):
        """Dynamically add trait attributes to the Widget."""
        super(Widget, self).add_traits(**traits)
        for name, trait in traits.items():
            if trait.get_metadata('sync'):
                self.keys.append(name)
                self.send_state(name)

    def notify_change(self, change):
        """Called when a property has changed."""
        # Send the state to the frontend before the user-registered callbacks
        # are called.
        name = change['name']
        if self.comm is not None and self.comm.kernel is not None:
            # Make sure this isn't information that the front-end just sent us.
            if name in self.keys and self._should_send_property(name, getattr(self, name)):
                # Send new state to front-end
                self.send_state(key=name)
        super(Widget, self).notify_change(change)

    def __repr__(self):
        return self._gen_repr_from_keys(self._repr_keys())

    #-------------------------------------------------------------------------
    # Support methods
    #-------------------------------------------------------------------------

    @contextmanager
    def _lock_property(self, **properties):
        """Lock a property-value pair.

        The value should be the JSON state of the property.

        NOTE: This, in addition to the single lock for all state changes, is
        flawed.  In the future we may want to look into buffering state changes
        back to the front-end."""
        self._property_lock = properties
        try:
            yield
        finally:
            self._property_lock = {}

    @contextmanager
    def hold_sync(self):
        """Hold syncing any state until the outermost context manager exits"""
        if self._holding_sync is True:
            yield
        else:
            try:
                self._holding_sync = True
                yield
            finally:
                self._holding_sync = False
                self.send_state(self._states_to_send)
                self._states_to_send.clear()

    def _should_send_property(self, key, value):
        """Check the property lock (property_lock)"""
        to_json = self.trait_metadata(key, 'to_json', self._trait_to_json)
        if key in self._property_lock:
            # model_state, buffer_paths, buffers
            split_value = _remove_buffers({ key: to_json(value, self)})
            split_lock = _remove_buffers({ key: self._property_lock[key]})
            # A roundtrip conversion through json in the comparison takes care of
            # idiosyncracies of how python data structures map to json, for example
            # tuples get converted to lists.
            if (jsonloads(jsondumps(split_value[0])) == split_lock[0]
                and split_value[1] == split_lock[1]
                and _buffer_list_equal(split_value[2], split_lock[2])):
                return False
        if self._holding_sync:
            self._states_to_send.add(key)
            return False
        else:
            return True

    # Event handlers
    @_show_traceback
    def _handle_msg(self, msg):
        """Called when a msg is received from the front-end"""
        data = msg['content']['data']
        method = data['method']

        if method == 'update':
            if 'state' in data:
                state = data['state']
                if 'buffer_paths' in data:
                    _put_buffers(state, data['buffer_paths'], msg['buffers'])
                self.set_state(state)

        # Handle a state request.
        elif method == 'request_state':
            self.send_state()

        # Handle a custom msg from the front-end.
        elif method == 'custom':
            if 'content' in data:
                self._handle_custom_msg(data['content'], msg['buffers'])

        # Catch remainder.
        else:
            self.log.error('Unknown front-end to back-end widget msg with method "%s"' % method)

    def _handle_custom_msg(self, content, buffers):
        """Called when a custom msg is received."""
        self._msg_callbacks(self, content, buffers)

    def _handle_displayed(self, **kwargs):
        """Called when a view has been displayed for this widget instance"""
        self._display_callbacks(self, **kwargs)

    @staticmethod
    def _trait_to_json(x, self):
        """Convert a trait value to json."""
        return x

    @staticmethod
    def _trait_from_json(x, self):
        """Convert json values to objects."""
        return x

    def _ipython_display_(self, **kwargs):
        """Called when `IPython.display.display` is called on the widget."""

        plaintext = repr(self)
        if len(plaintext) > 110:
            plaintext = plaintext[:110] + '…'
        data = {
            'text/plain': plaintext,
        }
        if self._view_name is not None:
            # The 'application/vnd.jupyter.widget-view+json' mimetype has not been registered yet.
            # See the registration process and naming convention at
            # http://tools.ietf.org/html/rfc6838
            # and the currently registered mimetypes at
            # http://www.iana.org/assignments/media-types/media-types.xhtml.
            data['application/vnd.jupyter.widget-view+json'] = {
                'version_major': 2,
                'version_minor': 0,
                'model_id': self._model_id
            }
        display(data, raw=True)

        if self._view_name is not None:
            self._handle_displayed(**kwargs)

    def _send(self, msg, buffers=None):
        """Sends a message to the model in the front-end."""
        if self.comm is not None and self.comm.kernel is not None:
            self.comm.send(data=msg, buffers=buffers)

    def _repr_keys(self):
        traits = self.traits()
        for key in sorted(self.keys):
            # Exclude traits that start with an underscore
            if key[0] == '_':
                continue
            # Exclude traits who are equal to their default value
            value = getattr(self, key)
            trait = traits[key]
            if self._compare(value, trait.default_value):
                continue
            elif (isinstance(trait, (Container, Dict)) and
                  trait.default_value == Undefined and
                  (value is None or len(value) == 0)):
                # Empty container, and dynamic default will be empty
                continue
            yield key

    def _gen_repr_from_keys(self, keys):
        class_name = self.__class__.__name__
        signature = ', '.join(
            '%s=%r' % (key, getattr(self, key))
            for key in keys
        )
        return '%s(%s)' % (class_name, signature)
