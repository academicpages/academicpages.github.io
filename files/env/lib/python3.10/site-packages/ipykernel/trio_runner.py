import builtins
import logging
import signal
import threading
import traceback
import warnings

import trio


class TrioRunner:
    def __init__(self):
        self._cell_cancel_scope = None
        self._trio_token = None

    def initialize(self, kernel, io_loop):
        kernel.shell.set_trio_runner(self)
        kernel.shell.run_line_magic("autoawait", "trio")
        kernel.shell.magics_manager.magics["line"]["autoawait"] = lambda _: warnings.warn(
            "Autoawait isn't allowed in Trio background loop mode."
        )
        self._interrupted = False
        bg_thread = threading.Thread(target=io_loop.start, daemon=True, name="TornadoBackground")
        bg_thread.start()

    def interrupt(self, signum, frame):
        if self._cell_cancel_scope:
            self._cell_cancel_scope.cancel()
        else:
            raise Exception("Kernel interrupted but no cell is running")

    def run(self):
        old_sig = signal.signal(signal.SIGINT, self.interrupt)

        def log_nursery_exc(exc):
            exc = "\n".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
            logging.error("An exception occurred in a global nursery task.\n%s", exc)

        async def trio_main():
            self._trio_token = trio.lowlevel.current_trio_token()
            async with trio.open_nursery() as nursery:
                # TODO This hack prevents the nursery from cancelling all child
                # tasks when an uncaught exception occurs, but it's ugly.
                nursery._add_exc = log_nursery_exc
                builtins.GLOBAL_NURSERY = nursery  # type:ignore[attr-defined]
                await trio.sleep_forever()

        trio.run(trio_main)
        signal.signal(signal.SIGINT, old_sig)

    def __call__(self, async_fn):
        async def loc(coro):
            self._cell_cancel_scope = trio.CancelScope()
            with self._cell_cancel_scope:
                return await coro
            self._cell_cancel_scope = None

        return trio.from_thread.run(loc, async_fn, trio_token=self._trio_token)
