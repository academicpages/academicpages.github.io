"""Test kernel for signalling subprocesses"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import signal
import time
from subprocess import PIPE
from subprocess import Popen

from ipykernel.displayhook import ZMQDisplayHook
from ipykernel.kernelapp import IPKernelApp
from ipykernel.kernelbase import Kernel


class SignalTestKernel(Kernel):
    """Kernel for testing subprocess signaling"""

    implementation = "signaltest"
    implementation_version = "0.0"
    banner = ""

    def __init__(self, **kwargs):
        kwargs.pop("user_ns", None)
        super().__init__(**kwargs)
        self.children = []

        if os.environ.get("NO_SIGTERM_REPLY", None) == "1":
            signal.signal(signal.SIGTERM, signal.SIG_IGN)

    async def shutdown_request(self, stream, ident, parent):
        if os.environ.get("NO_SHUTDOWN_REPLY") != "1":
            await super().shutdown_request(stream, ident, parent)

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        code = code.strip()
        reply = {
            "status": "ok",
            "user_expressions": {},
        }
        if code == "start":
            child = Popen(["bash", "-i", "-c", "sleep 30"], stderr=PIPE)
            self.children.append(child)
            reply["user_expressions"]["pid"] = self.children[-1].pid
        elif code == "check":
            reply["user_expressions"]["poll"] = [child.poll() for child in self.children]
        elif code == "env":
            reply["user_expressions"]["env"] = os.getenv("TEST_VARS", "")
        elif code == "sleep":
            try:
                time.sleep(10)
            except KeyboardInterrupt:
                reply["user_expressions"]["interrupted"] = True
            else:
                reply["user_expressions"]["interrupted"] = False
        else:
            reply["status"] = "error"
            reply["ename"] = "Error"
            reply["evalue"] = code
            reply["traceback"] = ["no such command: %s" % code]
        return reply


class SignalTestApp(IPKernelApp):
    kernel_class = SignalTestKernel

    def init_io(self):
        # Overridden to disable stdout/stderr capture
        self.displayhook = ZMQDisplayHook(self.session, self.iopub_socket)


if __name__ == "__main__":
    # make startup artificially slow,
    # so that we exercise client logic for slow-starting kernels
    time.sleep(2)
    SignalTestApp.launch_instance()
