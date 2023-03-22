"""Base class for notebook tests."""

from binascii import hexlify
from contextlib import contextmanager
import errno
import os
import sys
from threading import Thread, Event
import time
from unittest import TestCase

pjoin = os.path.join

from unittest.mock import patch

import requests
from tornado.ioloop import IOLoop
import zmq

import jupyter_core.paths
from traitlets.config import Config
from ..notebookapp import NotebookApp, urlencode_unix_socket
from ..utils import url_path_join
from ipython_genutils.tempdir import TemporaryDirectory

MAX_WAITTIME = 30   # seconds to wait for notebook server to start
POLL_INTERVAL = 0.1 # time between attempts

# TimeoutError is a builtin on Python 3. This can be removed when we stop
# supporting Python 2.
class TimeoutError(Exception):
    pass

class NotebookTestBase(TestCase):
    """A base class for tests that need a running notebook.

    This create some empty config and runtime directories
    and then starts the notebook server with them.
    """

    port = 12341
    config = None
    # run with a base URL that would be escaped,
    # to test that we don't double-escape URLs
    url_prefix = '/a%40b/'

    @classmethod
    def wait_until_alive(cls):
        """Wait for the server to be alive"""
        url = cls.base_url() + 'api/contents'
        for _ in range(int(MAX_WAITTIME/POLL_INTERVAL)):
            try:
                cls.fetch_url(url)
            except ModuleNotFoundError as error:
                # Errors that should be immediately thrown back to caller
                raise error
            except Exception as e:
                if not cls.notebook_thread.is_alive():
                    raise RuntimeError("The notebook server failed to start") from e
                time.sleep(POLL_INTERVAL)
            else:
                return

        raise TimeoutError("The notebook server didn't start up correctly.")

    @classmethod
    def wait_until_dead(cls):
        """Wait for the server process to terminate after shutdown"""
        cls.notebook_thread.join(timeout=MAX_WAITTIME)
        if cls.notebook_thread.is_alive():
            raise TimeoutError("Undead notebook server")

    @classmethod
    def auth_headers(cls):
        headers = {}
        if cls.token:
            headers['Authorization'] = f'token {cls.token}'
        return headers

    @staticmethod
    def fetch_url(url):
        return requests.get(url)

    @classmethod
    def request(cls, verb, path, **kwargs):
        """Send a request to my server

        with authentication and everything.
        """
        headers = kwargs.setdefault('headers', {})
        headers.update(cls.auth_headers())
        response = requests.request(verb,
            url_path_join(cls.base_url(), path),
            **kwargs)
        return response

    @classmethod
    def get_patch_env(cls):
        return {
            'HOME': cls.home_dir,
            'PYTHONPATH': os.pathsep.join(sys.path),
            'IPYTHONDIR': pjoin(cls.home_dir, '.ipython'),
            'JUPYTER_NO_CONFIG': '1', # needed in the future
            'JUPYTER_CONFIG_DIR' : cls.config_dir,
            'JUPYTER_DATA_DIR' : cls.data_dir,
            'JUPYTER_RUNTIME_DIR': cls.runtime_dir,
        }

    @classmethod
    def get_argv(cls):
        return []

    @classmethod
    def get_bind_args(cls):
        return dict(port=cls.port)

    @classmethod
    def setup_class(cls):
        cls.tmp_dir = TemporaryDirectory()
        def tmp(*parts):
            path = os.path.join(cls.tmp_dir.name, *parts)
            try:
                os.makedirs(path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            return path

        cls.home_dir = tmp('home')
        data_dir = cls.data_dir = tmp('data')
        config_dir = cls.config_dir = tmp('config')
        runtime_dir = cls.runtime_dir = tmp('runtime')
        cls.notebook_dir = tmp('notebooks')
        cls.env_patch = patch.dict('os.environ', cls.get_patch_env())
        cls.env_patch.start()
        # Patch systemwide & user-wide data & config directories, to isolate
        # the tests from oddities of the local setup. But leave Python env
        # locations alone, so data files for e.g. nbconvert are accessible.
        # If this isolation isn't sufficient, you may need to run the tests in
        # a virtualenv or conda env.
        cls.path_patch = patch.multiple(
            jupyter_core.paths,
            SYSTEM_JUPYTER_PATH=[tmp('share', 'jupyter')],
            SYSTEM_CONFIG_PATH=[tmp('etc', 'jupyter')],
        )
        cls.path_patch.start()

        config = cls.config or Config()
        config.NotebookNotary.db_file = ':memory:'

        cls.token = hexlify(os.urandom(4)).decode('ascii')

        started = Event()
        def start_thread():
            try:
                bind_args = cls.get_bind_args()
                app = cls.notebook = NotebookApp(
                    port_retries=0,
                    open_browser=False,
                    config_dir=cls.config_dir,
                    data_dir=cls.data_dir,
                    runtime_dir=cls.runtime_dir,
                    notebook_dir=cls.notebook_dir,
                    base_url=cls.url_prefix,
                    config=config,
                    allow_root=True,
                    token=cls.token,
                    **bind_args
                )
                if "asyncio" in sys.modules:
                    app._init_asyncio_patch()
                    import asyncio

                    asyncio.set_event_loop(asyncio.new_event_loop())
                    # Patch the current loop in order to match production
                    # behavior
                    import nest_asyncio

                    nest_asyncio.apply()
                # don't register signal handler during tests
                app.init_signal = lambda : None
                # clear log handlers and propagate to root for nose to capture it
                # needs to be redone after initialize, which reconfigures logging
                app.log.propagate = True
                app.log.handlers = []
                app.initialize(argv=cls.get_argv())
                app.log.propagate = True
                app.log.handlers = []
                loop = IOLoop.current()
                loop.add_callback(started.set)
                app.start()
            finally:
                # set the event, so failure to start doesn't cause a hang
                started.set()
                app.session_manager.close()
        cls.notebook_thread = Thread(target=start_thread)
        cls.notebook_thread.daemon = True
        cls.notebook_thread.start()
        started.wait()
        cls.wait_until_alive()

    @classmethod
    def teardown_class(cls):
        cls.notebook.stop()
        cls.wait_until_dead()
        cls.env_patch.stop()
        cls.path_patch.stop()
        cls.tmp_dir.cleanup()
        # cleanup global zmq Context, to ensure we aren't leaving dangling sockets
        def cleanup_zmq():
            zmq.Context.instance().term()
        t = Thread(target=cleanup_zmq)
        t.daemon = True
        t.start()
        t.join(5) # give it a few seconds to clean up (this should be immediate)
        # if term never returned, there's zmq stuff still open somewhere, so shout about it.
        if t.is_alive():
            raise RuntimeError("Failed to teardown zmq Context, open sockets likely left lying around.")

    @classmethod
    def base_url(cls):
        return f'http://localhost:{cls.port}{cls.url_prefix}'


class UNIXSocketNotebookTestBase(NotebookTestBase):
    # Rely on `/tmp` to avoid any Linux socket length max buffer
    # issues. Key on PID for process-wise concurrency.
    sock = f'/tmp/.notebook.{os.getpid()}.sock'

    @classmethod
    def get_bind_args(cls):
        return dict(sock=cls.sock)

    @classmethod
    def base_url(cls):
        return f'{urlencode_unix_socket(cls.sock)}{cls.url_prefix}'

    @staticmethod
    def fetch_url(url):
        # Lazily import so it is not required at the module level
        if os.name != 'nt':
            import requests_unixsocket
        with requests_unixsocket.monkeypatch():
            return requests.get(url)


@contextmanager
def assert_http_error(status, msg=None):
    try:
        yield
    except requests.HTTPError as e:
        real_status = e.response.status_code
        assert real_status == status, \
            f"Expected status {status}, got {real_status}"
        if msg:
            assert msg in str(e), e
    else:
        assert False, "Expected HTTP error status"
