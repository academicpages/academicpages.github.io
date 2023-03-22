# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import inspect
import warnings
from unittest import TestCase

from traitlets import TraitError

from ipywidgets import Dropdown, SelectionSlider, Select


class TestDropdown(TestCase):

    def test_construction(self):
        Dropdown()

    def test_deprecation_warning_mapping_options(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            # Clearing the internal __warningregistry__ seems to be required for
            # Python 2 (but not for Python 3)
            module = inspect.getmodule(Dropdown)
            getattr(module, '__warningregistry__', {}).clear()

            Dropdown(options={'One': 1, 'Two': 2, 'Three': 3})
            assert len(w) > 0
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "Support for mapping types has been deprecated" in str(w[-1].message)


class TestSelectionSlider(TestCase):

    def test_construction(self):
        SelectionSlider(options=['a', 'b', 'c'])

    def test_index_trigger(self):
        slider = SelectionSlider(options=['a', 'b', 'c'])
        observations = []
        def f(change):
            observations.append(change.new)
        slider.observe(f, 'index')
        assert slider.index == 0
        slider.options = [4, 5, 6]
        assert slider.index == 0
        assert slider.value == 4
        assert slider.label == '4'
        assert observations == [0]

class TestSelection(TestCase):

    def test_construction(self):
        select = Select(options=['a', 'b', 'c'])

    def test_index_trigger(self):
        select = Select(options=[1, 2, 3])
        observations = []
        def f(change):
            observations.append(change.new)
        select.observe(f, 'index')
        assert select.index == 0
        select.options = [4, 5, 6]
        assert select.index == 0
        assert select.value == 4
        assert select.label == '4'
        assert observations == [0]

    def test_duplicate(self):
        select = Select(options=['first', 1, 'dup', 'dup'])
        observations = []
        def f(change):
            observations.append(change.new)
        select.observe(f, 'index')
        select.index = 3
        assert select.index == 3
        assert select.value == 'dup'
        assert select.label == 'dup'
        assert observations == [3]
        select.index = 2
        assert select.index == 2
        assert select.value == 'dup'
        assert select.label == 'dup'
        assert observations == [3, 2]
        select.index = 0
        assert select.index == 0
        assert select.value == 'first'
        assert select.label == 'first'
        assert observations == [3, 2, 0]

        # picks the first matching value
        select.value = 'dup'
        assert select.index == 2
        assert select.value == 'dup'
        assert select.label == 'dup'
        assert observations == [3, 2, 0, 2]
