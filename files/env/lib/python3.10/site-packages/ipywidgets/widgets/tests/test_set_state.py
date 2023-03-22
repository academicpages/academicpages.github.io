# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ipython_genutils.py3compat import PY3

import pytest
try:
    from unittest import mock
except ImportError:
    import mock


from traitlets import Bool, Tuple, List, Instance, CFloat, CInt, Float, Int, TraitError, observe

from .utils import setup, teardown

from ..widget import Widget

#
# First some widgets to test on:
#

# A widget with simple traits (list + tuple to ensure both are handled)
class SimpleWidget(Widget):
    a = Bool().tag(sync=True)
    b = Tuple(Bool(), Bool(), Bool(), default_value=(False, False, False)).tag(sync=True)
    c = List(Bool()).tag(sync=True)


# A widget with various kinds of number traits
class NumberWidget(Widget):
    f = Float().tag(sync=True)
    cf = CFloat().tag(sync=True)
    i = Int().tag(sync=True)
    ci = CInt().tag(sync=True)



# A widget where the data might be changed on reception:
def transform_fromjson(data, widget):
    # Switch the two last elements when setting from json, if the first element is True
    # and always set first element to False
    if not data[0]:
        return data
    return [False] + data[1:-2] + [data[-1], data[-2]]

class TransformerWidget(Widget):
    d = List(Bool()).tag(sync=True, from_json=transform_fromjson)



# A widget that has a buffer:
class DataInstance():
    def __init__(self, data=None):
        self.data = data

def mview_serializer(instance, widget):
    return { 'data': memoryview(instance.data) if instance.data else None }

def bytes_serializer(instance, widget):
    return { 'data': bytearray(memoryview(instance.data).tobytes()) if instance.data else None }

def deserializer(json_data, widget):
    return DataInstance( memoryview(json_data['data']).tobytes() if json_data else None )

class DataWidget(SimpleWidget):
    d = Instance(DataInstance).tag(sync=True, to_json=mview_serializer, from_json=deserializer)

# A widget that has a buffer that might be changed on reception:
def truncate_deserializer(json_data, widget):
    return DataInstance( json_data['data'][:20].tobytes() if json_data else None )

class TruncateDataWidget(SimpleWidget):
    d = Instance(DataInstance).tag(sync=True, to_json=bytes_serializer, from_json=truncate_deserializer)


#
# Actual tests:
#

def test_set_state_simple():
    w = SimpleWidget()
    w.set_state(dict(
        a=True,
        b=[True, False, True],
        c=[False, True, False],
    ))

    assert w.comm.messages == []


def test_set_state_transformer():
    w = TransformerWidget()
    w.set_state(dict(
        d=[True, False, True]
    ))
    # Since the deserialize step changes the state, this should send an update
    assert w.comm.messages == [((), dict(
        buffers=[],
        data=dict(
            buffer_paths=[],
            method='update',
            state=dict(d=[False, True, False])
        )))]


def test_set_state_data():
    w = DataWidget()
    data = memoryview(b'x'*30)
    w.set_state(dict(
        a=True,
        d={'data': data},
    ))
    assert w.comm.messages == []


def test_set_state_data_truncate():
    w = TruncateDataWidget()
    data = memoryview(b'x'*30)
    w.set_state(dict(
        a=True,
        d={'data': data},
    ))
    # Get message for checking
    assert len(w.comm.messages) == 1   # ensure we didn't get more than expected
    msg = w.comm.messages[0]
    # Assert that the data update (truncation) sends an update
    buffers = msg[1].pop('buffers')
    assert msg == ((), dict(
        data=dict(
            buffer_paths=[['d', 'data']],
            method='update',
            state=dict(d={})
        )))

    # Sanity:
    assert len(buffers) == 1
    assert buffers[0] == data[:20].tobytes()


def test_set_state_numbers_int():
    # JS does not differentiate between float/int.
    # Instead, it formats exact floats as ints in JSON (1.0 -> '1').

    w = NumberWidget()
    # Set everything with ints
    w.set_state(dict(
        f = 1,
        cf = 2,
        i = 3,
        ci = 4,
    ))
    # Ensure no update message gets produced
    assert len(w.comm.messages) == 0


def test_set_state_numbers_float():
    w = NumberWidget()
    # Set floats to int-like floats
    w.set_state(dict(
        f = 1.0,
        cf = 2.0,
        ci = 4.0
    ))
    # Ensure no update message gets produced
    assert len(w.comm.messages) == 0


def test_set_state_float_to_float():
    w = NumberWidget()
    # Set floats to float
    w.set_state(dict(
        f = 1.2,
        cf = 2.6,
    ))
    # Ensure no update message gets produced
    assert len(w.comm.messages) == 0


def test_set_state_cint_to_float():
    w = NumberWidget()

    # Set CInt to float
    w.set_state(dict(
        ci = 5.6
    ))
    # Ensure an update message gets produced
    assert len(w.comm.messages) == 1
    msg = w.comm.messages[0]
    data = msg[1]['data']
    assert data['method'] == 'update'
    assert data['state'] == {'ci': 5}


# This test is disabled, meaning ipywidgets REQUIRES
# any JSON received to format int-like numbers as ints
def _x_test_set_state_int_to_int_like():
    # Note: Setting i to an int-like float will produce an
    # error, so if JSON producer were to always create
    # float formatted numbers, this would fail!

    w = NumberWidget()
    # Set floats to int-like floats
    w.set_state(dict(
        i = 3.0
    ))
    # Ensure no update message gets produced
    assert len(w.comm.messages) == 0


def test_set_state_int_to_float():
    w = NumberWidget()

    # Set Int to float
    with pytest.raises(TraitError):
        w.set_state(dict(
            i = 3.5
        ))

def test_property_lock():
    # when this widget's value is set to 42, it sets itself to 2, and then back to 42 again (and then stops)
    class AnnoyingWidget(Widget):
        value = Float().tag(sync=True)
        stop = Bool(False)

        @observe('value')
        def _propagate_value(self, change):
            print('_propagate_value', change.new)
            if self.stop:
                return
            if change.new == 42:
                self.value = 2
            if change.new == 2:
                self.stop = True
                self.value = 42

    widget = AnnoyingWidget(value=1)
    assert widget.value == 1

    widget._send = mock.MagicMock()
    # this mimics a value coming from the front end
    widget.set_state({'value': 42})
    assert widget.value == 42

    # we expect first the {'value': 2.0} state to be send, followed by the {'value': 42.0} state
    msg = {'method': 'update', 'state': {'value': 2.0}, 'buffer_paths': []}
    call2 = mock.call(msg, buffers=[])

    msg = {'method': 'update', 'state': {'value': 42.0}, 'buffer_paths': []}
    call42 = mock.call(msg, buffers=[])

    calls = [call2, call42]
    widget._send.assert_has_calls(calls)
