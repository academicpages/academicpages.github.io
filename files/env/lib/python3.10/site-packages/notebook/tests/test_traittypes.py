import pytest
from traitlets import HasTraits, TraitError
from traitlets.utils.importstring import import_item

from notebook.traittypes import (
    InstanceFromClasses,
    TypeFromClasses
)
from notebook.services.contents.largefilemanager import LargeFileManager


class DummyClass:
    """Dummy class for testing Instance"""


class DummyInt(int):
    """Dummy class for testing types."""


class Thing(HasTraits):

    a = InstanceFromClasses(
        default_value=2,
        klasses=[
            int,
            str,
            DummyClass,
        ]
    )

    b = TypeFromClasses(
        default_value=None,
        allow_none=True,
        klasses=[
            DummyClass,
            int,
            'notebook.services.contents.manager.ContentsManager'
        ]
    )


class TestInstanceFromClasses:

    @pytest.mark.parametrize(
        'value',
        [1, 'test', DummyClass()]
    )
    def test_good_values(self, value):
        thing = Thing(a=value)
        assert thing.a == value

    @pytest.mark.parametrize(
        'value',
        [2.4, object()]
    )
    def test_bad_values(self, value):
        with pytest.raises(TraitError) as e:
            thing = Thing(a=value)


class TestTypeFromClasses:

    @pytest.mark.parametrize(
        'value',
        [DummyClass, DummyInt, LargeFileManager,
            'notebook.services.contents.manager.ContentsManager']
    )
    def test_good_values(self, value):
        thing = Thing(b=value)
        if isinstance(value, str):
            value = import_item(value)
        assert thing.b == value

    @pytest.mark.parametrize(
        'value',
        [float, object]
    )
    def test_bad_values(self, value):
        with pytest.raises(TraitError) as e:
            thing = Thing(b=value)
