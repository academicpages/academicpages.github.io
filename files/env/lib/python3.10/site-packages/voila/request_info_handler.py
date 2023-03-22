from tornado.websocket import WebSocketHandler
import logging
from typing import Dict


class RequestInfoSocketHandler(WebSocketHandler):
    """A websocket handler used to provide the request info
    associated with kernel ids in preheat kernel mode.

    Class variables
    ---------------
    - _waiters : A dictionary which holds the `websocket` connection
    associated with the kernel id.

    - cache : A dictionary which holds the request info associated
    with the kernel id.
    """
    _waiters = dict()
    _cache = dict()

    def open(self, kernel_id: str) -> None:
        """Create a new websocket connection, this connection is
        identified by the kernel id.

        Args:
            kernel_id (str): Kernel id used by the notebook when it opens
            the websocket connection.
        """
        RequestInfoSocketHandler._waiters[kernel_id] = self
        if kernel_id in self._cache:
            self.write_message(self._cache[kernel_id])

    def on_close(self) -> None:
        for k_id, waiter in RequestInfoSocketHandler._waiters.items():
            if waiter == self:
                break
        del RequestInfoSocketHandler._waiters[k_id]

    @classmethod
    def send_updates(cls: 'RequestInfoSocketHandler', msg: Dict) -> None:
        """Class method used to dispatch the request info to the waiting
        notebook. This method is called in `VoilaHandler` when the request
        info becomes available.
        If this method is called before the opening of websocket connection,
        `msg` is stored in `_cache0` and the message will be dispatched when
        a notebook with corresponding kernel id is connected.

        Args:
            - msg (Dict): this dictionary contains the `kernel_id` to identify
            the waiting notebook and `payload` is the request info.
        """
        kernel_id = msg['kernel_id']
        payload = msg['payload']
        waiter = cls._waiters.get(kernel_id, None)
        if waiter is not None:
            try:
                waiter.write_message(payload)
            except Exception:
                logging.error("Error sending message", exc_info=True)

        cls._cache[kernel_id] = payload
