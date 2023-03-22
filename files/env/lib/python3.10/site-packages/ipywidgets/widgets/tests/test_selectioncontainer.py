# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase

from traitlets import TraitError

from ipywidgets.widgets import Accordion, HTML


class TestAccordion(TestCase):

    def setUp(self):
        self.children = [HTML('0'), HTML('1')]

    def test_selected_index_none(self):
        accordion = Accordion(self.children, selected_index=None)
        state = accordion.get_state()
        assert state['selected_index'] is None

    def test_selected_index(self):
        accordion = Accordion(self.children, selected_index=1)
        state = accordion.get_state()
        assert state['selected_index'] == 1

    def test_selected_index_out_of_bounds(self):
        with self.assertRaises(TraitError):
            Accordion(self.children, selected_index=-1)
