# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ipykernel.comm import Comm
from ipywidgets import Widget

class DummyComm(Comm):
    comm_id = 'a-b-c-d'
    kernel = 'Truthy'

    def __init__(self, *args, **kwargs):
        super(DummyComm, self).__init__(*args, **kwargs)
        self.messages = []

    def open(self, *args, **kwargs):
        pass

    def send(self, *args, **kwargs):
        self.messages.append((args, kwargs))

    def close(self, *args, **kwargs):
        pass

_widget_attrs = {}
undefined = object()

def setup_test_comm():
    _widget_attrs['_comm_default'] = getattr(Widget, '_comm_default', undefined)
    Widget._comm_default = lambda self: DummyComm()
    _widget_attrs['_ipython_display_'] = Widget._ipython_display_
    def raise_not_implemented(*args, **kwargs):
        raise NotImplementedError()
    Widget._ipython_display_ = raise_not_implemented

def teardown_test_comm():
    for attr, value in _widget_attrs.items():
        if value is undefined:
            delattr(Widget, attr)
        else:
            setattr(Widget, attr, value)
    _widget_attrs.clear()

def setup():
    setup_test_comm()

def teardown():
    teardown_test_comm()
