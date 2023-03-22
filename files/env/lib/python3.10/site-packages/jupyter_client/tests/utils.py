"""Testing utils for jupyter_client tests

"""
import json
import os
import sys
from tempfile import TemporaryDirectory
from typing import Dict
from unittest.mock import patch

import pytest

from jupyter_client import AsyncKernelManager
from jupyter_client import AsyncMultiKernelManager
from jupyter_client import KernelManager
from jupyter_client import MultiKernelManager

pjoin = os.path.join

skip_win32 = pytest.mark.skipif(sys.platform.startswith("win"), reason="Windows")


sample_kernel_json = {
    "argv": ["cat", "{connection_file}"],
    "display_name": "Test kernel",
}


def install_kernel(kernels_dir, argv=None, name="test", display_name=None):
    """install a kernel in a kernels directory"""
    kernel_dir = pjoin(kernels_dir, name)
    os.makedirs(kernel_dir)
    kernel_json = {
        "argv": argv or sample_kernel_json["argv"],
        "display_name": display_name or sample_kernel_json["display_name"],
    }
    json_file = pjoin(kernel_dir, "kernel.json")
    with open(json_file, "w") as f:
        json.dump(kernel_json, f)
    return kernel_dir


class test_env(object):
    """Set Jupyter path variables to a temporary directory

    Useful as a context manager or with explicit start/stop
    """

    def start(self):
        self.test_dir = td = TemporaryDirectory()
        self.env_patch = patch.dict(
            os.environ,
            {
                "JUPYTER_CONFIG_DIR": pjoin(td.name, "jupyter"),
                "JUPYTER_DATA_DIR": pjoin(td.name, "jupyter_data"),
                "JUPYTER_RUNTIME_DIR": pjoin(td.name, "jupyter_runtime"),
                "IPYTHONDIR": pjoin(td.name, "ipython"),
                "TEST_VARS": "test_var_1",
            },
        )
        self.env_patch.start()

    def stop(self):
        self.env_patch.stop()
        try:
            self.test_dir.cleanup()
        except (PermissionError, NotADirectoryError):
            if os.name != 'nt':
                raise

    def __enter__(self):
        self.start()
        return self.test_dir.name

    def __exit__(self, *exc_info):
        self.stop()


def execute(code="", kc=None, **kwargs):
    """wrapper for doing common steps for validating an execution request"""
    from .test_message_spec import validate_message

    if kc is None:
        kc = KC  # noqa
    msg_id = kc.execute(code=code, **kwargs)
    reply = kc.get_shell_msg(timeout=TIMEOUT)  # noqa
    validate_message(reply, "execute_reply", msg_id)
    busy = kc.get_iopub_msg(timeout=TIMEOUT)  # noqa
    validate_message(busy, "status", msg_id)
    assert busy["content"]["execution_state"] == "busy"

    if not kwargs.get("silent"):
        execute_input = kc.get_iopub_msg(timeout=TIMEOUT)  # noqa
        validate_message(execute_input, "execute_input", msg_id)
        assert execute_input["content"]["code"] == code

    return msg_id, reply["content"]


class RecordCallMixin:
    method_calls: Dict[str, int]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method_calls = {}

    def record(self, method_name: str) -> None:
        if method_name not in self.method_calls:
            self.method_calls[method_name] = 0
        self.method_calls[method_name] += 1

    def call_count(self, method_name: str) -> int:
        if method_name not in self.method_calls:
            self.method_calls[method_name] = 0
        return self.method_calls[method_name]

    def reset_counts(self) -> None:
        for record in self.method_calls:
            self.method_calls[record] = 0


def subclass_recorder(f):
    def wrapped(self, *args, **kwargs):
        # record this call
        self.record(f.__name__)
        method = getattr(self._superclass, f.__name__)
        # call the superclass method
        r = method(self, *args, **kwargs)
        # call anything defined in the actual class method
        f(self, *args, **kwargs)
        return r

    return wrapped


class KMSubclass(RecordCallMixin):
    @subclass_recorder
    def start_kernel(self, **kw):
        """Record call and defer to superclass"""

    @subclass_recorder
    def shutdown_kernel(self, now=False, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def restart_kernel(self, now=False, **kw):
        """Record call and defer to superclass"""

    @subclass_recorder
    def interrupt_kernel(self):
        """Record call and defer to superclass"""

    @subclass_recorder
    def request_shutdown(self, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def finish_shutdown(self, waittime=None, pollinterval=0.1, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def _launch_kernel(self, kernel_cmd, **kw):
        """Record call and defer to superclass"""

    @subclass_recorder
    def _kill_kernel(self):
        """Record call and defer to superclass"""

    @subclass_recorder
    def cleanup_resources(self, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def signal_kernel(self, signum: int):
        """Record call and defer to superclass"""

    @subclass_recorder
    def is_alive(self):
        """Record call and defer to superclass"""

    @subclass_recorder
    def _send_kernel_sigterm(self, restart: bool = False):
        """Record call and defer to superclass"""


class SyncKMSubclass(KMSubclass, KernelManager):
    """Used to test subclass hierarchies to ensure methods are called when expected."""

    _superclass = KernelManager


class AsyncKMSubclass(KMSubclass, AsyncKernelManager):
    """Used to test subclass hierarchies to ensure methods are called when expected."""

    _superclass = AsyncKernelManager


class MKMSubclass(RecordCallMixin):
    def _kernel_manager_class_default(self):
        return "jupyter_client.tests.utils.SyncKMSubclass"

    @subclass_recorder
    def get_kernel(self, kernel_id):
        """Record call and defer to superclass"""

    @subclass_recorder
    def remove_kernel(self, kernel_id):
        """Record call and defer to superclass"""

    @subclass_recorder
    def start_kernel(self, kernel_name=None, **kwargs):
        """Record call and defer to superclass"""

    @subclass_recorder
    def shutdown_kernel(self, kernel_id, now=False, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def restart_kernel(self, kernel_id, now=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def interrupt_kernel(self, kernel_id):
        """Record call and defer to superclass"""

    @subclass_recorder
    def request_shutdown(self, kernel_id, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def finish_shutdown(self, kernel_id, waittime=None, pollinterval=0.1, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def cleanup_resources(self, kernel_id, restart=False):
        """Record call and defer to superclass"""

    @subclass_recorder
    def shutdown_all(self, now=False):
        """Record call and defer to superclass"""


class SyncMKMSubclass(MKMSubclass, MultiKernelManager):

    _superclass = MultiKernelManager

    def _kernel_manager_class_default(self):
        return "jupyter_client.tests.utils.SyncKMSubclass"


class AsyncMKMSubclass(MKMSubclass, AsyncMultiKernelManager):

    _superclass = AsyncMultiKernelManager

    def _kernel_manager_class_default(self):
        return "jupyter_client.tests.utils.AsyncKMSubclass"
