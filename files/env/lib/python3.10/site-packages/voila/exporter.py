#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import mimetypes

import traitlets
from traitlets.config import Config
try:
    from jinja2 import pass_context
except ImportError:
    from jinja2 import contextfilter as pass_context

from nbconvert.filters.markdown_mistune import IPythonRenderer, MarkdownWithMath
from nbconvert.exporters.html import HTMLExporter
from nbconvert.exporters.templateexporter import TemplateExporter
from nbconvert.filters.highlight import Highlight2HTML

from .static_file_handler import TemplateStaticFileHandler
from .utils import create_include_assets_functions


class VoilaMarkdownRenderer(IPythonRenderer):
    """Custom markdown renderer that inlines images"""

    def __init__(self, contents_manager, *args, **kwargs):
        self.contents_manager = contents_manager
        super().__init__(*args, **kwargs)

    def image(self, src, title, text):
        contents_manager = self.contents_manager
        if contents_manager.file_exists(src):
            content = contents_manager.get(src, format='base64')
            data = content['content'].replace('\n', '')  # remove the newline
            mime_type, encoding = mimetypes.guess_type(src)
            src = 'data:{mime_type};base64,{data}'.format(mime_type=mime_type, data=data)
        return super().image(src, title, text)


class VoilaExporter(HTMLExporter):
    """Custom HTMLExporter that inlines the images using VoilaMarkdownRenderer"""

    base_url = traitlets.Unicode(help="Base url for resources").tag(config=True)
    markdown_renderer_class = traitlets.Type(VoilaMarkdownRenderer).tag(config=True)
    # Can be a ContentsManager from notebook or jupyter_server, so Any will have to do for now
    contents_manager = traitlets.Any()

    # The voila exporter overrides the markdown renderer from the HTMLExporter
    # to inline images.

    @pass_context
    def markdown2html(self, context, source):
        cell = context['cell']
        attachments = cell.get('attachments', {})
        cls = self.markdown_renderer_class
        renderer = cls(escape=False, attachments=attachments,
                       contents_manager=self.contents_manager,
                       anchor_link_text=self.anchor_link_text)
        return MarkdownWithMath(renderer=renderer).render(source)

    # The voila exporter disables the CSSHTMLHeaderPreprocessor from the HTMLExporter.

    @property
    def default_config(self):
        c = Config({
            'VoilaExporter': {
                'markdown_renderer_class': 'voila.exporter.VoilaMarkdownRenderer'
            }
        })
        c.merge(super(VoilaExporter, self).default_config)
        return c

    # Overriding the default template file.

    @traitlets.default('template_file')
    def default_template_file(self):
        return 'index.html.j2'

    async def generate_from_notebook_node(self, nb, resources=None, extra_context={}, **kw):
        # this replaces from_notebook_node, but calls template.generate instead of template.render
        langinfo = nb.metadata.get('language_info', {})
        lexer = langinfo.get('pygments_lexer', langinfo.get('name', None))
        highlight_code = self.filters.get('highlight_code', Highlight2HTML(pygments_lexer=lexer, parent=self))
        self.register_filter('highlight_code', highlight_code)

        # NOTE: we don't call HTML or TemplateExporter' from_notebook_node
        nb_copy, resources = super(TemplateExporter, self).from_notebook_node(nb, resources, **kw)
        resources.setdefault('raw_mimetypes', self.raw_mimetypes)
        resources['global_content_filter'] = {
                'include_code': not self.exclude_code_cell,
                'include_markdown': not self.exclude_markdown,
                'include_raw': not self.exclude_raw,
                'include_unknown': not self.exclude_unknown,
                'include_input': not self.exclude_input,
                'include_output': not self.exclude_output,
                'include_input_prompt': not self.exclude_input_prompt,
                'include_output_prompt': not self.exclude_output_prompt,
                'no_prompt': self.exclude_input_prompt and self.exclude_output_prompt,
                }
        async for output in self.template.generate_async(nb=nb_copy, resources=resources, **extra_context, static_url=self.static_url):
            yield (output, resources)

    @property
    def environment(self):
        # enable Jinja async template execution
        self.enable_async = True
        env = super().environment
        if 'jinja2.ext.do' not in env.extensions:
            env.add_extension('jinja2.ext.do')
        return env

    def get_template_paths(self):
        return self.template_path

    def static_url(self, path):
        """Mimics tornado.web.RequestHandler.static_url"""
        settings = {
            'static_url_prefix': f'{self.base_url}voila/templates/',
            'static_path': None  # not used in TemplateStaticFileHandler.get_absolute_path
        }
        return TemplateStaticFileHandler.make_static_url(settings, f'{self.template_name}/static/{path}')

    def _init_resources(self, resources):
        resources = super(VoilaExporter, self)._init_resources(resources)

        include_assets_functions = create_include_assets_functions(self.template_name, self.base_url)

        resources.update(include_assets_functions)

        return resources
