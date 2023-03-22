"""Test NbConvertApp"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os
from tempfile import TemporaryDirectory

import nbformat
import pytest
from traitlets.tests.utils import check_help_all_output

from nbconvert.exporters import HTMLExporter

from ..postprocessors import PostProcessorBase
from ..tests.utils import onlyif_cmds_exist
from .base import TestsBase

# -----------------------------------------------------------------------------
# Classes and functions
# -----------------------------------------------------------------------------


class DummyPost(PostProcessorBase):
    def postprocess(self, filename):
        print("Dummy:%s" % filename)


class TestNbConvertApp(TestsBase):
    """Collection of NbConvertApp tests"""

    def test_notebook_help(self):
        """Will help show if no notebooks are specified?"""
        with self.create_temp_cwd():
            out, err = self.nbconvert("--log-level 0", ignore_return_code=True)
            self.assertIn("--help-all", out)

    def test_help_output(self):
        """ipython nbconvert --help-all works"""
        check_help_all_output("nbconvert")

    def test_glob(self):
        """
        Do search patterns work for notebook names?
        """
        with self.create_temp_cwd(["notebook*.ipynb"]):
            self.nbconvert("--to python *.ipynb --log-level 0")
            assert os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_glob_subdir(self):
        """
        Do search patterns work for subdirectory notebook names?
        """
        with self.create_temp_cwd():
            self.copy_files_to(["notebook*.ipynb"], "subdir/")
            self.nbconvert("--to python --log-level 0 " + os.path.join("subdir", "*.ipynb"))
            assert os.path.isfile(os.path.join("subdir", "notebook1.py"))
            assert os.path.isfile(os.path.join("subdir", "notebook2.py"))

    def test_build_dir(self):
        """build_directory affects export location"""
        with self.create_temp_cwd():
            self.copy_files_to(["notebook*.ipynb"], "subdir/")
            self.nbconvert(
                "--to python --log-level 0 --output-dir . " + os.path.join("subdir", "*.ipynb")
            )
            assert os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_convert_full_qualified_name(self):
        """
        Test that nbconvert can convert file using a full qualified name for a
        package, import and use it.
        """
        with self.create_temp_cwd():
            self.copy_files_to(["notebook*.ipynb"], "subdir")
            self.nbconvert(
                "--to nbconvert.tests.fake_exporters.MyExporter --log-level 0 "
                + os.path.join("subdir", "*.ipynb")
            )
            assert os.path.isfile(os.path.join("subdir", "notebook1.test_ext"))
            assert os.path.isfile(os.path.join("subdir", "notebook2.test_ext"))

    def test_explicit(self):
        """
        Do explicit notebook names work?
        """
        with self.create_temp_cwd(["notebook*.ipynb"]):
            self.nbconvert("--log-level 0 --to python notebook2")
            assert not os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_clear_output(self):
        """
        Can we clear outputs?
        """
        with self.create_temp_cwd(["notebook*.ipynb"]) as td:
            self.nbconvert("--clear-output notebook1")
            assert os.path.isfile("notebook1.ipynb")
            with open("notebook1.ipynb", encoding="utf8") as f:
                nb = nbformat.read(f, 4)
                for cell in nb.cells:
                    # Skip markdown cells
                    if "outputs" in cell:
                        assert cell.outputs == []

    def test_absolute_template_file(self):
        """--template-file '/path/to/template.tpl'"""
        with self.create_temp_cwd(["notebook*.ipynb"]), TemporaryDirectory() as td:
            template = os.path.join(td, "mytemplate.tpl")
            test_output = "success!"
            with open(template, "w") as f:
                f.write(test_output)
            self.nbconvert("--log-level 0 notebook2 --to html --template-file %s" % template)
            assert os.path.isfile("notebook2.html")
            with open("notebook2.html", encoding="utf8") as f:
                text = f.read()
            assert text == test_output

    def test_relative_template_file(self):
        """Test --template-file 'relative/path.tpl'"""
        with self.create_temp_cwd(["notebook*.ipynb"]):
            os.mkdir("relative")
            template = os.path.join("relative", "path.tpl")
            test_output = "success!"
            with open(template, "w") as f:
                f.write(test_output)
            self.nbconvert("--log-level 0 notebook2 --to html --template-file %s" % template)
            assert os.path.isfile("notebook2.html")
            with open("notebook2.html", encoding="utf8") as f:
                text = f.read()
            assert text == test_output

    @onlyif_cmds_exist("pandoc", "xelatex")
    def test_filename_spaces(self):
        """
        Generate PDFs with graphics if notebooks have spaces in the name?
        """
        with self.create_temp_cwd(["notebook2.ipynb"]):
            os.rename("notebook2.ipynb", "notebook with spaces.ipynb")
            self.nbconvert(
                "--log-level 0 --to pdf"
                ' "notebook with spaces"'
                " --PDFExporter.latex_count=1"
                " --PDFExporter.verbose=True"
            )
            assert os.path.isfile("notebook with spaces.pdf")

    @pytest.mark.network
    def test_webpdf_with_chromium(self):
        """
        Generate PDFs if chromium allowed to be downloaded?
        """
        with self.create_temp_cwd(["notebook2.ipynb"]):
            self.nbconvert('--to webpdf --allow-chromium-download "notebook2"')
            assert os.path.isfile("notebook2.pdf")

    @onlyif_cmds_exist("pandoc", "xelatex")
    def test_pdf(self):
        """
        Check to see if pdfs compile, even if strikethroughs are included.
        """
        with self.create_temp_cwd(["notebook2.ipynb"]):
            self.nbconvert(
                "--log-level 0 --to pdf"
                ' "notebook2"'
                " --PDFExporter.latex_count=1"
                " --PDFExporter.verbose=True"
            )
            assert os.path.isfile("notebook2.pdf")

    def test_post_processor(self):
        """Do post processors work?"""
        with self.create_temp_cwd(["notebook1.ipynb"]):
            out, err = self.nbconvert(
                "--log-level 0 --to python notebook1 --post nbconvert.tests.test_nbconvertapp.DummyPost"
            )
            self.assertIn("Dummy:notebook1.py", out)

    @onlyif_cmds_exist("pandoc")
    def test_spurious_cr(self):
        """Check for extra CR characters"""
        with self.create_temp_cwd(["notebook2.ipynb"]):
            self.nbconvert("--log-level 0 --to latex notebook2")
            assert os.path.isfile("notebook2.tex")
            with open("notebook2.tex") as f:
                tex = f.read()
            self.nbconvert("--log-level 0 --to html notebook2")
            assert os.path.isfile("notebook2.html")
            with open("notebook2.html", encoding="utf8") as f:
                html = f.read()
        self.assertEqual(tex.count("\r"), tex.count("\r\n"))
        self.assertEqual(html.count("\r"), html.count("\r\n"))

    @onlyif_cmds_exist("pandoc")
    def test_png_base64_html_ok(self):
        """Is embedded png data well formed in HTML?"""
        with self.create_temp_cwd(["notebook2.ipynb"]):
            self.nbconvert("--log-level 0 --to HTML notebook2.ipynb --template lab")
            assert os.path.isfile("notebook2.html")
            with open("notebook2.html", encoding="utf8") as f:
                assert "data:image/png;base64,b'" not in f.read()

    @onlyif_cmds_exist("pandoc")
    def test_template(self):
        """
        Do export templates work?
        """
        with self.create_temp_cwd(["notebook2.ipynb"]):
            self.nbconvert("--log-level 0 --to slides notebook2.ipynb")
            assert os.path.isfile("notebook2.slides.html")
            with open("notebook2.slides.html", encoding="utf8") as f:
                assert "/reveal.css" in f.read()

    def test_output_ext(self):
        """test --output=outputfile[.ext]"""
        with self.create_temp_cwd(["notebook1.ipynb"]):
            self.nbconvert("--log-level 0 --to python notebook1.ipynb --output nb.py")
            assert os.path.exists("nb.py")

            self.nbconvert("--log-level 0 --to python notebook1.ipynb --output nb2")
            assert os.path.exists("nb2.py")

    def test_glob_explicit(self):
        """
        Can a search pattern be used along with matching explicit notebook names?
        """
        with self.create_temp_cwd(["notebook*.ipynb"]):
            self.nbconvert("--log-level 0 --to python *.ipynb notebook1.ipynb notebook2.ipynb")
            assert os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_explicit_glob(self):
        """
        Can explicit notebook names be used and then a matching search pattern?
        """
        with self.create_temp_cwd(["notebook*.ipynb"]):
            self.nbconvert("--log-level 0 --to=python notebook1.ipynb notebook2.ipynb *.ipynb")
            assert os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_default_config(self):
        """
        Does the default config work?
        """
        with self.create_temp_cwd(["notebook*.ipynb", "jupyter_nbconvert_config.py"]):
            self.nbconvert("--log-level 0")
            assert os.path.isfile("notebook1.py")
            assert not os.path.isfile("notebook2.py")

    def test_override_config(self):
        """
        Can the default config be overridden?
        """
        with self.create_temp_cwd(
            ["notebook*.ipynb", "jupyter_nbconvert_config.py", "override.py"]
        ):
            self.nbconvert('--log-level 0 --config="override.py"')
            assert not os.path.isfile("notebook1.py")
            assert os.path.isfile("notebook2.py")

    def test_accents_in_filename(self):
        """
        Can notebook names include accents?
        """
        with self.create_temp_cwd():
            self.create_empty_notebook("nb1_análisis.ipynb")
            self.nbconvert("--log-level 0 --to Python nb1_*")
            assert os.path.isfile("nb1_análisis.py")

    @onlyif_cmds_exist("xelatex", "pandoc")
    def test_filename_accent_pdf(self):
        """
        Generate PDFs if notebooks have an accent in their name?
        """
        with self.create_temp_cwd():
            self.create_empty_notebook("nb1_análisis.ipynb")
            self.nbconvert(
                '--log-level 0 --to pdf "nb1_*"'
                " --PDFExporter.latex_count=1"
                " --PDFExporter.verbose=True"
            )
            assert os.path.isfile("nb1_análisis.pdf")

    @pytest.mark.skipif(os.name == "nt", reason="CLI parsing does not work the same on Windows")
    def test_cwd_plugin(self):
        """
        Verify that an extension in the cwd can be imported.
        """
        with self.create_temp_cwd(["hello.py"]):
            self.create_empty_notebook("empty.ipynb")
            assert os.path.isfile("hello.py")
            self.nbconvert("empty --to html --NbConvertApp.writer_class='hello.HelloWriter'")
            assert os.path.isfile("hello.txt")

    def test_output_suffix(self):
        """
        Verify that the output suffix is applied
        """
        with self.create_temp_cwd():
            self.create_empty_notebook("empty.ipynb")
            self.nbconvert("empty.ipynb --to notebook")
            assert os.path.isfile("empty.nbconvert.ipynb")

    def test_different_build_dir(self):
        """
        Verify that the output suffix is not applied
        """
        with self.create_temp_cwd():
            self.create_empty_notebook("empty.ipynb")
            os.mkdir("output")
            self.nbconvert("empty.ipynb --to notebook --FilesWriter.build_directory=output")
            assert os.path.isfile("output/empty.ipynb")

    def test_inplace(self):
        """
        Verify that the notebook is converted in place
        """
        with self.create_temp_cwd():
            self.create_empty_notebook("empty.ipynb")
            self.nbconvert("empty.ipynb --inplace")
            assert os.path.isfile("empty.ipynb")
            assert not os.path.isfile("empty.nbconvert.ipynb")
            assert not os.path.isfile("empty.html")

    def test_no_prompt(self):
        """
        Verify that the html has no prompts when given --no-prompt.
        """
        with self.create_temp_cwd(["notebook1.ipynb"]):
            self.nbconvert("notebook1.ipynb --log-level 0 --no-prompt --to html")
            assert os.path.isfile("notebook1.html")
            with open("notebook1.html", encoding="utf8") as f:
                text = f.read()
                assert "In&nbsp;[" not in text
                assert "Out[6]" not in text
            self.nbconvert("notebook1.ipynb --log-level 0 --to html")
            assert os.path.isfile("notebook1.html")
            with open("notebook1.html", encoding="utf8") as f:
                text2 = f.read()
                assert "In&nbsp;[" in text2
                assert "Out[6]" in text2

    def test_cell_tag_output(self):
        """
        Verify that the html has tags in cell attributes if they exist.
        """
        with self.create_temp_cwd(["notebook_tags.ipynb"]):
            self.nbconvert("notebook_tags.ipynb --log-level 0 --to html")
            assert os.path.isfile("notebook_tags.html")
            with open("notebook_tags.html", encoding="utf8") as f:
                text = f.read()
                assert "celltag_mycelltag celltag_mysecondcelltag" in text
                assert "celltag_mymarkdowncelltag" in text

    def test_no_input(self):
        """
        Verify that the html has no input when given --no-input.
        """
        with self.create_temp_cwd(["notebook1.ipynb"]):
            self.nbconvert("notebook1.ipynb --log-level 0 --no-input --to html")
            assert os.path.isfile("notebook1.html")
            with open("notebook1.html", encoding="utf8") as f:
                text = f.read()
                assert "In&nbsp;[" not in text
                assert "Out[6]" not in text
                assert (
                    '<span class="n">x</span>'
                    '<span class="p">,</span>'
                    '<span class="n">y</span>'
                    '<span class="p">,</span>'
                    '<span class="n">z</span> '
                    '<span class="o">=</span> '
                    '<span class="n">symbols</span>'
                    '<span class="p">(</span>'
                    "<span class=\"s1\">'x y z'</span>"
                    '<span class="p">)</span>'
                ) not in text
            self.nbconvert("notebook1.ipynb --log-level 0 --to html")
            assert os.path.isfile("notebook1.html")
            with open("notebook1.html", encoding="utf8") as f:
                text2 = f.read()
                assert "In&nbsp;[" in text2
                assert "Out[6]" in text2
                assert (
                    '<span class="n">x</span>'
                    '<span class="p">,</span>'
                    '<span class="n">y</span>'
                    '<span class="p">,</span>'
                    '<span class="n">z</span> '
                    '<span class="o">=</span> '
                    '<span class="n">symbols</span>'
                    '<span class="p">(</span>'
                    "<span class=\"s1\">'x y z'</span>"
                    '<span class="p">)</span>'
                ) in text2

    def test_allow_errors(self):
        """
        Verify that conversion is aborted with '--execute' if an error is
        encountered, but that conversion continues if '--allow-errors' is
        used in addition.
        """
        with self.create_temp_cwd(["notebook3*.ipynb"]):
            # Convert notebook containing a cell that raises an error,
            # both without and with cell execution enabled.
            output1, _ = self.nbconvert(
                "--to markdown --stdout notebook3*.ipynb"
            )  # no cell execution
            output2, _ = self.nbconvert(
                "--to markdown --allow-errors --stdout notebook3*.ipynb"
            )  # no cell execution; --allow-errors should have no effect
            output3, _ = self.nbconvert(
                "--execute --allow-errors --to markdown --stdout notebook3*.ipynb"
            )  # with cell execution; errors are allowed

            # Un-executed outputs should not contain either
            # of the two numbers computed in the notebook.
            assert "23" not in output1
            assert "42" not in output1
            assert "23" not in output2
            assert "42" not in output2

            # Executed output should contain both numbers.
            assert "23" in output3
            assert "42" in output3

            # Executing the notebook should raise an exception if --allow-errors is not specified
            with pytest.raises(OSError):
                self.nbconvert("--execute --to markdown --stdout notebook3*.ipynb")

    def test_errors_print_traceback(self):
        """
        Verify that the stderr output contains the traceback of the cell execution exception.
        """
        with self.create_temp_cwd(["notebook3_with_errors.ipynb"]):
            _, error_output = self.nbconvert(
                "--execute --to markdown --stdout notebook3_with_errors.ipynb",
                ignore_return_code=True,
            )
            assert 'print("Some text before the error")' in error_output
            assert 'raise RuntimeError("This is a deliberate exception")' in error_output
            assert "RuntimeError: This is a deliberate exception" in error_output

    def test_fenced_code_blocks_markdown(self):
        """
        Verify that input cells use fenced code blocks with the language
        name in nb.metadata.kernelspec.language, if that exists
        """
        with self.create_temp_cwd(["notebook1*.ipynb"]):
            # this notebook doesn't have nb.metadata.kernelspec, so it should
            # just do a fenced code block, with no language
            output1, _ = self.nbconvert("--to markdown --stdout notebook1.ipynb")
            assert "```python" not in output1  # shouldn't have language
            assert "```" in output1  # but should have fenced blocks

        with self.create_temp_cwd(["notebook_jl*.ipynb"]):

            output2, _ = self.nbconvert("--to markdown --stdout notebook_jl.ipynb")
            assert "```julia" in output2  # shouldn't have language
            assert "```" in output2  # but should also plain ``` to close cell

    def test_convert_from_stdin_to_stdout(self):
        """
        Verify that conversion can be done via stdin to stdout
        """
        with self.create_temp_cwd(["notebook1.ipynb"]):
            with open("notebook1.ipynb") as f:
                notebook = f.read().encode()
                output1, _ = self.nbconvert("--to markdown --stdin --stdout", stdin=notebook)
            assert "```python" not in output1  # shouldn't have language
            assert "```" in output1  # but should have fenced blocks

    def test_convert_from_stdin(self):
        """
        Verify that conversion can be done via stdin.
        """
        with self.create_temp_cwd(["notebook1.ipynb"]):
            with open("notebook1.ipynb") as f:
                notebook = f.read().encode()
                self.nbconvert("--to markdown --stdin", stdin=notebook)
            assert os.path.isfile("notebook.md")  # default name for stdin input
            with open("notebook.md", encoding="utf8") as f:
                output1 = f.read()
                assert "```python" not in output1  # shouldn't have language
                assert "```" in output1  # but should have fenced blocks

    @onlyif_cmds_exist("pandoc", "xelatex")
    def test_linked_images(self):
        """
        Generate PDFs with an image linked in a markdown cell
        """
        with self.create_temp_cwd(["latex-linked-image.ipynb", "testimage.png"]):
            self.nbconvert("--to pdf latex-linked-image.ipynb")
            assert os.path.isfile("latex-linked-image.pdf")

    @onlyif_cmds_exist("pandoc")
    def test_embedded_jpeg(self):
        """
        Verify that latex conversion succeeds
        with a notebook with an embedded .jpeg
        """
        with self.create_temp_cwd(["notebook4_jpeg.ipynb", "containerized_deployments.jpeg"]):
            self.nbconvert("--to latex notebook4_jpeg.ipynb")
            assert os.path.isfile("notebook4_jpeg.tex")

    @onlyif_cmds_exist("pandoc")
    def test_markdown_display_priority(self):
        """
        Check to see if markdown conversion embeds PNGs,
        even if an (unsupported) PDF is present.
        """
        with self.create_temp_cwd(["markdown_display_priority.ipynb"]):
            self.nbconvert('--log-level 0 --to markdown "markdown_display_priority.ipynb"')
            assert os.path.isfile("markdown_display_priority.md")
            with open("markdown_display_priority.md", encoding="utf8") as f:
                markdown_output = f.read()
                assert (
                    "markdown_display_priority_files/markdown_display_priority_0_1.png"
                ) in markdown_output

    @onlyif_cmds_exist("pandoc")
    def test_write_figures_to_custom_path(self):
        """
        Check if figure files are copied to configured path.
        """

        def fig_exists(path):
            return len(os.listdir(path)) > 0

        # check absolute path
        with self.create_temp_cwd(["notebook4_jpeg.ipynb", "containerized_deployments.jpeg"]):
            output_dir = TemporaryDirectory()
            path = os.path.join(output_dir.name, "files")
            self.nbconvert(
                "--log-level 0 notebook4_jpeg.ipynb --to rst "
                "--NbConvertApp.output_files_dir={}".format(path)
            )
            assert fig_exists(path)
            output_dir.cleanup()

        # check relative path
        with self.create_temp_cwd(["notebook4_jpeg.ipynb", "containerized_deployments.jpeg"]):
            self.nbconvert(
                "--log-level 0 notebook4_jpeg.ipynb --to rst "
                "--NbConvertApp.output_files_dir=output"
            )
            assert fig_exists("output")

        # check default path with notebook name
        with self.create_temp_cwd(["notebook4_jpeg.ipynb", "containerized_deployments.jpeg"]):
            self.nbconvert("--log-level 0 notebook4_jpeg.ipynb --to rst")
            assert fig_exists("notebook4_jpeg_files")

    def test_widgets_from_nbconvert(self):
        """Check jupyter widgets URL"""

        with self.create_temp_cwd(["Widget_List.ipynb"]):
            self.nbconvert("Widget_List.ipynb --log-level 0 --to html")
            assert os.path.isfile("Widget_List.html")
            with open("Widget_List.html", encoding="utf8") as f:
                text = f.read()
                assert (
                    "var widgetRendererSrc = 'https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js';"
                    in text
                )

    def test_widgets_from_htmlexporter(self):
        """Check jupyter widgets URL"""
        with self.create_temp_cwd(["Widget_List.ipynb"]) as tmpdir:
            with open(os.path.join(tmpdir, "Widget_List.ipynb")) as f:
                nb = nbformat.read(f, 4)

            output, _ = HTMLExporter().from_notebook_node(nb)

            assert (
                "var widgetRendererSrc = 'https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js';"
                in output
            )

    def test_not_embedding_images_htmlexporter(self):
        """Check that the HTMLExporter does not embed images by default"""

        with self.create_temp_cwd(
            ["notebook5_embed_images.ipynb", "containerized_deployments.jpeg"]
        ):
            self.nbconvert("notebook5_embed_images --log-level 0 --to html")
            assert os.path.isfile("notebook5_embed_images.html")
            with open("notebook5_embed_images.html", encoding="utf8") as f:
                text = f.read()
                assert "./containerized_deployments.jpeg" in text
                assert "src='./containerized_deployments.jpeg'" in text
                assert text.count("data:image/jpeg;base64") == 0

    def test_embedding_images_htmlexporter(self):
        """Check that the HTMLExporter embeds images if needed"""

        with self.create_temp_cwd(
            ["notebook5_embed_images.ipynb", "containerized_deployments.jpeg"]
        ):
            self.nbconvert("notebook5_embed_images --log-level 0 --to html --embed-images")
            assert os.path.isfile("notebook5_embed_images.html")
            with open("notebook5_embed_images.html", encoding="utf8") as f:
                text = f.read()
                assert "./containerized_deployments.jpeg" not in text
                assert "src='./containerized_deployments.jpeg'" not in text
                assert text.count("data:image/jpeg;base64") == 3

    def test_execute_widgets_from_nbconvert(self):
        """Check jupyter widgets render"""
        notebookName = "Unexecuted_widget"
        with self.create_temp_cwd([f"{notebookName}.ipynb"]):
            self.nbconvert(f"{notebookName}.ipynb --execute --log-level 0 --to html")
            assert os.path.isfile(f"{notebookName}.html")
            with open(f"{notebookName}.html", encoding="utf8") as f:
                text = f.read()
                assert '<script type="application/vnd.jupyter.widget-view+json">' in text
                assert '<script type="application/vnd.jupyter.widget-state+json">' in text

    def test_execute_multiple_notebooks(self):
        """Check jupyter widgets render in case of batch convert"""
        notebookName = "Unexecuted_widget"
        with self.create_temp_cwd([f"{notebookName}*.ipynb"]):
            self.nbconvert("*.ipynb --execute --log-level 0 --to html")

            for name in (notebookName, f"{notebookName}_2"):
                assert os.path.isfile(f"{name}.html")
                with open(f"{name}.html", encoding="utf8") as f:
                    text = f.read()
                    assert '<script type="application/vnd.jupyter.widget-view+json">' in text
                    assert '<script type="application/vnd.jupyter.widget-state+json">' in text
