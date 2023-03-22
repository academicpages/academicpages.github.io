#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import os
import re

import tornado.web

from .paths import collect_static_paths


class TemplateStaticFileHandler(tornado.web.StaticFileHandler):
    """Static file handler that serves the static files for the template system.

    URL paths should be of the form <`template_name>/static/<path>`

    A url such as lab/static/voila.js can be translated to a real path such
    /my/prefix/jupyter/voila/templates/base/static/voila.js
    Meaning the url portion is not part of the real (absolute path)

    For this system, we don't need to use the root, since this is handled in the
    paths module.
    """
    def initialize(self):
        super().initialize(path='/fake-root/voila-template-system/')

    def parse_url_path(self, path):
        # since we cannot determine the template from validate_absolute_path
        # we get all possible roots here:
        template, static, _ignore = path.split('/', 2)
        assert static == 'static'
        self.roots = collect_static_paths(['voila', 'nbconvert'], template)
        # simply forward the call
        return super().parse_url_path(path)

    def validate_absolute_path(self, root: str, absolute_path: str):
        # Instead of comparing to 1 root (self.root), which we don't use
        # we compare it to all the roots, and only 1 combinations has to be valid
        last_exception = None
        for root in self.roots:
            try:
                return super().validate_absolute_path(root, absolute_path)
            except tornado.web.HTTPError as e:
                last_exception = e
        assert last_exception
        raise last_exception

    @classmethod
    def get_absolute_path(cls, root, path):
        template, static, relpath = os.path.normpath(path).split(os.path.sep, 2)
        assert static == 'static'
        roots = collect_static_paths(['voila', 'nbconvert'], template)
        for root in roots:
            abspath = os.path.abspath(os.path.join(root, relpath))
            if os.path.exists(abspath):
                return abspath
                break
        # if we didn't find it, we will simply return an invalid path
        # which will lead to a 404
        return abspath


class MultiStaticFileHandler(tornado.web.StaticFileHandler):
    """A static file handler that 'merges' a list of directories

    If initialized like this::

        application = web.Application([
            (r"/content/(.*)", web.MultiStaticFileHandler, {"paths": ["/var/1", "/var/2"]}),
        ])

    A file will be looked up in /var/1 first, then in /var/2.

    """

    def initialize(self, paths, default_filename=None):
        self.roots = paths
        super(MultiStaticFileHandler, self).initialize(path=paths[0], default_filename=default_filename)

    def get_absolute_path(self, root, path):
        # find the first absolute path that exists
        self.root = self.roots[0]
        for root in self.roots:
            abspath = os.path.abspath(os.path.join(root, path))
            if os.path.exists(abspath):
                self.root = root  # make sure all the other methods in the base class know how to find the file
                break
        return abspath


class WhiteListFileHandler(tornado.web.StaticFileHandler):
    def initialize(self, whitelist=[], blacklist=[], **kwargs):
        self.whitelist = whitelist
        self.blacklist = blacklist
        super(WhiteListFileHandler, self).initialize(**kwargs)

    def get_absolute_path(self, root, path):
        # StaticFileHandler.get always calls this method first, so we use this as the
        # place to check the path. Note that now the path separator is os dependent (\\ on windows)
        whitelisted = any(re.fullmatch(pattern, path) for pattern in self.whitelist)
        blacklisted = any(re.fullmatch(pattern, path) for pattern in self.blacklist)
        if not whitelisted:
            raise tornado.web.HTTPError(403, 'File not whitelisted')
        if blacklisted:
            raise tornado.web.HTTPError(403, 'File blacklisted')
        return super(WhiteListFileHandler, self).get_absolute_path(root, path)
