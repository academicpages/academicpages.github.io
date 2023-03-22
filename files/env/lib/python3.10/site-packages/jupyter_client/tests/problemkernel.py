"""Test kernel for signalling subprocesses"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import time

from ipykernel.displayhook import ZMQDisplayHook
from ipykernel.kernelapp import IPKernelApp
from ipykernel.kernelbase import Kernel


class ProblemTestKernel(Kernel):
    """Kernel for testing kernel problems"""

    implementation = "problemtest"
    implementation_version = "0.0"
    banner = ""


class ProblemTestApp(IPKernelApp):
    kernel_class = ProblemTestKernel

    def init_io(self):
        # Overridden to disable stdout/stderr capture
        self.displayhook = ZMQDisplayHook(self.session, self.iopub_socket)

    def init_sockets(self):
        if os.environ.get("FAIL_ON_START") == "1":
            # Simulates e.g. a port binding issue (Adress already in use)
            raise RuntimeError("Failed for testing purposes")
        return super().init_sockets()


if __name__ == "__main__":
    # make startup artificially slow,
    # so that we exercise client logic for slow-starting kernels
    startup_delay = int(os.environ.get("STARTUP_DELAY", "2"))
    time.sleep(startup_delay)
    ProblemTestApp.launch_instance()
