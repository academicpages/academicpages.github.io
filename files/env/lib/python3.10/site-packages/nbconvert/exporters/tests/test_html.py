"""Tests for HTMLExporter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import re

from nbformat import v4
from traitlets.config import Config

from ..html import HTMLExporter
from .base import ExportersTestsBase


class TestHTMLExporter(ExportersTestsBase):
    """Tests for HTMLExporter"""

    exporter_class = HTMLExporter
    should_include_raw = ["html"]

    def test_constructor(self):
        """
        Can a HTMLExporter be constructed?
        """
        HTMLExporter()

    def test_export(self):
        """
        Can a HTMLExporter export something?
        """
        (output, resources) = HTMLExporter().from_filename(self._get_notebook())
        assert len(output) > 0

    def test_export_classic(self):
        """
        Can a HTMLExporter export using the 'classic' template?
        """
        (output, resources) = HTMLExporter(template_name="classic").from_filename(
            self._get_notebook()
        )
        assert len(output) > 0

    def test_export_notebook(self):
        """
        Can a HTMLExporter export using the 'lab' template?
        """
        (output, resources) = HTMLExporter(template_name="lab").from_filename(self._get_notebook())
        assert len(output) > 0

    def test_prompt_number(self):
        """
        Does HTMLExporter properly format input and output prompts?
        """
        no_prompt_conf = Config(
            {
                "TemplateExporter": {
                    "exclude_input_prompt": True,
                    "exclude_output_prompt": True,
                }
            }
        )
        exporter = HTMLExporter(config=no_prompt_conf, template_name="lab")
        (output, resources) = exporter.from_filename(
            self._get_notebook(nb_name="prompt_numbers.ipynb")
        )
        in_regex = r"In&nbsp;\[(.*)\]:"
        out_regex = r"Out\[(.*)\]:"

        assert not re.findall(in_regex, output)
        assert not re.findall(out_regex, output)

    def test_png_metadata(self):
        """
        Does HTMLExporter with the 'classic' template treat pngs with width/height metadata correctly?
        """
        (output, resources) = HTMLExporter(template_name="classic").from_filename(
            self._get_notebook(nb_name="pngmetadata.ipynb")
        )
        check_for_png = re.compile(r'<img src="[^"]*?"([^>]*?)>')
        result = check_for_png.search(output)
        attr_string = result.group(1)
        assert "width" in attr_string
        assert "height" in attr_string

    def test_javascript_output(self):
        nb = v4.new_notebook(
            cells=[
                v4.new_code_cell(
                    outputs=[
                        v4.new_output(
                            output_type="display_data",
                            data={"application/javascript": "javascript_output();"},
                        )
                    ]
                )
            ]
        )
        (output, resources) = HTMLExporter(template_name="classic").from_notebook_node(nb)
        self.assertIn("javascript_output", output)

    def test_attachments(self):
        (output, resources) = HTMLExporter(template_name="classic").from_file(
            self._get_notebook(nb_name="attachment.ipynb")
        )
        check_for_png = re.compile(r'<img src="[^"]*?"([^>]*?)>')
        result = check_for_png.search(output)
        self.assertTrue(result.group(0).strip().startswith('<img src="data:image/png;base64,iVBOR'))
        self.assertTrue(result.group(1).strip().startswith('alt="image.png"'))

        check_for_data = re.compile(r'<img src="(?P<url>[^"]*?)"')
        results = check_for_data.findall(output)
        assert results[0] != results[1], "attachments only need to be unique within a cell"
        assert "image/svg" in results[1], "second image should use svg"

    def test_custom_filter_highlight_code(self):
        # Overwriting filters takes place at: Exporter.from_notebook_node
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        def custom_highlight_code(source, language="python", metadata=None):
            return source + " ADDED_TEXT"

        filters = {"highlight_code": custom_highlight_code}
        (output, resources) = HTMLExporter(
            template_name="classic", filters=filters
        ).from_notebook_node(nb)
        self.assertTrue("ADDED_TEXT" in output)

    def test_basic_name(self):
        """
        Can a HTMLExporter export using the 'basic' template?
        """
        (output, resources) = HTMLExporter(template_name="basic").from_filename(
            self._get_notebook()
        )
        assert len(output) > 0

    def test_javascript_injection(self):
        for template in ["lab", "classic", "reveal"]:
            (output, resources) = HTMLExporter(template_name=template).from_filename(
                self._get_notebook("notebook_inject.ipynb")
            )

            # Check injection in the metadata.title of the Notebook
            assert "<script>alert('title')</script>" not in output

            # Check injection in the metadata.widgets of the Notebook
            assert "</script><script>alert('widgets')" not in output

            # Check injection in the cell.metadata.tags of the Notebook
            assert "<script>alert('cell_tag')</script>" not in output

            # Check injection in the cell.source of the Notebook
            assert "<script>alert('raw cell')</script>" not in output

            # Check injection in svg output
            assert "<script>alert('image/svg+xml output')</script>" not in output
            assert "<script>alert('svg_filename')</script>" not in output

            # Check injection in image filenames
            assert "<script>alert('png filenames')</script>" not in output
            assert "<script>alert('jpg filenames')</script>" not in output

            # Check injection in image data
            assert "<script>alert('image/png output')</script>" not in output
            assert "<script>alert('image/jpeg output')</script>" not in output

            # Check injection in image width/height
            assert "<script>alert('output.metadata.width png injection')</script>" not in output
            assert "<script>alert('output.metadata.height png injection')</script>" not in output

            # Check injection in widget view
            assert (
                "<script>alert('output.data.application/vnd.jupyter.widget-view+json injection')"
                not in output
            )

        # By design, text/html, text/markdown, application/javascript and markdown cells should allow
        # for JavaScript code execution
        for template in ["lab", "classic", "reveal"]:
            (output, resources) = HTMLExporter(template_name=template).from_filename(
                self._get_notebook("notebook_inject.ipynb")
            )

            assert "<script>alert('markdown cell')</script>" in output
            assert "<script>alert('text/markdown output')</script>" in output
            assert "<script>alert('text/html output')</script>" in output
            assert "alert('application/javascript output')" in output

        # But it's an opt-out
        for template in ["lab", "classic", "reveal"]:
            (output, resources) = HTMLExporter(
                template_name=template, sanitize_html=True
            ).from_filename(self._get_notebook("notebook_inject.ipynb"))

            assert "<script>alert('markdown cell')</script>" not in output
            assert "<script>alert('text/markdown output')</script>" not in output
            assert "<script>alert('text/html output')</script>" not in output
            assert "alert('application/javascript output')" not in output
