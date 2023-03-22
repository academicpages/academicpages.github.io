from jupyter_client.manager import AsyncKernelManager


class FakeCustomKernelManager(AsyncKernelManager):
    expected_methods = {'__init__': 0, 'client': 0, 'start_kernel': 0}

    def __init__(self, *args, **kwargs):
        self.log.info('FakeCustomKernelManager initialized')
        self.expected_methods['__init__'] += 1
        super().__init__(*args, **kwargs)

    async def start_kernel(self, *args, **kwargs):
        self.log.info('FakeCustomKernelManager started a kernel')
        self.expected_methods['start_kernel'] += 1
        return await super().start_kernel(*args, **kwargs)

    def client(self, *args, **kwargs):
        self.log.info('FakeCustomKernelManager created a client')
        self.expected_methods['client'] += 1
        return super().client(*args, **kwargs)
