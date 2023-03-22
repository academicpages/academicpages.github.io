"""
Telnet server.
"""
import asyncio
import socket
import sys
from typing import Any, Awaitable, Callable, List, Optional, Set, TextIO, Tuple, cast

from prompt_toolkit.application.current import create_app_session, get_app
from prompt_toolkit.application.run_in_terminal import run_in_terminal
from prompt_toolkit.data_structures import Size
from prompt_toolkit.eventloop import get_event_loop
from prompt_toolkit.formatted_text import AnyFormattedText, to_formatted_text
from prompt_toolkit.input import PipeInput, create_pipe_input
from prompt_toolkit.output.vt100 import Vt100_Output
from prompt_toolkit.renderer import print_formatted_text as print_formatted_text
from prompt_toolkit.styles import BaseStyle, DummyStyle

from .log import logger
from .protocol import (
    DO,
    ECHO,
    IAC,
    LINEMODE,
    MODE,
    NAWS,
    SB,
    SE,
    SEND,
    SUPPRESS_GO_AHEAD,
    TTYPE,
    WILL,
    TelnetProtocolParser,
)

if sys.version_info >= (3, 7):
    import contextvars  # Requires Python3.7!
else:
    contextvars: Any = None

__all__ = [
    "TelnetServer",
]


def int2byte(number: int) -> bytes:
    return bytes((number,))


def _initialize_telnet(connection: socket.socket) -> None:
    logger.info("Initializing telnet connection")

    # Iac Do Linemode
    connection.send(IAC + DO + LINEMODE)

    # Suppress Go Ahead. (This seems important for Putty to do correct echoing.)
    # This will allow bi-directional operation.
    connection.send(IAC + WILL + SUPPRESS_GO_AHEAD)

    # Iac sb
    connection.send(IAC + SB + LINEMODE + MODE + int2byte(0) + IAC + SE)

    # IAC Will Echo
    connection.send(IAC + WILL + ECHO)

    # Negotiate window size
    connection.send(IAC + DO + NAWS)

    # Negotiate terminal type
    # Assume the client will accept the negociation with `IAC +  WILL + TTYPE`
    connection.send(IAC + DO + TTYPE)

    # We can then select the first terminal type supported by the client,
    # which is generally the best type the client supports
    # The client should reply with a `IAC + SB  + TTYPE + IS + ttype + IAC + SE`
    connection.send(IAC + SB + TTYPE + SEND + IAC + SE)


class _ConnectionStdout:
    """
    Wrapper around socket which provides `write` and `flush` methods for the
    Vt100_Output output.
    """

    def __init__(self, connection: socket.socket, encoding: str) -> None:
        self._encoding = encoding
        self._connection = connection
        self._errors = "strict"
        self._buffer: List[bytes] = []
        self._closed = False

    def write(self, data: str) -> None:
        data = data.replace("\n", "\r\n")
        self._buffer.append(data.encode(self._encoding, errors=self._errors))
        self.flush()

    def isatty(self) -> bool:
        return True

    def flush(self) -> None:
        try:
            if not self._closed:
                self._connection.send(b"".join(self._buffer))
        except OSError as e:
            logger.warning("Couldn't send data over socket: %s" % e)

        self._buffer = []

    def close(self) -> None:
        self._closed = True

    @property
    def encoding(self) -> str:
        return self._encoding

    @property
    def errors(self) -> str:
        return self._errors


