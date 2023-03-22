import os
import stat
import subprocess
import sys
import time
import pytest

from notebook import DEFAULT_NOTEBOOK_PORT

from .launchnotebook import UNIXSocketNotebookTestBase
from ..utils import urlencode_unix_socket, urlencode_unix_socket_path


pytestmark = pytest.mark.integration_tests


@pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
def test_shutdown_sock_server_integration():
    sock = UNIXSocketNotebookTestBase.sock
    url = urlencode_unix_socket(sock).encode()
    encoded_sock_path = urlencode_unix_socket_path(sock)

    p = subprocess.Popen(
        ['jupyter-notebook', f'--sock={sock}', '--sock-mode=0700'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    complete = False
    for line in iter(p.stderr.readline, b''):
        print(line.decode())
        if url in line:
            complete = True
            break

    assert complete, 'did not find socket URL in stdout when launching notebook'

    assert encoded_sock_path.encode() in subprocess.check_output(['jupyter-notebook', 'list'])

    # Ensure umask is properly applied.
    assert stat.S_IMODE(os.lstat(sock).st_mode) == 0o700

    try:
        subprocess.check_output(['jupyter-notebook', 'stop'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert 'There is currently no server running on' in e.output.decode()
    else:
        raise AssertionError('expected stop command to fail due to target mis-match')

    assert encoded_sock_path.encode() in subprocess.check_output(['jupyter-notebook', 'list'])

    subprocess.check_output(['jupyter-notebook', 'stop', sock])

    assert encoded_sock_path.encode() not in subprocess.check_output(['jupyter-notebook', 'list'])

    p.wait()


def test_sock_server_validate_sockmode_type():
    try:
        subprocess.check_output(
            ['jupyter-notebook', '--sock=/tmp/nonexistent', '--sock-mode=badbadbad'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        assert 'badbadbad' in e.output.decode()
    else:
        raise AssertionError('expected execution to fail due to validation of --sock-mode param')


def test_sock_server_validate_sockmode_accessible():
    try:
        subprocess.check_output(
            ['jupyter-notebook', '--sock=/tmp/nonexistent', '--sock-mode=0444'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        assert '0444' in e.output.decode()
    else:
        raise AssertionError('expected execution to fail due to validation of --sock-mode param')


def _ensure_stopped(check_msg='There are no running servers'):
    try:
        subprocess.check_output(
            ['jupyter-notebook', 'stop'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        assert check_msg in e.output.decode()
    else:
        raise AssertionError('expected all servers to be stopped')


@pytest.mark.skipif(not bool(os.environ.get('RUN_NB_INTEGRATION_TESTS', False)), reason="for local testing")
def test_stop_multi_integration():
    """Tests lifecycle behavior for mixed-mode server types w/ default ports.

    Mostly suitable for local dev testing due to reliance on default port binding.
    """
    TEST_PORT = '9797'
    MSG_TMPL = 'Shutting down server on {}...'

    _ensure_stopped()

    # Default port.
    p1 = subprocess.Popen(
        ['jupyter-notebook', '--no-browser']
    )

    # Unix socket.
    sock = UNIXSocketNotebookTestBase.sock
    p2 = subprocess.Popen(
        ['jupyter-notebook', f'--sock={sock}']
    )

    # Specified port
    p3 = subprocess.Popen(
        ['jupyter-notebook', '--no-browser', f'--port={TEST_PORT}']
    )

    time.sleep(3)

    assert MSG_TMPL.format(DEFAULT_NOTEBOOK_PORT) in subprocess.check_output(
        ['jupyter-notebook', 'stop']
    ).decode()

    _ensure_stopped('There is currently no server running on 8888')

    assert MSG_TMPL.format(sock) in subprocess.check_output(
        ['jupyter-notebook', 'stop', sock]
    ).decode()

    assert MSG_TMPL.format(TEST_PORT) in subprocess.check_output(
        ['jupyter-notebook', 'stop', TEST_PORT]
    ).decode()

    _ensure_stopped()

    p1.wait()
    p2.wait()
    p3.wait()


@pytest.mark.skipif(sys.platform == "win32", reason="do not run on windows")
def test_launch_socket_collision():
    """Tests UNIX socket in-use detection for lifecycle correctness."""
    sock = UNIXSocketNotebookTestBase.sock
    check_msg = f'socket {sock} is already in use'

    _ensure_stopped()

    # Start a server.
    cmd = ['jupyter-notebook', f'--sock={sock}']
    p1 = subprocess.Popen(cmd)
    time.sleep(3)

    # Try to start a server bound to the same UNIX socket.
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert check_msg in e.output.decode()
    else:
        raise AssertionError(f'expected error, instead got {e.output.decode()}')

    # Stop the background server, ensure it's stopped and wait on the process to exit.
    subprocess.check_call(['jupyter-notebook', 'stop', sock])

    _ensure_stopped()

    p1.wait()
