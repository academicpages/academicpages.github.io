#############################################################################
# Copyright (c) 2021, Voilà Contributors                                    #
# Copyright (c) 2021, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################


import os
import sys
import traceback
from typing import Generator, Tuple, Union, List
import nbformat
import tornado.web
from jupyter_server.config_manager import recursive_update
from nbclient.exceptions import CellExecutionError
from nbclient.util import ensure_async
from nbconvert.preprocessors import ClearOutputPreprocessor
from traitlets.config.configurable import LoggingConfigurable

from .execute import VoilaExecutor, strip_code_cell_warnings
from .exporter import VoilaExporter
from .paths import collect_template_paths
from .utils import ENV_VARIABLE


class NotebookRenderer(LoggingConfigurable):
    """Render the notebook into HTML string."""

    def __init__(self, **kwargs):
        super().__init__()
        self.request_handler = kwargs.get('request_handler')
        self.root_dir = kwargs.get('root_dir', [])
        self.notebook_path = kwargs.get('notebook_path', [])  # should it be []
        self.template_paths = kwargs.get('template_paths', [])
        self.traitlet_config = kwargs.get('traitlet_config', None)
        self.voila_configuration = kwargs.get('voila_configuration')
        self.config_manager = kwargs.get('config_manager')
        self.contents_manager = kwargs.get('contents_manager')
        self.kernel_spec_manager = kwargs.get('kernel_spec_manager')
        self.prelaunch_hook = kwargs.get('prelaunch_hook')
        self.default_kernel_name = 'python3'
        self.base_url = kwargs.get('base_url')
        self.kernel_started = False
        self.stop_generator = False
        self.rendered_cache: List[str] = []

    async def initialize(self, **kwargs) -> None:
        """ Initialize the notebook generator.
        """
        notebook_path = self.notebook_path
        if self.voila_configuration.enable_nbextensions:
            # generate a list of nbextensions that are enabled for the classical notebook
            # a template can use that to load classical notebook extensions, but does not have to
            notebook_config = self.config_manager.get('notebook')
            # except for the widget extension itself, since Voilà has its own
            load_extensions = notebook_config.get('load_extensions', {})
            if 'jupyter-js-widgets/extension' in load_extensions:
                load_extensions['jupyter-js-widgets/extension'] = False
            if 'voila/extension' in load_extensions:
                load_extensions['voila/extension'] = False
            nbextensions = [
                name for name, enabled in load_extensions.items() if enabled
            ]
        else:
            nbextensions = []

        self.notebook = await self.load_notebook(notebook_path)

        self.cwd = os.path.dirname(notebook_path)

        if self.prelaunch_hook:
            # Allow for preprocessing the notebook.
            # Can be used to add auth, do custom formatting/standardization
            # of the notebook, raise exceptions, etc
            #
            # Necessary inside of the handler if you need
            # to access the tornado request itself
            returned_notebook = self.prelaunch_hook(self.request_handler,
                                                    notebook=self.notebook,
                                                    cwd=self.cwd)
            if returned_notebook:
                self.notebook = returned_notebook

        _, basename = os.path.split(notebook_path)
        notebook_name = os.path.splitext(basename)[0]

        # we can override the template via notebook metadata or via
        # input parameter
        template_override = None
        if (
            'voila' in self.notebook.metadata
            and self.voila_configuration.allow_template_override in ['YES', 'NOTEBOOK']
        ):
            template_override = self.notebook.metadata['voila'].get('template')

        if self.voila_configuration.allow_template_override == 'YES':
            template_arg = kwargs.get('template', None)
            template_override = (
                template_arg if template_arg is not None else template_override
            )
        if template_override:
            self.template_paths = collect_template_paths(
                ['voila', 'nbconvert'], template_override
            )
        self.template_name = template_override or self.voila_configuration.template

        theme_override = self.voila_configuration.theme
        if (
            'voila' in self.notebook.metadata
            and self.voila_configuration.allow_theme_override in ['YES', 'NOTEBOOK']
        ):
            theme_override = self.notebook.metadata['voila'].get(
                'theme', theme_override
            )
        if self.voila_configuration.allow_theme_override == 'YES':
            theme_arg = kwargs.get('theme', None)
            theme_override = theme_arg if theme_arg is not None else theme_override
        self.theme = theme_override
        # render notebook to html
        self.resources = {
            'base_url': self.base_url,
            'nbextensions': nbextensions,
            'theme': self.theme,
            'template': self.template_name,
            'metadata': {'name': notebook_name},
        }

        # include potential extra resources
        extra_resources = self.voila_configuration.config.VoilaConfiguration.resources
        # if no resources get configured from neither the CLI nor a config file,
        # extra_resources is a traitlets.config.loader.LazyConfigValue object
        # This seems to only happy with the notebook server and traitlets 5
        # Note that we use string checking for backward compatibility

        if 'DeferredConfigString' in str(type(extra_resources)):
            from .configuration import VoilaConfiguration

            extra_resources = VoilaConfiguration.resources.from_string(extra_resources)
        if not isinstance(extra_resources, dict):
            extra_resources = extra_resources.to_dict()
        if extra_resources:
            recursive_update(self.resources, extra_resources)

        self.exporter = VoilaExporter(
            template_paths=self.template_paths,
            template_name=self.template_name,
            config=self.traitlet_config,
            contents_manager=self.contents_manager,  # for the image inlining
            theme=self.theme,  # we now have the theme in two places
            base_url=self.base_url,
        )

        if self.voila_configuration.strip_sources:
            self.exporter.exclude_input = True
            self.exporter.exclude_output_prompt = True
            self.exporter.exclude_input_prompt = True

    def generate_content_generator(
        self,
        kernel_id: Union[str, None] = None,
        kernel_future=None,
    ) -> Generator:
        async def inner_kernel_start(nb):
            return await self._jinja_kernel_start(nb, kernel_id, kernel_future)

        def inner_cell_generator(nb, kernel_id):
            return self._jinja_cell_generator(nb, kernel_id)

        # These functions allow the start of a kernel and execution of the
        # notebook after (parts of) the template has been rendered and send
        # to the client to allow progressive rendering.
        # Template should first call kernel_start, and then decide to use
        # notebook_executer cell_generator to implement progressive cell rendering

        extra_context = {
            'kernel_start': inner_kernel_start,
            'cell_generator': inner_cell_generator,
            'notebook_execute': self._jinja_notebook_execute,
        }
        # render notebook in snippets, then return an iterator so we can flush
        # them out to the browser progressively.
        return self.exporter.generate_from_notebook_node(
            self.notebook, resources=self.resources, extra_context=extra_context
        )

    async def generate_content_hybrid(
        self,
        kernel_id: Union[str, None] = None,
        kernel_future=None,
    ) -> Tuple[List[str], Generator]:
        """Generate the HTML version of notebook, this process can be stopped
        anytime by setting `elf.stop_generator=True`. The remaining cells can
        be rendered after by using the returned generator.
        """
        rendered = []
        generator = self.generate_content_generator(kernel_id, kernel_future)
        async for html_snippet, _ in generator:
            rendered.append(html_snippet)
            if self.stop_generator:
                break
            self.rendered_cache.append(html_snippet)
        return rendered, generator

    async def generate_content_str(
        self,
        kernel_id: Union[str, None] = None,
        kernel_future=None,
    ) -> str:
        """Generate the HTML version of notebook."""
        html = ''
        async for html_snippet, _ in self.generate_content_generator(kernel_id, kernel_future):
            html += html_snippet
        return html

    async def _jinja_kernel_start(self, nb, kernel_id, kernel_future):
        assert not self.kernel_started, 'kernel was already started'
        km = await ensure_async(kernel_future)
        self.executor = VoilaExecutor(
            nb,
            km=km,
            config=self.traitlet_config,
            show_tracebacks=self.voila_configuration.show_tracebacks,
        )

        self.executor.kc = await self.executor.async_start_new_kernel_client()

        # Set `VOILA_KERNEL_ID` environment variable, this variable help user can
        # identify which kernel the notebook use.
        if nb.metadata.kernelspec['language'] == 'python':
            await ensure_async(
                self.executor.kc.execute(
                    f'''import os
                    \nos.environ["{ENV_VARIABLE.VOILA_KERNEL_ID}"]="{kernel_id}"
                    ''',
                    store_history=False,
                )
            )

        self.kernel_started = True
        return kernel_id

    async def _jinja_notebook_execute(self, nb, kernel_id):

        result = await self.executor.async_execute(cleanup_kc=False)
        # we modify the notebook in place, since the nb variable cannot be
        # reassigned it seems in jinja2 e.g. if we do {% with nb = notebook_execute(nb, kernel_id) %}
        # ,the base template/blocks will not see the updated variable
        #  (it seems to be local to our block)
        nb.cells = result.cells

        await self._cleanup_resources()

    async def _jinja_cell_generator(self, nb, kernel_id):
        """Generator that will execute a single notebook cell at a time"""
        nb, _ = ClearOutputPreprocessor().preprocess(
            nb, {'metadata': {'path': self.cwd}}
        )
        for cell_idx, input_cell in enumerate(nb.cells):
            try:
                output_cell = await self.executor.execute_cell(
                    input_cell, None, cell_idx, store_history=False
                )
            except TimeoutError:
                output_cell = input_cell
                break
            except CellExecutionError:
                self.log.exception(
                    'Error at server while executing cell: %r', input_cell
                )
                if self.executor.should_strip_error():
                    strip_code_cell_warnings(input_cell)
                    self.executor.strip_code_cell_errors(input_cell)
                output_cell = input_cell
                break
            except Exception as e:
                self.log.exception(
                    'Error at server while executing cell: %r', input_cell
                )
                output_cell = nbformat.v4.new_code_cell()
                if self.executor.should_strip_error():
                    output_cell.outputs = [
                        {
                            'output_type': 'stream',
                            'name': 'stderr',
                            'text': 'An exception occurred at the server (not the notebook). {}'.format(
                                self.executor.cell_error_instruction
                            ),
                        }
                    ]
                else:
                    output_cell.outputs = [
                        {
                            'output_type': 'error',
                            'ename': type(e).__name__,
                            'evalue': str(e),
                            'traceback': traceback.format_exception(*sys.exc_info()),
                        }
                    ]
            finally:
                yield output_cell

        await self._cleanup_resources()

    async def _cleanup_resources(self):
        await ensure_async(self.executor.km.cleanup_resources())
        await ensure_async(self.executor.kc.stop_channels())

    async def load_notebook(self, path):

        model = await ensure_async(self.contents_manager.get(path=path))
        if 'content' not in model:
            raise tornado.web.HTTPError(404, f'{path} can not be found')
        __, extension = os.path.splitext(model.get('path', ''))
        if model.get('type') == 'notebook':
            notebook = model['content']
            notebook = await self.fix_notebook(notebook)
            return notebook
        elif extension in self.voila_configuration.extension_language_mapping:
            language = self.voila_configuration.extension_language_mapping[extension]
            notebook = await self.create_notebook(model, language=language)
            return notebook
        else:
            raise tornado.web.HTTPError(500, f'Failed to load {path}')

    async def fix_notebook(self, notebook):
        """Returns a notebook object with a valid kernelspec.

        In case the kernel is not found, we search for a matching kernel based on the language.
        """

        # Fetch kernel name from the notebook metadata
        if 'kernelspec' not in notebook.metadata:
            notebook.metadata.kernelspec = nbformat.NotebookNode()
        kernelspec = notebook.metadata.kernelspec
        kernel_name = kernelspec.get('name', self.default_kernel_name)
        # We use `maybe_future` to support RemoteKernelSpecManager
        all_kernel_specs = await ensure_async(self.kernel_spec_manager.get_all_specs())
        # Find a spec matching the language if the kernel name does not exist in the kernelspecs
        if kernel_name not in all_kernel_specs:
            missing_kernel_name = kernel_name
            language = kernelspec.get(
                'language', notebook.metadata.get('language_info', {}).get('name', '')
            )
            kernel_name = await self.find_kernel_name_for_language(
                language.lower(), kernel_specs=all_kernel_specs
            )
            self.log.warning(
                'Could not find a kernel named %r, will use  %r',
                missing_kernel_name,
                kernel_name,
            )
        # We make sure the notebook's kernelspec is correct
        notebook.metadata.kernelspec.name = kernel_name
        notebook.metadata.kernelspec.display_name = all_kernel_specs[kernel_name][
            'spec'
        ]['display_name']
        notebook.metadata.kernelspec.language = all_kernel_specs[kernel_name]['spec'][
            'language'
        ]
        return notebook

    async def create_notebook(self, model, language):
        all_kernel_specs = await ensure_async(self.kernel_spec_manager.get_all_specs())
        kernel_name = await self.find_kernel_name_for_language(
            language, kernel_specs=all_kernel_specs
        )
        spec = all_kernel_specs[kernel_name]
        notebook = nbformat.v4.new_notebook(
            metadata={
                'kernelspec': {
                    'display_name': spec['spec']['display_name'],
                    'language': spec['spec']['language'],
                    'name': kernel_name,
                }
            },
            cells=[nbformat.v4.new_code_cell(model['content'])],
        )
        return notebook

    async def find_kernel_name_for_language(self, kernel_language, kernel_specs=None):
        """Finds a best matching kernel name given a kernel language.

        If multiple kernels matches are found, we try to return the same kernel name each time.
        """
        if kernel_language in self.voila_configuration.language_kernel_mapping:
            return self.voila_configuration.language_kernel_mapping[kernel_language]
        if kernel_specs is None:
            kernel_specs = await ensure_async(self.kernel_spec_manager.get_all_specs())
        matches = [
            name
            for name, kernel in kernel_specs.items()
            if kernel['spec']['language'].lower() == kernel_language.lower()
        ]
        if matches:
            # Sort by display name to get the same kernel each time.
            matches.sort(key=lambda name: kernel_specs[name]['spec']['display_name'])
            return matches[0]
        else:
            raise tornado.web.HTTPError(
                500, 'No Jupyter kernel for language %r found' % kernel_language
            )
