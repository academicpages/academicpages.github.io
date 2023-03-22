# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""Contains the Layout class"""

from traitlets import Unicode, Instance, CaselessStrEnum, validate
from .widget import Widget, register
from .._version import __jupyter_widgets_base_version__

CSS_PROPERTIES=['inherit', 'initial', 'unset']

@register
class Layout(Widget):
    """Layout specification

    Defines a layout that can be expressed using CSS.  Supports a subset of
    https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

    When a property is also accessible via a shorthand property, we only
    expose the shorthand.

    For example:
    - ``flex-grow``, ``flex-shrink`` and ``flex-basis`` are bound to ``flex``.
    - ``flex-wrap`` and ``flex-direction`` are bound to ``flex-flow``.
    - ``margin-[top/bottom/left/right]`` values are bound to ``margin``, etc.
    """

    _view_name = Unicode('LayoutView').tag(sync=True)
    _view_module = Unicode('@jupyter-widgets/base').tag(sync=True)
    _view_module_version = Unicode(__jupyter_widgets_base_version__).tag(sync=True)
    _model_name = Unicode('LayoutModel').tag(sync=True)

    # Keys
    align_content = CaselessStrEnum(['flex-start', 'flex-end', 'center', 'space-between',
        'space-around', 'space-evenly', 'stretch'] + CSS_PROPERTIES, allow_none=True, help="The align-content CSS attribute.").tag(sync=True)
    align_items = CaselessStrEnum(['flex-start', 'flex-end', 'center',
        'baseline', 'stretch'] + CSS_PROPERTIES, allow_none=True, help="The align-items CSS attribute.").tag(sync=True)
    align_self = CaselessStrEnum(['auto', 'flex-start', 'flex-end',
        'center', 'baseline', 'stretch'] + CSS_PROPERTIES, allow_none=True, help="The align-self CSS attribute.").tag(sync=True)
    bottom = Unicode(None, allow_none=True, help="The bottom CSS attribute.").tag(sync=True)
    border = Unicode(None, allow_none=True, help="The border CSS attribute.").tag(sync=True)
    display = Unicode(None, allow_none=True, help="The display CSS attribute.").tag(sync=True)
    flex = Unicode(None, allow_none=True, help="The flex CSS attribute.").tag(sync=True)
    flex_flow = Unicode(None, allow_none=True, help="The flex-flow CSS attribute.").tag(sync=True)
    height = Unicode(None, allow_none=True, help="The height CSS attribute.").tag(sync=True)
    justify_content = CaselessStrEnum(['flex-start', 'flex-end', 'center',
        'space-between', 'space-around'] + CSS_PROPERTIES, allow_none=True, help="The justify-content CSS attribute.").tag(sync=True)
    justify_items = CaselessStrEnum(['flex-start', 'flex-end', 'center'] + CSS_PROPERTIES,
        allow_none=True, help="The justify-items CSS attribute.").tag(sync=True)
    left = Unicode(None, allow_none=True, help="The left CSS attribute.").tag(sync=True)
    margin = Unicode(None, allow_none=True, help="The margin CSS attribute.").tag(sync=True)
    max_height = Unicode(None, allow_none=True, help="The max-height CSS attribute.").tag(sync=True)
    max_width = Unicode(None, allow_none=True, help="The max-width CSS attribute.").tag(sync=True)
    min_height = Unicode(None, allow_none=True, help="The min-height CSS attribute.").tag(sync=True)
    min_width = Unicode(None, allow_none=True, help="The min-width CSS attribute.").tag(sync=True)
    overflow = Unicode(None, allow_none=True, help="The overflow CSS attribute.").tag(sync=True)
    overflow_x = CaselessStrEnum(['visible', 'hidden', 'scroll', 'auto'] + CSS_PROPERTIES, allow_none=True, help="The overflow-x CSS attribute (deprecated).").tag(sync=True)
    overflow_y = CaselessStrEnum(['visible', 'hidden', 'scroll', 'auto'] + CSS_PROPERTIES, allow_none=True, help="The overflow-y CSS attribute (deprecated).").tag(sync=True)
    order = Unicode(None, allow_none=True, help="The order CSS attribute.").tag(sync=True)
    padding = Unicode(None, allow_none=True, help="The padding CSS attribute.").tag(sync=True)
    right = Unicode(None, allow_none=True, help="The right CSS attribute.").tag(sync=True)
    top = Unicode(None, allow_none=True, help="The top CSS attribute.").tag(sync=True)
    visibility = CaselessStrEnum(['visible', 'hidden']+CSS_PROPERTIES, allow_none=True, help="The visibility CSS attribute.").tag(sync=True)
    width = Unicode(None, allow_none=True, help="The width CSS attribute.").tag(sync=True)

    object_fit = CaselessStrEnum(['contain', 'cover', 'fill', 'scale-down', 'none'], allow_none=True, help="The object-fit CSS attribute.").tag(sync=True)
    object_position = Unicode(None, allow_none=True, help="The object-position CSS attribute.").tag(sync=True)

    grid_auto_columns = Unicode(None, allow_none=True, help="The grid-auto-columns CSS attribute.").tag(sync=True)
    grid_auto_flow = CaselessStrEnum(['column','row','row dense','column dense']+ CSS_PROPERTIES, allow_none=True, help="The grid-auto-flow CSS attribute.").tag(sync=True)
    grid_auto_rows = Unicode(None, allow_none=True, help="The grid-auto-rows CSS attribute.").tag(sync=True)
    grid_gap = Unicode(None, allow_none=True, help="The grid-gap CSS attribute.").tag(sync=True)
    grid_template_rows = Unicode(None, allow_none=True, help="The grid-template-rows CSS attribute.").tag(sync=True)
    grid_template_columns = Unicode(None, allow_none=True, help="The grid-template-columns CSS attribute.").tag(sync=True)
    grid_template_areas = Unicode(None, allow_none=True, help="The grid-template-areas CSS attribute.").tag(sync=True)
    grid_row = Unicode(None, allow_none=True, help="The grid-row CSS attribute.").tag(sync=True)
    grid_column = Unicode(None, allow_none=True, help="The grid-column CSS attribute.").tag(sync=True)
    grid_area = Unicode(None, allow_none=True, help="The grid-area CSS attribute.").tag(sync=True)

    @validate('overflow_x', 'overflow_y')
    def _validate_overflows(self, proposal):
        if proposal.value is not None:
            import warnings
            warnings.warn("Layout properties overflow_x and overflow_y have been deprecated and will be dropped in a future release. Please use the overflow shorthand property instead", DeprecationWarning)
        return proposal.value


class LayoutTraitType(Instance):

    klass = Layout

    def validate(self, obj, value):
        if isinstance(value, dict):
            return super(LayoutTraitType, self).validate(obj, self.klass(**value))
        else:
            return super(LayoutTraitType, self).validate(obj, value)
