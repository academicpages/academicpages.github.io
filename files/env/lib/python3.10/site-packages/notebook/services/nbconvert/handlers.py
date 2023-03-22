import json

from tornado import web

from ...base.handlers import APIHandler


class NbconvertRootHandler(APIHandler):

    @web.authenticated
    def get(self):
        self.check_xsrf_cookie()
        try:
            from nbconvert.exporters import base
        except ImportError as e:
            raise web.HTTPError(500, f"Could not import nbconvert: {e}") from e
        res = {}
        exporters = base.get_export_names()
        for exporter_name in exporters:
            try:
                exporter_class = base.get_exporter(exporter_name)
            except ValueError:
                # I think the only way this will happen is if the entrypoint
                # is uninstalled while this method is running
                continue
            # XXX: According to the docs, it looks like this should be set to None
            # if the exporter shouldn't be exposed to the front-end and a friendly
            # name if it should. However, none of the built-in exports have it defined.
            # if not exporter_class.export_from_notebook:
            #    continue
            res[exporter_name] = {
                "output_mimetype": exporter_class.output_mimetype,
            }

        self.finish(json.dumps(res))

default_handlers = [
    (r"/api/nbconvert", NbconvertRootHandler),
]
