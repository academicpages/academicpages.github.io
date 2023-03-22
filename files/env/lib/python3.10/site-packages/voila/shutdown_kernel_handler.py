import tornado
from jupyter_server.base.handlers import APIHandler
from nbclient.util import ensure_async


class VoilaShutdownKernelHandler(APIHandler):
    """ Handler to shut down kernel on page's `beforeunload` event.
    """

    @tornado.web.authenticated
    async def post(self, kernel_id):
        await ensure_async(self.kernel_manager.shutdown_kernel(kernel_id))
        self.set_status(204)
        self.finish()
