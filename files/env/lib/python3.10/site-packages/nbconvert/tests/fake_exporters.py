"""
Module that define a custom exporter just to test the ability to invoke
nbconvert with full qualified name
"""

from traitlets import default

from nbconvert.exporters.html import HTMLExporter


class MyExporter(HTMLExporter):
    """
    My custom exporter
    """

    @default("file_extension")
    def _file_extension_default(self):
        """
        The new file extension is `.test_ext`
        """
        return ".test_ext"

    @default("template_extension")
    def _template_extension_default(self):
        return ".html.j2"
