"""
Module with tests for templateexporter.py
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
import os
from concurrent.futures import ProcessPoolExecutor
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest
from jinja2 import TemplateNotFound
from nbformat import v4
from traitlets import default
from traitlets.config import Config

from ...utils import _contextlib_chdir
from ..html import HTMLExporter
from ..markdown import MarkdownExporter
from ..rst import RSTExporter
from ..templateexporter import TemplateExporter
from .base import ExportersTestsBase
from .cheese import CheesePreprocessor

raw_template = """{%- extends 'index.rst.j2' -%}
{%- block in_prompt -%}
blah
{%- endblock in_prompt -%}
"""


class SampleExporter(TemplateExporter):
    """
    Exports a Python code file.
    """

    @default("file_extension")
    def _file_extension_default(self):
        return ".py"

    @default("template_name")
    def _template_name_default(self):
        return "python"


class TestExporter(ExportersTestsBase):
    """Contains test functions for exporter.py"""

    def test_constructor(self):
        """
        Can a TemplateExporter be constructed?
        """
        TemplateExporter()

    def test_export(self):
        """
        Can a TemplateExporter export something?
        """
        exporter = self._make_exporter()
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert len(output) > 0

    def test_extract_outputs(self):
        """
        If the ExtractOutputPreprocessor is enabled, are outputs extracted?
        """
        config = Config({"ExtractOutputPreprocessor": {"enabled": True}})
        exporter = self._make_exporter(config=config)
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert resources is not None
        assert isinstance(resources["outputs"], dict)
        assert len(resources["outputs"]) > 0

    def test_preprocessor_class(self):
        """
        Can a preprocessor be added to the preprocessors list by class type?
        """
        config = Config({"Exporter": {"preprocessors": [CheesePreprocessor]}})
        exporter = self._make_exporter(config=config)
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert resources is not None
        assert resources["cheese"] == "real"

    def test_preprocessor_instance(self):
        """
        Can a preprocessor be added to the preprocessors list by instance?
        """
        config = Config({"Exporter": {"preprocessors": [CheesePreprocessor()]}})
        exporter = self._make_exporter(config=config)
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert resources is not None
        assert resources["cheese"] == "real"

    def test_preprocessor_dottedobjectname(self):
        """
        Can a preprocessor be added to the preprocessors list by dotted object name?
        """
        config = Config(
            {"Exporter": {"preprocessors": ["nbconvert.exporters.tests.cheese.CheesePreprocessor"]}}
        )
        exporter = self._make_exporter(config=config)
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert resources is not None
        assert resources["cheese"] == "real"

    def test_preprocessor_via_method(self):
        """
        Can a preprocessor be added via the Exporter convenience method?
        """
        exporter = self._make_exporter()
        exporter.register_preprocessor(CheesePreprocessor, enabled=True)
        (output, resources) = exporter.from_filename(self._get_notebook())
        assert resources is not None
        assert resources["cheese"] == "real"

    def test_pickle(self):
        """
        Can exporters be pickled & called across processes?
        """
        exporter = self._make_exporter()
        executor = ProcessPoolExecutor()
        (output, resources) = executor.submit(exporter.from_filename, self._get_notebook()).result()
        assert len(output) > 0

    def test_absolute_template_file(self):
        with TemporaryDirectory() as td:
            template = os.path.join(td, "abstemplate.ext.j2")
            test_output = "absolute!"
            with open(template, "w") as f:
                f.write(test_output)
            config = Config()
            config.TemplateExporter.template_file = template
            exporter = self._make_exporter(config=config)
            assert exporter.template.filename == template
            assert os.path.dirname(template) in exporter.template_paths

    def test_relative_template_file(self):
        with TemporaryDirectory() as td, _contextlib_chdir.chdir(td):
            with patch("os.getcwd", return_value=os.path.abspath(td)):
                template = os.path.join("relative", "relative_template.ext.j2")
                template_abs = os.path.abspath(os.path.join(td, template))
                os.mkdir(os.path.dirname(template_abs))
                test_output = "relative!"
                with open(template_abs, "w") as f:
                    f.write(test_output)
                config = Config()
                config.TemplateExporter.template_file = template
                exporter = self._make_exporter(config=config)
                assert os.path.abspath(exporter.template.filename) == template_abs
                assert os.path.dirname(template_abs) in [
                    os.path.abspath(d) for d in exporter.template_paths
                ]

    def test_absolute_template_file_compatibility(self):
        with TemporaryDirectory() as td:
            template = os.path.join(td, "abstemplate.tpl")
            test_output = "absolute!"
            with open(template, "w") as f:
                f.write(test_output)
            config = Config()
            config.TemplateExporter.template_file = template
            with pytest.warns(DeprecationWarning):
                exporter = self._make_exporter(config=config)
            assert exporter.template.filename == template
            assert os.path.dirname(template) in exporter.template_paths

    def test_relative_template_file_compatibility(self):
        with TemporaryDirectory() as td, _contextlib_chdir.chdir(td):
            with patch("os.getcwd", return_value=os.path.abspath(td)):
                template = os.path.join("relative", "relative_template.tpl")
                template_abs = os.path.abspath(os.path.join(td, template))
                os.mkdir(os.path.dirname(template_abs))
                test_output = "relative!"
                with open(template_abs, "w") as f:
                    f.write(test_output)
                config = Config()
                config.TemplateExporter.template_file = template
                with pytest.warns(DeprecationWarning):
                    exporter = self._make_exporter(config=config)
                assert os.path.abspath(exporter.template.filename) == template_abs
                assert os.path.dirname(template_abs) in [
                    os.path.abspath(d) for d in exporter.template_paths
                ]

    def test_absolute_template_name_tpl_compatibility(self):
        with TemporaryDirectory() as td:
            template = os.path.join(td, "abstemplate.tpl")
            test_output = "absolute!"
            with open(template, "w") as f:
                f.write(test_output)
            config = Config()
            # We're setting the template_name instead of the template_file
            config.TemplateExporter.template_name = template
            with pytest.warns(DeprecationWarning):
                exporter = self._make_exporter(config=config)
            assert exporter.template.filename == template
            assert os.path.dirname(template) in exporter.template_paths

    # Can't use @pytest.mark.parametrize without removing all self.assert calls in all tests... repeating some here
    def absolute_template_name_5x_compatibility_test(self, template, mimetype=None):
        config = Config()
        # We're setting the template_name instead of the template_file
        config.TemplateExporter.template_name = template
        with pytest.warns(DeprecationWarning):
            exporter = self._make_exporter(config=config)
        template_dir, template_file = os.path.split(exporter.template.filename)
        _, compat_dir = os.path.split(template_dir)
        assert compat_dir == "compatibility"
        assert template_file == template + ".tpl"
        assert template_dir in exporter.template_paths

    def test_absolute_template_name_5x_compatibility_full(self):
        self.absolute_template_name_5x_compatibility_test("full", "text/html")

    def test_absolute_template_name_5x_compatibility_display_priority(self):
        self.absolute_template_name_5x_compatibility_test("display_priority")

    # Can't use @pytest.mark.parametrize without removing all self.assert calls in all tests... repeating some here
    def relative_template_test(self, template):
        with TemporaryDirectory() as td, _contextlib_chdir.chdir(td):
            with patch("os.getcwd", return_value=os.path.abspath(td)):
                template_abs = os.path.abspath(os.path.join(td, template))
                dirname = os.path.dirname(template_abs)
                if not os.path.exists(dirname):
                    os.mkdir(dirname)
                test_output = "relative!"
                with open(template_abs, "w") as f:
                    f.write(test_output)
                config = Config()
                # We're setting the template_name instead of the template_file
                config.TemplateExporter.template_name = template
                with pytest.warns(DeprecationWarning):
                    exporter = self._make_exporter(config=config)
                assert os.path.abspath(exporter.template.filename) == template_abs
                assert os.path.dirname(template_abs) in [
                    os.path.abspath(d) for d in exporter.template_paths
                ]

    def test_relative_template_name_tpl_compatibility_local(self):
        self.relative_template_test("relative_template.tpl")

    def test_relative_template_name_tpl_compatibility_nested(self):
        self.relative_template_test(os.path.join("relative", "relative_template.tpl"))

    def test_relative_template_name_tpl_compatibility_dot(self):
        self.relative_template_test(os.path.join(".", "relative_template.tpl"))

    def test_relative_template_name_tpl_compatibility_dot_nested(self):
        self.relative_template_test(os.path.join(".", "relative", "relative_template.tpl"))

    def test_absolute_template_dir(self):
        with TemporaryDirectory() as td:
            template = "mytemplate"
            template_file = os.path.join(td, template, "index.py.j2")
            template_dir = os.path.dirname(template_file)
            os.mkdir(template_dir)
            test_output = "absolute!"
            with open(template_file, "w") as f:
                f.write(test_output)
            config = Config()
            config.TemplateExporter.template_name = template
            config.TemplateExporter.extra_template_basedirs = [td]
            exporter = self._make_exporter(config=config)
            assert exporter.template.filename == template_file
            assert exporter.template_name == template
            assert os.path.join(td, template) in exporter.template_paths

    def test_local_template_dir(self):
        with TemporaryDirectory() as td, _contextlib_chdir.chdir(td):
            with patch("os.getcwd", return_value=os.path.abspath(td)):
                template = "mytemplate"
                template_file = os.path.join(template, "index.py.j2")
                template_abs = os.path.abspath(os.path.join(td, template_file))
                template_conf = os.path.abspath(os.path.join(td, template, "conf.json"))
                os.mkdir(os.path.dirname(template_abs))
                test_output = "local!"
                with open(template_abs, "w") as f:
                    f.write(test_output)
                with open(template_conf, "w") as f:
                    # Mimic having a superset of accepted mimetypes
                    f.write(
                        json.dumps(
                            Config(
                                mimetypes={
                                    "text/x-python": True,
                                    "text/html": True,
                                }
                            )
                        )
                    )
                config = Config()
                config.TemplateExporter.template_name = template
                exporter = self._make_exporter(config=config)
                assert os.path.abspath(exporter.template.filename) == template_abs
                assert exporter.template_name == template
                assert os.path.join(td, template) in exporter.template_paths

    def test_local_template_file_extending_lab(self):
        template_file = os.path.join(self._get_files_path(), "lablike.html.j2")
        exporter = HTMLExporter(template_file=template_file, template_name="lab")
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))
        output, resources = exporter.from_notebook_node(nb)
        assert "UNIQUE" in output

    def test_raw_template_attr(self):
        """
        Verify that you can assign a in memory template string by overwriting
        `raw_template` as simple(non-traitlet) attribute
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        class AttrExporter(TemplateExporter):
            raw_template = raw_template

        exporter_attr = AttrExporter(template_name="rst")
        output_attr, _ = exporter_attr.from_notebook_node(nb)
        assert "blah" in output_attr

    def test_raw_template_init(self):
        """
        Test that template_file and raw_template traitlets play nicely together.
        - source assigns template_file default first, then raw_template
        - checks that the raw_template overrules template_file if set
        - checks that once raw_template is set to '', template_file returns
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        class AttrExporter(RSTExporter):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.raw_template = raw_template

        exporter_init = AttrExporter()
        output_init, _ = exporter_init.from_notebook_node(nb)
        assert "blah" in output_init
        exporter_init.raw_template = ""
        assert exporter_init.template_file == "index.rst.j2"
        output_init, _ = exporter_init.from_notebook_node(nb)
        assert "blah" not in output_init

    def test_raw_template_dynamic_attr(self):
        """
        Test that template_file and raw_template traitlets play nicely together.
        - source assigns template_file default first, then raw_template
        - checks that the raw_template overrules template_file if set
        - checks that once raw_template is set to '', template_file returns
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        class AttrDynamicExporter(TemplateExporter):
            @default("default_template_file")
            def _template_file_default(self):
                return "index.rst.j2"

            @default("raw_template")
            def _raw_template_default(self):
                return raw_template

        exporter_attr_dynamic = AttrDynamicExporter(template_name="rst")
        output_attr_dynamic, _ = exporter_attr_dynamic.from_notebook_node(nb)
        assert "blah" in output_attr_dynamic
        exporter_attr_dynamic.raw_template = ""
        assert exporter_attr_dynamic.template_file == "index.rst.j2"
        output_attr_dynamic, _ = exporter_attr_dynamic.from_notebook_node(nb)
        assert "blah" not in output_attr_dynamic

    def test_raw_template_dynamic_attr_reversed(self):
        """
        Test that template_file and raw_template traitlets play nicely together.
        - source assigns raw_template default first, then template_file
        - checks that the raw_template overrules template_file if set
        - checks that once raw_template is set to '', template_file returns
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        class AttrDynamicExporter(TemplateExporter):
            @default("raw_template")
            def _raw_template_default(self):
                return raw_template

            @default("default_template_file")
            def _template_file_default(self):
                return "index.rst.j2"

        exporter_attr_dynamic = AttrDynamicExporter(template_name="rst")
        output_attr_dynamic, _ = exporter_attr_dynamic.from_notebook_node(nb)
        assert "blah" in output_attr_dynamic
        exporter_attr_dynamic.raw_template = ""
        assert exporter_attr_dynamic.template_file == "index.rst.j2"
        output_attr_dynamic, _ = exporter_attr_dynamic.from_notebook_node(nb)
        assert "blah" not in output_attr_dynamic

    def test_raw_template_constructor(self):
        """
        Test `raw_template` as a keyword argument in the exporter constructor.
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))

        output_constructor, _ = TemplateExporter(
            template_name="rst", raw_template=raw_template
        ).from_notebook_node(nb)
        assert "blah" in output_constructor

    def test_raw_template_assignment(self):
        """
        Test `raw_template` assigned after the fact on non-custom Exporter.
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))
        exporter_assign = TemplateExporter(template_name="rst")
        exporter_assign.raw_template = raw_template
        output_assign, _ = exporter_assign.from_notebook_node(nb)
        assert "blah" in output_assign

    def test_raw_template_reassignment(self):
        """
        Test `raw_template` reassigned after the fact on non-custom Exporter.
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))
        exporter_reassign = TemplateExporter(template_name="rst")
        exporter_reassign.raw_template = raw_template
        output_reassign, _ = exporter_reassign.from_notebook_node(nb)
        assert "blah" in output_reassign
        exporter_reassign.raw_template = raw_template.replace("blah", "baz")
        output_reassign, _ = exporter_reassign.from_notebook_node(nb)
        assert "baz" in output_reassign

    def test_raw_template_deassignment(self):
        """
        Test `raw_template` does not overwrite template_file if deassigned after
        being assigned to a non-custom Exporter.
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))
        exporter_deassign = RSTExporter()
        exporter_deassign.raw_template = raw_template
        output_deassign, _ = exporter_deassign.from_notebook_node(nb)
        assert "blah" in output_deassign
        exporter_deassign.raw_template = ""
        assert exporter_deassign.template_file == "index.rst.j2"
        output_deassign, _ = exporter_deassign.from_notebook_node(nb)
        assert "blah" not in output_deassign

    def test_raw_template_dereassignment(self):
        """
        Test `raw_template` does not overwrite template_file if deassigned after
        being assigned to a non-custom Exporter.
        """
        nb = v4.new_notebook()
        nb.cells.append(v4.new_code_cell("some_text"))
        exporter_dereassign = RSTExporter()
        exporter_dereassign.raw_template = raw_template
        output_dereassign, _ = exporter_dereassign.from_notebook_node(nb)
        assert "blah" in output_dereassign
        exporter_dereassign.raw_template = raw_template.replace("blah", "baz")
        output_dereassign, _ = exporter_dereassign.from_notebook_node(nb)
        assert "baz" in output_dereassign
        exporter_dereassign.raw_template = ""
        assert exporter_dereassign.template_file == "index.rst.j2"
        output_dereassign, _ = exporter_dereassign.from_notebook_node(nb)
        assert "blah" not in output_dereassign

    def test_fail_to_find_template_file(self):
        # Create exporter with invalid template file, check that it doesn't
        # exist in the environment, try to convert empty notebook. Failure is
        # expected due to nonexistant template file.

        template = "does_not_exist.tpl"
        exporter = TemplateExporter(template_file=template)
        assert template not in exporter.environment.list_templates(extensions=["tpl"])
        nb = v4.new_notebook()
        with pytest.raises(TemplateNotFound):
            out, resources = exporter.from_notebook_node(nb)

    def test_exclude_code_cell(self):
        no_io = {
            "TemplateExporter": {
                "exclude_output": True,
                "exclude_input": True,
                "exclude_input_prompt": False,
                "exclude_output_prompt": False,
                "exclude_markdown": False,
                "exclude_code_cell": False,
                "exclude_output_stdin": True,
            }
        }
        c_no_io = Config(no_io)
        exporter_no_io = TemplateExporter(config=c_no_io, template_name="markdown")
        exporter_no_io.template_file = "index.md.j2"
        nb_no_io, resources_no_io = exporter_no_io.from_filename(self._get_notebook())

        assert not resources_no_io["global_content_filter"]["include_input"]
        assert not resources_no_io["global_content_filter"]["include_output"]

        no_code = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": False,
                "exclude_output_prompt": False,
                "exclude_markdown": False,
                "exclude_code_cell": True,
                "exclude_output_stdin": True,
            }
        }
        c_no_code = Config(no_code)
        exporter_no_code = TemplateExporter(config=c_no_code, template_name="markdown")
        exporter_no_code.template_file = "index.md.j2"
        nb_no_code, resources_no_code = exporter_no_code.from_filename(self._get_notebook())

        assert not resources_no_code["global_content_filter"]["include_code"]
        assert nb_no_io == nb_no_code

    def test_exclude_input_prompt(self):
        no_input_prompt = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": True,
                "exclude_output_prompt": False,
                "exclude_markdown": False,
                "exclude_code_cell": False,
                "exclude_output_stdin": True,
            }
        }
        c_no_input_prompt = Config(no_input_prompt)
        exporter_no_input_prompt = MarkdownExporter(config=c_no_input_prompt)
        nb_no_input_prompt, resources_no_input_prompt = exporter_no_input_prompt.from_filename(
            self._get_notebook()
        )

        assert not resources_no_input_prompt["global_content_filter"]["include_input_prompt"]
        assert "# In[" not in nb_no_input_prompt

    def test_exclude_markdown(self):

        no_md = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": False,
                "exclude_output_prompt": False,
                "exclude_markdown": True,
                "exclude_code_cell": False,
                "exclude_output_stdin": True,
            }
        }

        c_no_md = Config(no_md)
        exporter_no_md = TemplateExporter(config=c_no_md, template_name="python")
        exporter_no_md.template_file = "index.py.j2"
        nb_no_md, resources_no_md = exporter_no_md.from_filename(self._get_notebook())

        assert not resources_no_md["global_content_filter"]["include_markdown"]
        assert "First import NumPy and Matplotlib" not in nb_no_md

    def test_exclude_output_prompt(self):
        no_output_prompt = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": False,
                "exclude_output_prompt": True,
                "exclude_markdown": False,
                "exclude_code_cell": False,
                "exclude_output_stdin": True,
            }
        }
        c_no_output_prompt = Config(no_output_prompt)
        exporter_no_output_prompt = HTMLExporter(config=c_no_output_prompt)
        nb_no_output_prompt, resources_no_output_prompt = exporter_no_output_prompt.from_filename(
            self._get_notebook()
        )

        assert not resources_no_output_prompt["global_content_filter"]["include_output_prompt"]
        assert "Out[1]" not in nb_no_output_prompt

    def test_exclude_output_stdin(self):
        no_output_stdin = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": False,
                "exclude_output_prompt": True,
                "exclude_markdown": False,
                "exclude_code_cell": False,
                "exclude_output_stdin": True,
            }
        }
        c_no_output_stdin = Config(no_output_stdin)
        exporter_no_output_prompt = HTMLExporter(config=c_no_output_stdin)

        nb_no_output_stdin, resources_no_output_stdin = exporter_no_output_prompt.from_filename(
            self._get_notebook("notebook3.ipynb")
        )

        assert not resources_no_output_stdin["global_content_filter"]["include_output_stdin"]
        assert "test input: input value" not in nb_no_output_stdin

    def test_include_output_stdin(self):
        output_stdin = {
            "TemplateExporter": {
                "exclude_output": False,
                "exclude_input": False,
                "exclude_input_prompt": False,
                "exclude_output_prompt": True,
                "exclude_markdown": False,
                "exclude_code_cell": False,
                "exclude_output_stdin": False,
            }
        }
        c_output_stdin = Config(output_stdin)
        exporter_output_stdin = HTMLExporter(config=c_output_stdin)

        nb_output_stdin, resources_output_stdin = exporter_output_stdin.from_filename(
            self._get_notebook("notebook3.ipynb")
        )

        assert resources_output_stdin["global_content_filter"]["include_output_stdin"]
        assert "test input: input value" in nb_output_stdin

    def test_remove_elements_with_tags(self):

        conf = Config(
            {
                "TagRemovePreprocessor": {
                    "remove_cell_tags": ["remove_cell"],
                    "remove_all_outputs_tags": ["remove_output"],
                    "remove_input_tags": ["remove_input"],
                },
            }
        )

        exporter = MarkdownExporter(config=conf)
        nb, resources = exporter.from_filename(self._get_notebook())

        assert "hist(evs.real)" not in nb
        assert "cell is just markdown testing whether" not in nb
        assert "(100,)" not in nb

    def _make_exporter(self, config=None):
        exporter = SampleExporter(config=config)
        return exporter
