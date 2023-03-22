# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""Contains the DOMWidget class"""

from traitlets import Unicode
from .widget import Widget, widget_serialization, register
from .trait_types import InstanceDict
from .widget_style import Style
from .widget_core import CoreWidget
from .domwidget import DOMWidget

@register
class DescriptionStyle(Style, CoreWidget, Widget):
    """Description style widget."""
    _model_name = Unicode('DescriptionStyleModel').tag(sync=True)
    description_width = Unicode(help="Width of the description to the side of the control.").tag(sync=True)


class DescriptionWidget(DOMWidget, CoreWidget):
    """Widget that has a description label to the side."""
    _model_name = Unicode('DescriptionModel').tag(sync=True)
    description = Unicode('', help="Description of the control.").tag(sync=True)
    description_tooltip = Unicode(None, allow_none=True, help="Tooltip for the description (defaults to description).").tag(sync=True)
    style = InstanceDict(DescriptionStyle, help="Styling customizations").tag(sync=True, **widget_serialization)

    def _repr_keys(self):
        for key in super(DescriptionWidget, self)._repr_keys():
            # Exclude style if it had the default value
            if key == 'style':
                value = getattr(self, key)
                if repr(value) == '%s()' % value.__class__.__name__:
                    continue
            yield key
