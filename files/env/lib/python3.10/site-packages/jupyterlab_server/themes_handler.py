"""Tornado handlers for dynamic theme loading."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import re
from glob import glob
from os import path as osp
from urllib.parse import urlparse

from .server import FileFindHandler
from .server import url_path_join as ujoin


class ThemesHandler(FileFindHandler):
    """A file handler that mangles local urls in CSS files."""

    def initialize(
        self,
        path,
        default_filename=None,
        no_cache_paths=None,
        themes_url=None,
        labextensions_path=None,
        **kwargs,
    ):
        """Initialize the handler."""
        # Get all of the available theme paths in order
        labextensions_path = labextensions_path or []
        ext_paths = []
        for ext_dir in labextensions_path:
            theme_pattern = ext_dir + "/**/themes"
            ext_paths.extend([path for path in glob(theme_pattern, recursive=True)])

        # Add the core theme path last
        if not isinstance(path, list):
            path = [path]
        path = ext_paths + path

        FileFindHandler.initialize(
            self, path, default_filename=default_filename, no_cache_paths=no_cache_paths
        )
        self.themes_url = themes_url

    def get_content(self, abspath, start=None, end=None):
        """Retrieve the content of the requested resource which is located
        at the given absolute path.

        This method should either return a byte string or an iterator
        of byte strings.
        """
        base, ext = osp.splitext(abspath)
        if ext != ".css":
            return FileFindHandler.get_content(abspath, start, end)

        return self._get_css()

    def get_content_size(self):
        """Retrieve the total size of the resource at the given path."""
        assert self.absolute_path is not None  # noqa
        base, ext = osp.splitext(self.absolute_path)
        if ext != ".css":
            return FileFindHandler.get_content_size(self)
        else:
            return len(self._get_css())

    def _get_css(self):
        """Get the mangled css file contents."""
        assert self.absolute_path is not None  # noqa
        with open(self.absolute_path, "rb") as fid:
            data = fid.read().decode("utf-8")

        basedir = osp.dirname(self.path).replace(os.sep, "/")
        basepath = ujoin(self.themes_url, basedir)

        # Replace local paths with mangled paths.
        # We only match strings that are local urls,
        # e.g. `url('../foo.css')`, `url('images/foo.png')`
        pattern = r"url\('(.*)'\)|url\('(.*)'\)"

        def replacer(m):
            """Replace the matched relative url with the mangled url."""
            group = m.group()
            # Get the part that matched
            part = [g for g in m.groups() if g][0]

            # Ignore urls that start with `/` or have a protocol like `http`.
            parsed = urlparse(part)
            if part.startswith("/") or parsed.scheme:
                return group

            return group.replace(part, ujoin(basepath, part))

        return re.sub(pattern, replacer, data).encode("utf-8")
