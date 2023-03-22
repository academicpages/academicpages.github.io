# Copyright(c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""FileUpload class.

Represents a file upload button.
"""

from traitlets import (
    observe, default, Unicode, Dict, List, Int, Bool, Bytes, CaselessStrEnum
)

from .widget_description import DescriptionWidget
from .valuewidget import ValueWidget
from .widget_core import CoreWidget
from .widget_button import ButtonStyle
from .widget import register, widget_serialization
from .trait_types import bytes_serialization, InstanceDict

def content_from_json(value, widget):
    """
    deserialize file content
    """
    from_json = bytes_serialization['from_json']
    output = [from_json(e, None) for e in value]
    return output


@register
class FileUpload(DescriptionWidget, ValueWidget, CoreWidget):
    """
    Upload file(s) from browser to Python kernel as bytes
    """
    _model_name = Unicode('FileUploadModel').tag(sync=True)
    _view_name = Unicode('FileUploadView').tag(sync=True)
    _counter = Int().tag(sync=True)

    accept = Unicode(help='File types to accept, empty string for all').tag(sync=True)
    multiple = Bool(help='If True, allow for multiple files upload').tag(sync=True)
    disabled = Bool(help='Enable or disable button').tag(sync=True)
    icon = Unicode('upload', help="Font-awesome icon name, without the 'fa-' prefix.").tag(sync=True)
    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)
    style = InstanceDict(ButtonStyle).tag(sync=True, **widget_serialization)
    metadata = List(Dict(), help='List of file metadata').tag(sync=True)
    data = List(Bytes(), help='List of file content (bytes)').tag(
        sync=True, from_json=content_from_json
    )
    error = Unicode(help='Error message').tag(sync=True)
    value = Dict(read_only=True)

    @observe('_counter')
    def on_incr_counter(self, change):
        """
        counter increment triggers the update of trait value
        """
        res = {}
        msg = 'Error: length of metadata and data must be equal'
        assert len(self.metadata) == len(self.data), msg
        for metadata, content in zip(self.metadata, self.data):
            name = metadata['name']
            res[name] = {'metadata': metadata, 'content': content}
        self.set_trait('value', res)

    @default('description')
    def _default_description(self):
        return 'Upload'
