# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""Bool class.

Represents a boolean using a widget.
"""

from .widget_description import DescriptionWidget
from .widget_core import CoreWidget
from .valuewidget import ValueWidget
from .widget import register
from traitlets import Unicode, Bool, CaselessStrEnum


class _Bool(DescriptionWidget, ValueWidget, CoreWidget):
    """A base class for creating widgets that represent booleans."""
    value = Bool(False, help="Bool value").tag(sync=True)
    disabled = Bool(False, help="Enable or disable user changes.").tag(sync=True)

    def __init__(self, value=None, **kwargs):
        if value is not None:
            kwargs['value'] = value
        super(_Bool, self).__init__(**kwargs)

    _model_name = Unicode('BoolModel').tag(sync=True)


@register
class Checkbox(_Bool):
    """Displays a boolean `value` in the form of a checkbox.

    Parameters
    ----------
    value : {True,False}
        value of the checkbox: True-checked, False-unchecked
    description : str
	    description displayed next to the checkbox
    indent : {True,False}
        indent the control to align with other controls with a description. The style.description_width attribute controls this width for consistence with other controls.
    """
    _view_name = Unicode('CheckboxView').tag(sync=True)
    _model_name = Unicode('CheckboxModel').tag(sync=True)
    indent = Bool(True, help="Indent the control to align with other controls with a description.").tag(sync=True)


@register
class ToggleButton(_Bool):
    """Displays a boolean `value` in the form of a toggle button.

    Parameters
    ----------
    value : {True,False}
        value of the toggle button: True-pressed, False-unpressed
    description : str
	      description displayed next to the button
    tooltip: str
        tooltip caption of the toggle button
    icon: str
        font-awesome icon name
    """
    _view_name = Unicode('ToggleButtonView').tag(sync=True)
    _model_name = Unicode('ToggleButtonModel').tag(sync=True)

    tooltip = Unicode(help="Tooltip caption of the toggle button.").tag(sync=True)
    icon = Unicode('', help= "Font-awesome icon.").tag(sync=True)

    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)


@register
class Valid(_Bool):
    """Displays a boolean `value` in the form of a green check (True / valid)
    or a red cross (False / invalid).

    Parameters
    ----------
    value: {True,False}
        value of the Valid widget
    """
    readout = Unicode('Invalid', help="Message displayed when the value is False").tag(sync=True)
    _view_name = Unicode('ValidView').tag(sync=True)
    _model_name = Unicode('ValidModel').tag(sync=True)
