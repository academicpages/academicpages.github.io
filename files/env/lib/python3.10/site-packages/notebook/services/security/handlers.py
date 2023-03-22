"""Tornado handlers for security logging."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web

from ...base.handlers import APIHandler
from . import csp_report_uri

class CSPReportHandler(APIHandler):
    '''Accepts a content security policy violation report'''

    _track_activity = False

    def skip_check_origin(self):
        """Don't check origin when reporting origin-check violations!"""
        return True

    def check_xsrf_cookie(self):
        # don't check XSRF for CSP reports
        return

    @web.authenticated
    def post(self):
        '''Log a content security policy violation report'''
        self.log.warning("Content security violation: %s",
                      self.request.body.decode('utf8', 'replace'))

default_handlers = [
    (csp_report_uri, CSPReportHandler)
]
