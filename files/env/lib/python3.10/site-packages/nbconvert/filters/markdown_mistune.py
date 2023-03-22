"""Markdown filters with mistune

Used from markdown.py
"""
# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.


import base64
import mimetypes
import os
import re
from functools import partial

try:
    from html import escape

    html_escape = partial(escape, quote=False)
except ImportError:
    # Python 2
    from cgi import escape as html_escape

import bs4
import mistune
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

from nbconvert.filters.strings import add_anchor


class InvalidNotebook(Exception):
    pass


class MathBlockGrammar(mistune.BlockGrammar):
    """This defines a single regex comprised of the different patterns that
    identify math content spanning multiple lines. These are used by the
    MathBlockLexer.
    """

    multi_math_str = "|".join(
        [r"^\$\$.*?\$\$", r"^\\\\\[.*?\\\\\]", r"^\\begin\{([a-z]*\*?)\}(.*?)\\end\{\1\}"]
    )
    multiline_math = re.compile(multi_math_str, re.DOTALL)


class MathBlockLexer(mistune.BlockLexer):
    """This acts as a pass-through to the MathInlineLexer. It is needed in
    order to avoid other block level rules splitting math sections apart.
    """

    default_rules = ["multiline_math"] + mistune.BlockLexer.default_rules

    def __init__(self, rules=None, **kwargs):
        if rules is None:
            rules = MathBlockGrammar()
        super().__init__(rules, **kwargs)

    def parse_multiline_math(self, m):
        """Add token to pass through mutiline math."""
        self.tokens.append({"type": "multiline_math", "text": m.group(0)})


class MathInlineGrammar(mistune.InlineGrammar):
    """This defines different ways of declaring math objects that should be
    passed through to mathjax unaffected. These are used by the MathInlineLexer.
    """

    inline_math = re.compile(r"^\$(.+?)\$|^\\\\\((.+?)\\\\\)", re.DOTALL)
    block_math = re.compile(r"^\$\$(.*?)\$\$|^\\\\\[(.*?)\\\\\]", re.DOTALL)
    latex_environment = re.compile(r"^\\begin\{([a-z]*\*?)\}(.*?)\\end\{\1\}", re.DOTALL)
    text = re.compile(r"^[\s\S]+?(?=[\\<!\[_*`~$]|https?://| {2,}\n|$)")


class MathInlineLexer(mistune.InlineLexer):
    r"""This interprets the content of LaTeX style math objects using the rules
    defined by the MathInlineGrammar.

    In particular this grabs ``$$...$$``, ``\\[...\\]``, ``\\(...\\)``, ``$...$``,
    and ``\begin{foo}...\end{foo}`` styles for declaring mathematics. It strips
    delimiters from all these varieties, and extracts the type of environment
    in the last case (``foo`` in this example).
    """
    default_rules = [
        "block_math",
        "inline_math",
        "latex_environment",
    ] + mistune.InlineLexer.default_rules

    def __init__(self, renderer, rules=None, **kwargs):
        if rules is None:
            rules = MathInlineGrammar()
        super().__init__(renderer, rules, **kwargs)

    def output_inline_math(self, m):
        return self.renderer.inline_math(m.group(1) or m.group(2))

    def output_block_math(self, m):
        return self.renderer.block_math(m.group(1) or m.group(2) or "")

    def output_latex_environment(self, m):
        return self.renderer.latex_environment(m.group(1), m.group(2))


class MarkdownWithMath(mistune.Markdown):
    def __init__(self, renderer, **kwargs):
        if "inline" not in kwargs:
            kwargs["inline"] = MathInlineLexer
        if "block" not in kwargs:
            kwargs["block"] = MathBlockLexer
        super().__init__(renderer, **kwargs)

    def output_multiline_math(self):
        return self.inline(self.token["text"])


class IPythonRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if lang:
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                code = lang + "\n" + code
                lang = None

        if not lang:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)

        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

    def block_html(self, html):
        embed_images = self.options.get("embed_images", False)

        if embed_images:
            html = self._html_embed_images(html)

        return super().block_html(html)

    def inline_html(self, html):
        embed_images = self.options.get("embed_images", False)

        if embed_images:
            html = self._html_embed_images(html)

        return super().inline_html(html)

    def header(self, text, level, raw=None):
        html = super().header(text, level, raw=raw)
        if self.options.get("exclude_anchor_links"):
            return html
        anchor_link_text = self.options.get("anchor_link_text", "¶")
        return add_anchor(html, anchor_link_text=anchor_link_text)

    def escape_html(self, text):
        return html_escape(text)

    def block_math(self, text):
        return "$$%s$$" % self.escape_html(text)

    def latex_environment(self, name, text):
        name = self.escape_html(name)
        text = self.escape_html(text)
        return rf"\begin{{{name}}}{text}\end{{{name}}}"

    def inline_math(self, text):
        return "$%s$" % self.escape_html(text)

    def image(self, src, title, text):
        """Rendering a image with title and text.

        :param src: source link of the image.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        attachments = self.options.get("attachments", {})
        attachment_prefix = "attachment:"
        embed_images = self.options.get("embed_images", False)

        if src.startswith(attachment_prefix):
            name = src[len(attachment_prefix) :]

            if name not in attachments:
                raise InvalidNotebook(f"missing attachment: {name}")

            attachment = attachments[name]
            # we choose vector over raster, and lossless over lossy
            preferred_mime_types = ["image/svg+xml", "image/png", "image/jpeg"]
            for preferred_mime_type in preferred_mime_types:
                if preferred_mime_type in attachment:
                    break
            else:  # otherwise we choose the first mimetype we can find
                preferred_mime_type = list(attachment.keys())[0]
            mime_type = preferred_mime_type
            data = attachment[mime_type]
            src = "data:" + mime_type + ";base64," + data

        elif embed_images:
            base64_url = self._src_to_base64(src)

            if base64_url is not None:
                src = base64_url

        return super().image(src, title, text)

    def _src_to_base64(self, src):
        """Turn the source file into a base64 url.

        :param src: source link of the file.
        :return: the base64 url or None if the file was not found.
        """
        path = self.options.get("path", "")
        src_path = os.path.join(path, src)

        if not os.path.exists(src_path):
            return None

        with open(src_path, "rb") as fobj:
            mime_type = mimetypes.guess_type(src_path)[0]

            base64_data = base64.b64encode(fobj.read())
            base64_data = base64_data.replace(b"\n", b"").decode("ascii")

            return f"data:{mime_type};base64,{base64_data}"

    def _html_embed_images(self, html):
        parsed_html = bs4.BeautifulSoup(html, features="html.parser")
        imgs = parsed_html.find_all("img")

        # Replace img tags's sources by base64 dataurls
        for img in imgs:
            if "src" not in img.attrs:
                continue

            base64_url = self._src_to_base64(img.attrs["src"])

            if base64_url is not None:
                img.attrs["src"] = base64_url

        return str(parsed_html)


def markdown2html_mistune(source):
    """Convert a markdown string to HTML using mistune"""
    return MarkdownWithMath(renderer=IPythonRenderer(escape=False)).render(source)
