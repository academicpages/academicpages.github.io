#############################################################################
# Copyright (c) 2021, Voilà Contributors                                    #
# Copyright (c) 2021, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################


import asyncio
import os
from typing import Awaitable, Tuple, Type, TypeVar, Union
from typing import Dict as TypeDict
from typing import List as TypeList
from pathlib import Path
from traitlets.traitlets import Dict, Float, List, default
from nbclient.util import ensure_async
import re
from .notebook_renderer import NotebookRenderer
from .utils import ENV_VARIABLE

T = TypeVar('T')


async def wait_before(delay: float, aw: Awaitable) -> Awaitable:
    await asyncio.sleep(delay)
    return await aw


def voila_kernel_manager_factory(base_class: Type[T], preheat_kernel: bool, default_pool_size: int) -> T:
    """
    Decorator used to make a normal kernel manager compatible with pre-heated
    kernel system.
    - If `preheat_kernel` is `False`, only the property
    `notebook_data` and the method `get_pool_size` are added to keep `VoilaHandler`
    working, the kernel manager will work as it is.
    - If `preheat_kernel` is `True`, the input class is transformed to
     `VoilaKernelManager` with all the functionalities.

    Args:
        - base_class (Type[T]): The kernel manager class
        - preheat_kernel (Bool): Flag to decorate the input class
        - default_pool_size (int): Size of pre-heated kernel pool for each notebook.
            Zero or negative number means disabled

    Returns:
        T: Decorated class
    """
    if not preheat_kernel:

        class NormalKernelManager(base_class):

            @property
            def notebook_data(self) -> TypeDict:
                return {}

            def get_pool_size(self, nb: str) -> int:
                return 0

        return NormalKernelManager

    else:

        class VoilaKernelManager(base_class):
            """This class adds pooling heated kernels and pre-rendered notebook
            feature to a normal kernel manager. The 'pooling heated kernels'
            part is heavily inspired from `hotpot_km`(https://github.com/voila-dashboards/hotpot_km) library.
            """

            kernel_pools_config = Dict(
                config=True,
                help='''Mapping from notebook name to the kernel configuration
                like: number of started kernels to keep on standby, environment
                variables used to start kernel''',
            )

            default_env_variables = Dict(
                {},
                config=True,
                help='''Default environmental variables for kernels
                ''',
            )

            preheat_blacklist = List([],
                                     config=True,
                                     help='List of notebooks which do not use pre-heated kernel.')

            fill_delay = Float(
                1,
                config=True,
                help='Wait time before re-filling the pool after a kernel is used',
            )

            @default('kernel_pools_config')
            def _kernel_pools_config(self):
                return {
                    'default': {
                        'pool_size': max(default_pool_size, 0),
                        'kernel_env_variables': self.default_env_variables,
                    }
                }

            def __init__(self, **kwargs):

                super().__init__(**kwargs)
                self._wait_at_startup = True
                self.notebook_data: TypeDict = {}
                self._pools: TypeDict[str, List[TypeDict]] = {}
                self.root_dir = self.parent.root_dir
                if self.parent.notebook_path is not None:
                    self.notebook_path = os.path.relpath(
                        self.parent.notebook_path, self.root_dir
                    )
                    self.fill_if_needed(delay=0, notebook_name=self.notebook_path)
                else:
                    self.notebook_path = None
                    all_notebooks = [
                        x.relative_to(self.root_dir)
                        for x in list(Path(self.root_dir).rglob('*.ipynb'))
                        if self._notebook_filter(x)
                    ]
                    for nb in all_notebooks:
                        self.fill_if_needed(delay=0, notebook_name=str(nb))

            async def get_rendered_notebook(
                self, notebook_name: str, **kwargs
            ) -> Tuple[asyncio.Task, TypeList[str]]:
                """ Get the notebook rendering task and the rendered cell.
                By setting the `stop_generator` to True, the running task
                `render_task` used for rendering notebook will be stopped
                after finishing the running cell. The results of this task
                will contain the rendered cells and a generator for continuing
                render the remaining cells. We need to return also
                `renderer.rendered_cache` since it contains the rendered cells
                before the moment we set `stop_generator` to `True`, so that
                we can flush data immediately without waiting for running cell
                to be finished.

                Args:
                    notebook_name (str): Path to notebook

                Raises:
                    NameError: Raised if no notebook is provided.
                    Exception: Raised if the kernel pool is empty.

                Returns:
                    Tuple[asyncio.Task, List[str]]:

                """
                if notebook_name is None:
                    raise NameError('Notebook name must be provided!')

                if (len(self._pools.get(notebook_name, ())) == 0):
                    raise Exception(f'Kernel pool for {notebook_name} is empty!')

                pool_item = self._pools[notebook_name].pop(0)
                content = await pool_item
                renderer: NotebookRenderer = content['renderer']
                render_task: asyncio.Task = content['task']
                kernel_id: str = content['kernel_id']
                renderer.stop_generator = True
                self.log.info('Using pre-heated kernel: %s for %s', kernel_id, notebook_name)
                self.fill_if_needed(delay=None, notebook_name=notebook_name, **kwargs)

                return render_task, renderer.rendered_cache, kernel_id

            def get_pool_size(self, notebook_name: str) -> int:
                return len(self._pools.get(notebook_name, []))

            def fill_if_needed(
                self,
                delay: Union[float, None] = None,
                notebook_name: Union[str, None] = None,
                **kwargs,
            ) -> None:
                """Start kernels until the pool is full

                Args:
                    - delay (Union[float, None], optional): Delay time before
                    starting refill kernel. Defaults to None.
                    - notebook_name (Union[str, None], optional): Name of notebook to
                    create kernel pool.
                    Defaults to None.
                """
                delay = delay if delay is not None else self.fill_delay
                try:
                    loop = asyncio.get_event_loop()
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                default_config: dict = self.kernel_pools_config.get('default', {})
                notebook_config: dict = self.kernel_pools_config.get(
                    notebook_name, default_config
                )
                kernel_env_variables: dict = notebook_config.get(
                    'kernel_env_variables', default_config.get('kernel_env_variables', {})
                )
                kernel_size: int = notebook_config.get(
                    'pool_size', default_config.get('pool_size', 1)
                )
                pool = self._pools.get(notebook_name, [])
                self._pools[notebook_name] = pool
                if 'path' not in kwargs:
                    kwargs['path'] = (
                        os.path.dirname(notebook_name)
                        if notebook_name is not None
                        else self.root_dir
                    )
                kernel_env = os.environ.copy()
                kernel_env_arg = kwargs.get('env', {})
                kernel_env.update(kernel_env_arg)

                for key in kernel_env_variables:
                    if key not in kernel_env:
                        kernel_env[key] = kernel_env_variables[key]
                kernel_env[ENV_VARIABLE.VOILA_BASE_URL] = self.parent.base_url
                kernel_env[ENV_VARIABLE.VOILA_SERVER_URL] = self.parent.server_url
                kernel_env[ENV_VARIABLE.VOILA_APP_PORT] = str(self.parent.port)
                kernel_env[ENV_VARIABLE.VOILA_PREHEAT] = 'True'
                kwargs['env'] = kernel_env

                heated = len(pool)

                def task_counter(tk):
                    nonlocal heated
                    heated += 1
                    if (heated == kernel_size):
                        self.log.info(
                            'Kernel pool of %s is filled with %s kernel(s)', notebook_name, kernel_size)

                for _ in range(kernel_size - len(pool)):
                    # Start the work on the loop immediately, so it is ready when needed:
                    task = loop.create_task(
                        wait_before(delay, self._initialize(notebook_name, None, **kwargs))
                    )
                    pool.append(task)
                    task.add_done_callback(task_counter)

            async def restart_kernel(self, kernel_id: str, **kwargs) -> None:
                await ensure_async(super().restart_kernel(kernel_id, **kwargs))
                notebook_name = self._get_notebook_from_kernel(kernel_id)
                if notebook_name is not None:
                    await self._initialize(notebook_name, kernel_id, **kwargs)

            async def shutdown_kernel(self, kernel_id: str, *args, **kwargs):
                for pool in self._pools.values():
                    for i, f in enumerate(pool):
                        if f.done() and f.result().get('kernel_id') == kernel_id:
                            pool.pop(i)
                            break
                    else:
                        continue
                    break
                for value in self.notebook_data.values():
                    if kernel_id in value['kernel_ids']:
                        value['kernel_ids'].remove(kernel_id)

                return await ensure_async(
                    super().shutdown_kernel(kernel_id, *args, **kwargs)
                )

            async def shutdown_all(self, *args, **kwargs):
                await ensure_async(super().shutdown_all(*args, **kwargs))
                # Parent doesn't correctly add all created kernels until they have completed startup:
                pools = self._pools
                self._pools = {}

                for value in self.notebook_data.values():
                    value['kernel_ids'] = set()

                for pool in pools.values():
                    # The iteration gets confused if we don't copy pool
                    for task in tuple(pool):
                        try:
                            result = await task
                        except Exception:
                            pass
                        else:
                            kid = result['kernel_id']
                            if kid in self:
                                try:
                                    await ensure_async(
                                        self.shutdown_kernel(kid, *args, **kwargs)
                                    )
                                except RuntimeError:
                                    pass  # Kernel is not running

            async def _initialize(
                    self, notebook_path: str, kernel_id: str = None, **kwargs) -> str:
                """Run any configured initialization code in the kernel"""

                renderer = self._notebook_renderer_factory(notebook_path)
                await renderer.initialize()
                kernel_name = renderer.notebook.metadata.kernelspec.name

                if kernel_id is None:
                    kernel_id = await super().start_kernel(kernel_name=kernel_name, **kwargs)

                if renderer.notebook_path not in self.notebook_data:
                    self.notebook_data[renderer.notebook_path] = {
                        'notebook': renderer.notebook,
                        'template': renderer.template_name,
                        'theme': renderer.theme,
                        'kernel_name': kernel_name,
                        'kernel_ids': {kernel_id}
                    }
                else:
                    self.notebook_data[renderer.notebook_path]['kernel_ids'].add(kernel_id)

                kernel_future = self.get_kernel(kernel_id)
                task = asyncio.get_event_loop().create_task(renderer.generate_content_hybrid(kernel_id, kernel_future))
                return {'task': task, 'renderer': renderer, 'kernel_id': kernel_id}

            async def cull_kernel_if_idle(self, kernel_id: str):
                """Ensure we don't cull pooled kernels:
                (this logic assumes the init time is shorter than the cull time)
                """

                for pool in self._pools.values():
                    for i, f in enumerate(pool):
                        try:
                            if f.done() and f.result().get('kernel_id') == kernel_id:
                                return
                        except Exception:
                            pool.pop(i)
                return await ensure_async(super().cull_kernel_if_idle(kernel_id))

            def _notebook_renderer_factory(
                self, notebook_path: Union[str, None] = None
            ) -> NotebookRenderer:
                """Helper function to create `NotebookRenderer` instance.

                Args:
                    - notebook_path (Union[str, None], optional): Path to the
                    notebook. Defaults to None.
                """
                return NotebookRenderer(
                    voila_configuration=self.parent.voila_configuration,
                    traitlet_config=self.parent.config,
                    notebook_path=notebook_path,
                    template_paths=self.parent.template_paths,
                    config_manager=self.parent.config_manager,
                    contents_manager=self.parent.contents_manager,
                    base_url=self.parent.base_url,
                    kernel_spec_manager=self.parent.kernel_spec_manager,
                )

            def _notebook_filter(self, nb_path: Path) -> bool:
                """Helper to filter blacklisted notebooks.

                Args:
                    nb_path (Path): Path to notebook

                Returns:
                    bool: return `False` if notebook is in `ipynb_checkpoints` folder or
                    is blacklisted, `True` otherwise.
                """
                nb_name = str(nb_path)
                if '.ipynb_checkpoints' in nb_name:
                    return False
                for nb_pattern in self.preheat_blacklist:
                    pattern = re.compile(nb_pattern)
                    if (nb_pattern in nb_name) or bool(pattern.match(nb_name)):
                        return False
                return True

            def _get_notebook_from_kernel(self, kernel_id: str) -> Union[None, str]:
                """Helper to get notebook name from heated kernel id.

                Args:
                    kernel_id (str): Kernel id

                Returns:
                    Union[None, str]: return associated notebook with kernel id.

                """
                for nb_name, data in self.notebook_data.items():
                    if kernel_id in data['kernel_ids']:
                        return nb_name
                return None

    return VoilaKernelManager
