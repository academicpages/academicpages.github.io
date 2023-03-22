"""LaTeX Exporter class"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.


from traitlets import default
from traitlets.config import Config

from nbconvert.filters.filter_links import resolve_references
from nbconvert.filters.highlight import Highlight2Latex

from .templateexporter import TemplateExporter


class LatexExporter(TemplateExporter):
    """
    Exports to a Latex template.  Inherit from this class if your template is
    LaTeX based and you need custom transformers/filters.
    If you don't need custom transformers/filters, just change the
    'template_file' config option.  Place your template in the special "/latex"
    subfolder of the "../templates" folder.
    """

    export_from_notebook = "LaTeX"

    @default("file_extension")
    def _file_extension_default(self):
        return ".tex"

    @default("template_name")
    def _template_name_default(self):
        return "latex"

    output_mimetype = "text/latex"

    def default_filters(self):
        yield from super().default_filters()
        yield ("resolve_references", resolve_references)

    @property
    def default_config(self):
        c = Config(
            {
                "NbConvertBase": {
                    "display_data_priority": [
                        "text/latex",
                        "application/pdf",
                        "image/png",
                        "image/jpeg",
                        "image/svg+xml",
                        "text/markdown",
                        "text/plain",
                    ]
                },
                "ExtractOutputPreprocessor": {"enabled": True},
                "SVG2PDFPreprocessor": {"enabled": True},
                "LatexPreprocessor": {"enabled": True},
                "SphinxPreprocessor": {"enabled": True},
                "HighlightMagicsPreprocessor": {"enabled": True},
            }
        )
        c.merge(super().default_config)
        return c

    def from_notebook_node(self, nb, resources=None, **kw):
        langinfo = nb.metadata.get("language_info", {})
        lexer = langinfo.get("pygments_lexer", langinfo.get("name", None))
        highlight_code = self.filters.get(
            "highlight_code", Highlight2Latex(pygments_lexer=lexer, parent=self)
        )
        self.register_filter("highlight_code", highlight_code)

        return super().from_notebook_node(nb, resources, **kw)

    def _create_environment(self):
        environment = super()._create_environment()

        # Set special Jinja2 syntax that will not conflict with latex.
        environment.block_start_string = "((*"
        environment.block_end_string = "*))"
        environment.variable_start_string = "((("
        environment.variable_end_string = ")))"
        environment.comment_start_string = "((="
        environment.comment_end_string = "=))"

        return environment
