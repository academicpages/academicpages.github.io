"""Tests for Latex exporter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os.path
import re
import textwrap
from tempfile import TemporaryDirectory

from jinja2 import DictLoader
from nbformat import v4, write
from traitlets.config import Config

from ...tests.utils import onlyif_cmds_exist
from ..latex import LatexExporter
from .base import ExportersTestsBase

current_dir = os.path.dirname(__file__)


class TestLatexExporter(ExportersTestsBase):
    """Contains test functions for latex.py"""

    exporter_class = LatexExporter
    should_include_raw = ["latex"]

    def test_constructor(self):
        """
        Can a LatexExporter be constructed?
        """
        LatexExporter()

    @onlyif_cmds_exist("pandoc")
    def test_export(self):
        """
        Can a LatexExporter export something?
        """
        (output, resources) = LatexExporter().from_filename(self._get_notebook())
        assert len(output) > 0

    @onlyif_cmds_exist("pandoc")
    def test_export_book(self):
        """
        Can a LatexExporter export using 'report' template?
        """
        (output, resources) = LatexExporter(template_file="report").from_filename(
            self._get_notebook()
        )
        assert len(output) > 0

    @onlyif_cmds_exist("pandoc")
    def test_very_long_cells(self):
        """
        Torture test that long cells do not cause issues
        """
        lorem_ipsum_text = textwrap.dedent(
            """\
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
          dignissim, ipsum non facilisis tempus, dui felis tincidunt metus,
          nec pulvinar neque odio eget risus. Nulla nisi lectus, cursus
          suscipit interdum at, ultrices sit amet orci. Mauris facilisis
          imperdiet elit, vitae scelerisque ipsum dignissim non. Integer
          consequat malesuada neque sit amet pulvinar. Curabitur pretium
          ut turpis eget aliquet. Maecenas sagittis lacus sed lectus
          volutpat, eu adipiscing purus pulvinar. Maecenas consequat
          luctus urna, eget cursus quam mollis a. Aliquam vitae ornare
          erat, non hendrerit urna. Sed eu diam nec massa egestas pharetra
          at nec tellus. Fusce feugiat lacus quis urna sollicitudin volutpat.
          Quisque at sapien non nibh feugiat tempus ac ultricies purus.
           """
        )
        lorem_ipsum_text = lorem_ipsum_text.replace("\n", " ") + "\n\n"
        large_lorem_ipsum_text = "".join([lorem_ipsum_text] * 3000)

        notebook_name = "lorem_ipsum_long.ipynb"
        nb = v4.new_notebook(cells=[v4.new_markdown_cell(source=large_lorem_ipsum_text)])

        with TemporaryDirectory() as td:
            nbfile = os.path.join(td, notebook_name)
            with open(nbfile, "w") as f:
                write(nb, f, 4)

            (output, resources) = LatexExporter().from_filename(nbfile)
            assert len(output) > 0

    @onlyif_cmds_exist("pandoc")
    def test_prompt_number_color(self):
        """
        Does LatexExporter properly format input and output prompts in color?
        """
        (output, resources) = LatexExporter().from_filename(
            self._get_notebook(nb_name="prompt_numbers.ipynb")
        )

        in_regex = r"\\prompt\{In\}\{incolor\}\{(\d+|\s*)\}"
        out_regex = r"\\prompt\{Out\}\{outcolor\}\{(\d+|\s*)\}"

        ins = ["2", "10", " ", " ", "0"]
        outs = ["10"]

        assert re.findall(in_regex, output) == ins
        assert re.findall(out_regex, output) == outs

    @onlyif_cmds_exist("pandoc")
    def test_prompt_number_color_ipython(self):
        """
        Does LatexExporter properly format input and output prompts in color?

        Uses an in memory latex template to load style_ipython as the cell style.
        """
        my_loader_tplx = DictLoader(
            {
                "my_template": r"""
            ((* extends 'style_ipython.tex.j2' *))

            ((* block docclass *))
            \documentclass[11pt]{article}
            ((* endblock docclass *))
            """
            }
        )

        class MyExporter(LatexExporter):
            template_file = "my_template"

        (output, resources) = MyExporter(extra_loaders=[my_loader_tplx]).from_filename(
            self._get_notebook(nb_name="prompt_numbers.ipynb")
        )

        in_regex = r"In \[\{\\color\{incolor\}(.*)\}\]:"
        out_regex = r"Out\[\{\\color\{outcolor\}(.*)\}\]:"

        ins = ["2", "10", " ", " ", "0"]
        outs = ["10"]

        assert re.findall(in_regex, output) == ins
        assert re.findall(out_regex, output) == outs

    @onlyif_cmds_exist("pandoc")
    def test_no_prompt_yes_input(self):
        no_prompt = {
            "TemplateExporter": {
                "exclude_input_prompt": True,
                "exclude_output_prompt": True,
            }
        }
        c_no_prompt = Config(no_prompt)

        exporter = LatexExporter(config=c_no_prompt)
        (output, resources) = exporter.from_filename(
            self._get_notebook(nb_name="prompt_numbers.ipynb")
        )
        assert "shape" in output
        assert "evs" in output

    @onlyif_cmds_exist("pandoc", "inkscape")
    def test_svg(self):
        """
        Can a LatexExporter export when it recieves raw binary strings form svg?
        """
        filename = os.path.join(current_dir, "files", "svg.ipynb")
        (output, resources) = LatexExporter().from_filename(filename)
        assert len(output) > 0

    def test_in_memory_template_tplx(self):
        # Loads in an in memory latex template (.tplx) using jinja2.DictLoader
        # creates a class that uses this template with the template_file argument
        # converts an empty notebook using this mechanism
        my_loader_tplx = DictLoader({"my_template": "{%- extends 'index' -%}"})

        class MyExporter(LatexExporter):
            template_file = "my_template"

        exporter = MyExporter(extra_loaders=[my_loader_tplx])
        nb = v4.new_notebook()
        out, resources = exporter.from_notebook_node(nb)

    def test_custom_filter_highlight_code(self):
        # Overwriting filters takes place at: Exporter.from_notebook_node
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        def custom_highlight_code(source, language="python", metadata=None, strip_verbatim=False):
            return source + " ADDED_TEXT"

        filters = {"highlight_code": custom_highlight_code}
        (output, resources) = LatexExporter(filters=filters).from_notebook_node(nb)
        self.assertTrue("ADDED_TEXT" in output)
