# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ..widget_string import Combobox


def test_combobox_creation_blank():
    w = Combobox()
    assert w.value == ''
    assert w.options == ()
    assert w.ensure_option == False


def test_combobox_creation_kwargs():
    w = Combobox(
        value='Chocolate',
        options=[
            "Chocolate",
            "Coconut",
            "Mint",
            "Strawberry",
            "Vanilla",
        ],
        ensure_option=True
    )
    assert w.value == 'Chocolate'
    assert w.options == (
            "Chocolate",
            "Coconut",
            "Mint",
            "Strawberry",
            "Vanilla",
        )
    assert w.ensure_option == True