class TelnetConnection:
    """
    Class that represents one Telnet connection.
    """

    def __init__(
        self,
        conn: socket.socket,
        addr: Tuple[str, int],
        interact: Callable[["TelnetConnection"], Awaitable[None]],
        server: "TelnetServer",
        encoding: str,
        style: Optional[BaseStyle],
        vt100_input: PipeInput,
        enable_cpr: bool = True,
    ) -> None:

        self.conn = conn
        self.addr = addr
        self.interact = interact
        self.server = server
        self.encoding = encoding
        self.style = style
        self._closed = False
        self._ready = asyncio.Event()
        self.vt100_input = vt100_input
        self.enable_cpr = enable_cpr
        self.vt100_output: Optional[Vt100_Output] = None

        # Create "Output" object.
        self.size = Size(rows=40, columns=79)

        # Initialize.
        _initialize_telnet(conn)

        # Create output.
        def get_size() -> Size:
            return self.size

        self.stdout = cast(TextIO, _ConnectionStdout(conn, encoding=encoding))

        def data_received(data: bytes) -> None:
            """TelnetProtocolParser 'data_received' callback"""
            self.vt100_input.send_bytes(data)

        def size_received(rows: int, columns: int) -> None:
            """TelnetProtocolParser 'size_received' callback"""
            self.size = Size(rows=rows, columns=columns)
            if self.vt100_output is not None and self.context:
                self.context.run(lambda: get_app()._on_resize())

        def ttype_received(ttype: str) -> None:
            """TelnetProtocolParser 'ttype_received' callback"""
            self.vt100_output = Vt100_Output(
                self.stdout, get_size, term=ttype, enable_cpr=enable_cpr
            )
            self._ready.set()

        self.parser = TelnetProtocolParser(data_received, size_received, ttype_received)
        self.context: Optional[contextvars.Context] = None

    async def run_application(self) -> None:
        """
        Run application.
        """

        def handle_incoming_data() -> None:
            data = self.conn.recv(1024)
            if data:
                self.feed(data)
            else:
                # Connection closed by client.
                logger.info("Connection closed by client. %r %r" % self.addr)
                self.close()

        # Add reader.
        loop = get_event_loop()
        loop.add_reader(self.conn, handle_incoming_data)

        try:
            # Wait for v100_output to be properly instantiated
            await self._ready.wait()
            with create_app_session(input=self.vt100_input, output=self.vt100_output):
                self.context = contextvars.copy_context()
                await self.interact(self)
        finally:
            self.close()

    def feed(self, data: bytes) -> None:
        """
        Handler for incoming data. (Called by TelnetServer.)
        """
        self.parser.feed(data)

    def close(self) -> None:
        """
        Closed by client.
        """
        if not self._closed:
            self._closed = True

            self.vt100_input.close()
            get_event_loop().remove_reader(self.conn)
            self.conn.close()
            self.stdout.close()

    def send(self, formatted_text: AnyFormattedText) -> None:
        """
        Send text to the client.
        """
        if self.vt100_output is None:
            return
        formatted_text = to_formatted_text(formatted_text)
        print_formatted_text(
            self.vt100_output, formatted_text, self.style or DummyStyle()
        )

    def send_above_prompt(self, formatted_text: AnyFormattedText) -> None:
        """
        Send text to the client.
        This is asynchronous, returns a `Future`.
        """
        formatted_text = to_formatted_text(formatted_text)
        return self._run_in_terminal(lambda: self.send(formatted_text))

    def _run_in_terminal(self, func: Callable[[], None]) -> None:
        # Make sure that when an application was active for this connection,
        # that we print the text above the application.
        if self.context:
            self.context.run(run_in_terminal, func)  # type: ignore
        else:
            raise RuntimeError("Called _run_in_terminal outside `run_application`.")

    def erase_screen(self) -> None:
        """
        Erase the screen and move the cursor to the top.
        """
        if self.vt100_output is None:
            return
        self.vt100_output.erase_screen()
        self.vt100_output.cursor_goto(0, 0)
        self.vt100_output.flush()


async def _dummy_interact(connection: TelnetConnection) -> None:
    pass


class TelnetServer:
    """
    Telnet server implementation.
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 23,
        interact: Callable[[TelnetConnection], Awaitable[None]] = _dummy_interact,
        encoding: str = "utf-8",
        style: Optional[BaseStyle] = None,
        enable_cpr: bool = True,
    ) -> None:

        self.host = host
        self.port = port
        self.interact = interact
        self.encoding = encoding
        self.style = style
        self.enable_cpr = enable_cpr
        self._application_tasks: List[asyncio.Task[None]] = []

        self.connections: Set[TelnetConnection] = set()
        self._listen_socket: Optional[socket.socket] = None

    @classmethod
    def _create_socket(cls, host: str, port: int) -> socket.socket:
        # Create and bind socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))

        s.listen(4)
        return s

    def start(self) -> None:
        """
        Start the telnet server.
        Don't forget to call `loop.run_forever()` after doing this.
        """
        self._listen_socket = self._create_socket(self.host, self.port)
        logger.info(
            "Listening for telnet connections on %s port %r", self.host, self.port
        )

        get_event_loop().add_reader(self._listen_socket, self._accept)

    async def stop(self) -> None:
        if self._listen_socket:
            get_event_loop().remove_reader(self._listen_socket)
            self._listen_socket.close()

        # Wait for all applications to finish.
        for t in self._application_tasks:
            t.cancel()

        # (This is similar to
        # `Application.cancel_and_wait_for_background_tasks`. We wait for the
        # background tasks to complete, but don't propagate exceptions, because
        # we can't use `ExceptionGroup` yet.)
        if len(self._application_tasks) > 0:
            await asyncio.wait(
                self._application_tasks, timeout=None, return_when=asyncio.ALL_COMPLETED
            )

    def _accept(self) -> None:
        """
        Accept new incoming connection.
        """
        if self._listen_socket is None:
            return  # Should not happen. `_accept` is called after `start`.

        conn, addr = self._listen_socket.accept()
        logger.info("New connection %r %r", *addr)

        # Run application for this connection.
        async def run() -> None:
            try:
                with create_pipe_input() as vt100_input:
                    connection = TelnetConnection(
                        conn,
                        addr,
                        self.interact,
                        self,
                        encoding=self.encoding,
                        style=self.style,
                        vt100_input=vt100_input,
                        enable_cpr=self.enable_cpr,
                    )
                    self.connections.add(connection)

                    logger.info("Starting interaction %r %r", *addr)
                    try:
                        await connection.run_application()
                    finally:
                        self.connections.remove(connection)
                        logger.info("Stopping interaction %r %r", *addr)
            except EOFError:
                # Happens either when the connection is closed by the client
                # (e.g., when the user types 'control-]', then 'quit' in the
                # telnet client) or when the user types control-d in a prompt
                # and this is not handled by the interact function.
                logger.info("Unhandled EOFError in telnet application.")
            except KeyboardInterrupt:
                # Unhandled control-c propagated by a prompt.
                logger.info("Unhandled KeyboardInterrupt in telnet application.")
            except BaseException as e:
                print("Got %s" % type(e).__name__, e)
                import traceback

                traceback.print_exc()
            finally:
                self._application_tasks.remove(task)

        task = get_event_loop().create_task(run())
        self._application_tasks.append(task)
