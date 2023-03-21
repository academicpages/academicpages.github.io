# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import socket
import sys


class SocketManager(object):
    """Create a socket and connect to the given address.

    The address is a (host: str, port: int) tuple.
    Example usage:

    ```
    with SocketManager(("localhost", 6767)) as sock:
        request = json.dumps(payload)
        result = s.socket.sendall(request.encode("utf-8"))
    ```
    """

    def __init__(self, addr):
        self.addr = addr
        self.socket = None

    def __enter__(self):
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
        )
        if sys.platform == "win32":
            addr_use = socket.SO_EXCLUSIVEADDRUSE
        else:
            addr_use = socket.SO_REUSEADDR
        self.socket.setsockopt(socket.SOL_SOCKET, addr_use, 1)
        self.socket.connect(self.addr)

        return self

    def __exit__(self, *_):
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            self.socket.close()
