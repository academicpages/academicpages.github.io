"""Test IO capturing functionality"""

import io
import warnings

import pytest
import zmq
from jupyter_client.session import Session

from ipykernel.iostream import MASTER, BackgroundSocket, IOPubThread, OutStream


def test_io_api():
    """Test that wrapped stdout has the same API as a normal TextIO object"""
    session = Session()
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    thread = IOPubThread(pub)
    thread.start()

    stream = OutStream(session, thread, "stdout")

    # cleanup unused zmq objects before we start testing
    thread.stop()
    thread.close()
    ctx.term()

    assert stream.errors is None
    assert not stream.isatty()
    with pytest.raises(io.UnsupportedOperation):
        stream.detach()
    with pytest.raises(io.UnsupportedOperation):
        next(stream)
    with pytest.raises(io.UnsupportedOperation):
        stream.read()
    with pytest.raises(io.UnsupportedOperation):
        stream.readline()
    with pytest.raises(io.UnsupportedOperation):
        stream.seek(0)
    with pytest.raises(io.UnsupportedOperation):
        stream.tell()
    with pytest.raises(TypeError):
        stream.write(b"")  # type:ignore


def test_io_isatty():
    session = Session()
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    thread = IOPubThread(pub)
    thread.start()

    stream = OutStream(session, thread, "stdout", isatty=True)
    assert stream.isatty()


def test_io_thread():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    thread = IOPubThread(pub)
    thread._setup_pipe_in()
    msg = [thread._pipe_uuid, b"a"]
    thread._handle_pipe_msg(msg)
    ctx1, pipe = thread._setup_pipe_out()
    pipe.close()
    thread._pipe_in.close()
    thread._check_mp_mode = lambda: MASTER  # type:ignore
    thread._really_send([b"hi"])
    ctx1.destroy()
    thread.close()
    thread.close()
    thread._really_send(None)


def test_background_socket():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    thread = IOPubThread(pub)
    sock = BackgroundSocket(thread)
    assert sock.__class__ == BackgroundSocket
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        sock.linger = 101
        assert thread.socket.linger == 101
    assert sock.io_thread == thread
    sock.send(b"hi")


def test_outstream():
    session = Session()
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    thread = IOPubThread(pub)
    thread.start()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        stream = OutStream(session, pub, "stdout")
        stream = OutStream(session, thread, "stdout", pipe=object())

    stream = OutStream(session, thread, "stdout", isatty=True, echo=io.StringIO())
    with pytest.raises(io.UnsupportedOperation):
        stream.fileno()
    stream._watch_pipe_fd()
    stream.flush()
    stream.write("hi")
    stream.writelines(["ab", "cd"])
    assert stream.writable()
