"""Test Provisioning"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import asyncio
import json
import os
import signal
import sys
from subprocess import PIPE
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import pytest
from entrypoints import EntryPoint
from entrypoints import NoSuchEntryPoint
from jupyter_core import paths
from traitlets import Int
from traitlets import Unicode

from ..connect import KernelConnectionInfo
from ..kernelspec import KernelSpecManager
from ..kernelspec import NoSuchKernel
from ..launcher import launch_kernel
from ..manager import AsyncKernelManager
from ..provisioning import KernelProvisionerBase
from ..provisioning import KernelProvisionerFactory
from ..provisioning import LocalProvisioner

pjoin = os.path.join


class SubclassedTestProvisioner(LocalProvisioner):

    config_var_1: int = Int(config=True)
    config_var_2: str = Unicode(config=True)

    pass


class CustomTestProvisioner(KernelProvisionerBase):

    process = None
    pid = None
    pgid = None

    config_var_1: int = Int(config=True)
    config_var_2: str = Unicode(config=True)

    @property
    def has_process(self) -> bool:
        return self.process is not None

    async def poll(self) -> Optional[int]:
        ret = 0
        if self.process:
            ret = self.process.poll()
        return ret

    async def wait(self) -> Optional[int]:
        ret = 0
        if self.process:
            while await self.poll() is None:
                await asyncio.sleep(0.1)

            # Process is no longer alive, wait and clear
            ret = self.process.wait()
            # Make sure all the fds get closed.
            for attr in ['stdout', 'stderr', 'stdin']:
                fid = getattr(self.process, attr)
                if fid:
                    fid.close()
            self.process = None
        return ret

    async def send_signal(self, signum: int) -> None:
        if self.process:
            if signum == signal.SIGINT and sys.platform == 'win32':
                from ..win_interrupt import send_interrupt

                send_interrupt(self.process.win32_interrupt_event)
                return

            # Prefer process-group over process
            if self.pgid and hasattr(os, "killpg"):
                try:
                    os.killpg(self.pgid, signum)
                    return
                except OSError:
                    pass
            return self.process.send_signal(signum)

    async def kill(self, restart=False) -> None:
        if self.process:
            self.process.kill()

    async def terminate(self, restart=False) -> None:
        if self.process:
            self.process.terminate()

    async def pre_launch(self, **kwargs: Any) -> Dict[str, Any]:
        km = self.parent
        if km:
            # save kwargs for use in restart
            km._launch_args = kwargs.copy()
            # build the Popen cmd
            extra_arguments = kwargs.pop('extra_arguments', [])

            # write connection file / get default ports
            km.write_connection_file()
            self.connection_info = km.get_connection_info()

            kernel_cmd = km.format_kernel_cmd(
                extra_arguments=extra_arguments
            )  # This needs to remain here for b/c

            return await super().pre_launch(cmd=kernel_cmd, **kwargs)

    async def launch_kernel(self, cmd: List[str], **kwargs: Any) -> KernelConnectionInfo:
        scrubbed_kwargs = kwargs
        self.process = launch_kernel(cmd, **scrubbed_kwargs)
        pgid = None
        if hasattr(os, "getpgid"):
            try:
                pgid = os.getpgid(self.process.pid)
            except OSError:
                pass

        self.pid = self.process.pid
        self.pgid = pgid
        return self.connection_info

    async def cleanup(self, restart=False) -> None:
        pass


class NewTestProvisioner(CustomTestProvisioner):
    pass


def build_kernelspec(name: str, provisioner: Optional[str] = None) -> None:
    spec = {
        'argv': [
            sys.executable,
            '-m',
            'jupyter_client.tests.signalkernel',
            '-f',
            '{connection_file}',
        ],
        'display_name': f"Signal Test Kernel w {provisioner}",
        'env': {'TEST_VARS': '${TEST_VARS}:test_var_2'},
        'metadata': {},
    }

    if provisioner:
        kernel_provisioner = {'kernel_provisioner': {'provisioner_name': provisioner}}
        spec['metadata'].update(kernel_provisioner)
        if provisioner != 'local-provisioner':
            spec['metadata']['kernel_provisioner']['config'] = {
                'config_var_1': 42,
                'config_var_2': name,
            }

    kernel_dir = pjoin(paths.jupyter_data_dir(), 'kernels', name)
    os.makedirs(kernel_dir)
    with open(pjoin(kernel_dir, 'kernel.json'), 'w') as f:
        f.write(json.dumps(spec))


def new_provisioner():
    build_kernelspec('new_provisioner', 'new-test-provisioner')


def custom_provisioner():
    build_kernelspec('custom_provisioner', 'custom-test-provisioner')


@pytest.fixture
def all_provisioners():
    build_kernelspec('no_provisioner')
    build_kernelspec('missing_provisioner', 'missing-provisioner')
    build_kernelspec('default_provisioner', 'local-provisioner')
    build_kernelspec('subclassed_provisioner', 'subclassed-test-provisioner')
    custom_provisioner()


@pytest.fixture(
    params=[
        'no_provisioner',
        'default_provisioner',
        'missing_provisioner',
        'custom_provisioner',
        'subclassed_provisioner',
    ]
)
def akm(request, all_provisioners):
    return AsyncKernelManager(kernel_name=request.param)


initial_provisioner_map = {
    'local-provisioner': ('jupyter_client.provisioning', 'LocalProvisioner'),
    'subclassed-test-provisioner': (
        'jupyter_client.tests.test_provisioning',
        'SubclassedTestProvisioner',
    ),
    'custom-test-provisioner': ('jupyter_client.tests.test_provisioning', 'CustomTestProvisioner'),
}


def mock_get_all_provisioners() -> List[EntryPoint]:
    result = []
    for name, epstr in initial_provisioner_map.items():
        result.append(EntryPoint(name, epstr[0], epstr[1]))
    return result


def mock_get_provisioner(factory, name) -> EntryPoint:
    if name == 'new-test-provisioner':
        return EntryPoint(
            'new-test-provisioner', 'jupyter_client.tests.test_provisioning', 'NewTestProvisioner'
        )

    if name in initial_provisioner_map:
        return EntryPoint(name, initial_provisioner_map[name][0], initial_provisioner_map[name][1])

    raise NoSuchEntryPoint(KernelProvisionerFactory.GROUP_NAME, name)


@pytest.fixture
def kpf(monkeypatch):
    """Setup the Kernel Provisioner Factory, mocking the entrypoint fetch calls."""
    monkeypatch.setattr(
        KernelProvisionerFactory, '_get_all_provisioners', mock_get_all_provisioners
    )
    monkeypatch.setattr(KernelProvisionerFactory, '_get_provisioner', mock_get_provisioner)
    factory = KernelProvisionerFactory.instance()
    return factory


class TestDiscovery:
    def test_find_all_specs(self, kpf, all_provisioners):
        ksm = KernelSpecManager()
        kernels = ksm.get_all_specs()

        # Ensure specs for initial provisioners exist,
        # and missing_provisioner & new_provisioner don't
        assert 'no_provisioner' in kernels
        assert 'default_provisioner' in kernels
        assert 'subclassed_provisioner' in kernels
        assert 'custom_provisioner' in kernels
        assert 'missing_provisioner' not in kernels
        assert 'new_provisioner' not in kernels

    def test_get_missing(self, all_provisioners):
        ksm = KernelSpecManager()
        with pytest.raises(NoSuchKernel):
            ksm.get_kernel_spec('missing_provisioner')

    def test_get_new(self, kpf):
        new_provisioner()  # Introduce provisioner after initialization of KPF
        ksm = KernelSpecManager()
        kernel = ksm.get_kernel_spec('new_provisioner')
        assert 'new-test-provisioner' == kernel.metadata['kernel_provisioner']['provisioner_name']


class TestRuntime:
    async def akm_test(self, kernel_mgr):
        """Starts a kernel, validates the associated provisioner's config, shuts down kernel"""

        assert kernel_mgr.provisioner is None
        if kernel_mgr.kernel_name == 'missing_provisioner':
            with pytest.raises(NoSuchKernel):
                await kernel_mgr.start_kernel()
        else:
            await kernel_mgr.start_kernel()

            TestRuntime.validate_provisioner(kernel_mgr)

            await kernel_mgr.shutdown_kernel()
            assert kernel_mgr.provisioner.has_process is False

    @pytest.mark.asyncio
    async def test_existing(self, kpf, akm):
        await self.akm_test(akm)

    @pytest.mark.asyncio
    async def test_new(self, kpf):
        new_provisioner()  # Introduce provisioner after initialization of KPF
        new_km = AsyncKernelManager(kernel_name='new_provisioner')
        await self.akm_test(new_km)

    @pytest.mark.asyncio
    async def test_custom_lifecycle(self, kpf):
        custom_provisioner()
        async_km = AsyncKernelManager(kernel_name='custom_provisioner')
        await async_km.start_kernel(stdout=PIPE, stderr=PIPE)
        is_alive = await async_km.is_alive()
        assert is_alive
        await async_km.restart_kernel(now=True)
        is_alive = await async_km.is_alive()
        assert is_alive
        await async_km.interrupt_kernel()
        assert isinstance(async_km, AsyncKernelManager)
        await async_km.shutdown_kernel(now=True)
        is_alive = await async_km.is_alive()
        assert is_alive is False
        assert async_km.context.closed

    @pytest.mark.asyncio
    async def test_default_provisioner_config(self, kpf, all_provisioners):
        kpf.default_provisioner_name = 'custom-test-provisioner'
        async_km = AsyncKernelManager(kernel_name='no_provisioner')
        await async_km.start_kernel(stdout=PIPE, stderr=PIPE)
        is_alive = await async_km.is_alive()
        assert is_alive

        assert isinstance(async_km.provisioner, CustomTestProvisioner)
        assert async_km.provisioner.config_var_1 == 0  # Not in kernelspec, so default of 0 exists

        await async_km.shutdown_kernel(now=True)
        is_alive = await async_km.is_alive()
        assert is_alive is False
        assert async_km.context.closed

    @staticmethod
    def validate_provisioner(akm: AsyncKernelManager):
        # Ensure the provisioner is managing a process at this point
        assert akm.provisioner is not None and akm.provisioner.has_process

        # Validate provisioner config
        if akm.kernel_name in ['no_provisioner', 'default_provisioner']:
            assert not hasattr(akm.provisioner, 'config_var_1')
            assert not hasattr(akm.provisioner, 'config_var_2')
        else:
            assert akm.provisioner.config_var_1 == 42
            assert akm.provisioner.config_var_2 == akm.kernel_name

        # Validate provisioner class
        if akm.kernel_name in ['no_provisioner', 'default_provisioner', 'subclassed_provisioner']:
            assert isinstance(akm.provisioner, LocalProvisioner)
            if akm.kernel_name == 'subclassed_provisioner':
                assert isinstance(akm.provisioner, SubclassedTestProvisioner)
            else:
                assert not isinstance(akm.provisioner, SubclassedTestProvisioner)
        else:
            assert isinstance(akm.provisioner, CustomTestProvisioner)
            assert not isinstance(akm.provisioner, LocalProvisioner)
            if akm.kernel_name == 'new_provisioner':
                assert isinstance(akm.provisioner, NewTestProvisioner)
