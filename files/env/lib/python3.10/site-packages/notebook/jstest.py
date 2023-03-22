"""Notebook Javascript Test Controller

This module runs one or more subprocesses which will actually run the Javascript
test suite.
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import argparse
import json
import multiprocessing.pool
import os
import re
import requests
import signal
import sys
import subprocess
import time
from io import BytesIO
from threading import Thread, Lock, Event

from unittest.mock import patch

from jupyter_core.paths import jupyter_runtime_dir
from ipython_genutils.py3compat import bytes_to_str, which
from notebook._sysinfo import get_sys_info
from ipython_genutils.tempdir import TemporaryDirectory

from subprocess import TimeoutExpired
def popen_wait(p, timeout):
    return p.wait(timeout)

NOTEBOOK_SHUTDOWN_TIMEOUT = 10

have = {}
have['casperjs'] = bool(which('casperjs'))
have['phantomjs'] = bool(which('phantomjs'))
have['slimerjs'] = bool(which('slimerjs'))

class StreamCapturer(Thread):
    daemon = True  # Don't hang if main thread crashes
    started = False
    def __init__(self, echo=False):
        super().__init__()
        self.echo = echo
        self.streams = []
        self.buffer = BytesIO()
        self.readfd, self.writefd = os.pipe()
        self.buffer_lock = Lock()
        self.stop = Event()

    def run(self):
        self.started = True

        while not self.stop.is_set():
            chunk = os.read(self.readfd, 1024)

            with self.buffer_lock:
                self.buffer.write(chunk)
            if self.echo:
                sys.stdout.write(bytes_to_str(chunk))

        os.close(self.readfd)
        os.close(self.writefd)

    def reset_buffer(self):
        with self.buffer_lock:
            self.buffer.truncate(0)
            self.buffer.seek(0)

    def get_buffer(self):
        with self.buffer_lock:
            return self.buffer.getvalue()

    def ensure_started(self):
        if not self.started:
            self.start()

    def halt(self):
        """Safely stop the thread."""
        if not self.started:
            return

        self.stop.set()
        os.write(self.writefd, b'\0')  # Ensure we're not locked in a read()
        self.join()


class TestController:
    """Run tests in a subprocess
    """
    #: str, test group to be executed.
    section = None
    #: list, command line arguments to be executed
    cmd = None
    #: dict, extra environment variables to set for the subprocess
    env = None
    #: list, TemporaryDirectory instances to clear up when the process finishes
    dirs = None
    #: subprocess.Popen instance
    process = None
    #: str, process stdout+stderr
    stdout = None

    def __init__(self):
        self.cmd = []
        self.env = {}
        self.dirs = []

    def setup(self):
        """Create temporary directories etc.

        This is only called when we know the test group will be run. Things
        created here may be cleaned up by self.cleanup().
        """
        pass

    def launch(self, buffer_output=False, capture_output=False):
        # print('*** ENV:', self.env)  # dbg
        # print('*** CMD:', self.cmd)  # dbg
        env = os.environ.copy()
        env.update(self.env)
        if buffer_output:
            capture_output = True
        self.stdout_capturer = c = StreamCapturer(echo=not buffer_output)
        c.start()
        stdout = c.writefd if capture_output else None
        stderr = subprocess.STDOUT if capture_output else None
        self.process = subprocess.Popen(self.cmd, stdout=stdout,
                stderr=stderr, env=env)

    def wait(self):
        self.process.wait()
        self.stdout_capturer.halt()
        self.stdout = self.stdout_capturer.get_buffer()
        return self.process.returncode

    def print_extra_info(self):
        """Print extra information about this test run.

        If we're running in parallel and showing the concise view, this is only
        called if the test group fails. Otherwise, it's called before the test
        group is started.

        The base implementation does nothing, but it can be overridden by
        subclasses.
        """
        return

    def cleanup_process(self):
        """Cleanup on exit by killing any leftover processes."""
        subp = self.process
        if subp is None or (subp.poll() is not None):
            return  # Process doesn't exist, or is already dead.

        try:
            print(f'Cleaning up stale PID: {subp.pid}')
            subp.kill()
        except: # (OSError, WindowsError) ?
            # This is just a best effort, if we fail or the process was
            # really gone, ignore it.
            pass
        else:
            for i in range(10):
                if subp.poll() is None:
                    time.sleep(0.1)
                else:
                    break

        if subp.poll() is None:
            # The process did not die...
            print('... failed. Manual cleanup may be required.')

    def cleanup(self):
        "Kill process if it's still alive, and clean up temporary directories"
        self.cleanup_process()
        for td in self.dirs:
            td.cleanup()

    __del__ = cleanup


def get_js_test_dir():
    import notebook.tests as t
    return os.path.join(os.path.dirname(t.__file__), '')

def all_js_groups():
    import glob
    test_dir = get_js_test_dir()
    all_subdirs = glob.glob(test_dir + '[!_]*/')
    return [os.path.relpath(x, test_dir) for x in all_subdirs]

class JSController(TestController):
    """Run CasperJS tests """

    requirements =  ['casperjs']

    def __init__(self, section, xunit=True, engine='phantomjs', url=None):
        """Create new test runner."""
        TestController.__init__(self)
        self.engine = engine
        self.section = section
        self.xunit = xunit
        self.url = url
        # run with a base URL that would be escaped,
        # to test that we don't double-escape URLs
        self.base_url = '/a@b/'
        self.slimer_failure = re.compile('^FAIL.*', flags=re.MULTILINE)
        js_test_dir = get_js_test_dir()
        includes = '--includes=' + os.path.join(js_test_dir,'util.js')
        test_cases = os.path.join(js_test_dir, self.section)
        self.cmd = ['casperjs', 'test', includes, test_cases, f'--engine={self.engine}']

    def setup(self):
        self.ipydir = TemporaryDirectory()
        self.config_dir = TemporaryDirectory()
        self.nbdir = TemporaryDirectory()
        self.home = TemporaryDirectory()
        self.env = {
            'HOME': self.home.name,
            'JUPYTER_CONFIG_DIR': self.config_dir.name,
            'IPYTHONDIR': self.ipydir.name,
        }
        self.dirs.append(self.ipydir)
        self.dirs.append(self.home)
        self.dirs.append(self.config_dir)
        self.dirs.append(self.nbdir)
        os.makedirs(os.path.join(self.nbdir.name, os.path.join('sub ∂ir1', 'sub ∂ir 1a')))
        os.makedirs(os.path.join(self.nbdir.name, os.path.join('sub ∂ir2', 'sub ∂ir 1b')))

        if self.xunit:
            self.add_xunit()

        # If a url was specified, use that for the testing.
        if self.url:
            try:
                alive = requests.get(self.url).status_code == 200
            except:
                alive = False

            if alive:
                self.cmd.append(f"--url={self.url}")
            else:
                raise Exception(f'Could not reach "{self.url}".')
        else:
            # start the ipython notebook, so we get the port number
            self.server_port = 0
            self._init_server()
            if self.server_port:
                self.cmd.append(f'--url=http://localhost:{self.server_port:d}{self.base_url}')
            else:
                # don't launch tests if the server didn't start
                self.cmd = [sys.executable, '-c', 'raise SystemExit(1)']

    def add_xunit(self):
        xunit_file = os.path.abspath(self.section.replace('/','.') + '.xunit.xml')
        self.cmd.append(f'--xunit={xunit_file}')

    def launch(self, buffer_output):
        # If the engine is SlimerJS, we need to buffer the output because
        # SlimerJS does not support exit codes, so CasperJS always returns 0.
        if self.engine == 'slimerjs' and not buffer_output:
            return super().launch(capture_output=True)

        else:
            return super().launch(buffer_output=buffer_output)

    def wait(self, *pargs, **kwargs):
        """Wait for the JSController to finish"""
        ret = super().wait(*pargs, **kwargs)
        # If this is a SlimerJS controller, check the captured stdout for
        # errors.  Otherwise, just return the return code.
        if self.engine == 'slimerjs':
            stdout = bytes_to_str(self.stdout)
            if ret != 0:
                # This could still happen e.g. if it's stopped by SIGINT
                return ret
            return bool(self.slimer_failure.search(stdout))
        else:
            return ret

    def print_extra_info(self):
        print(f"Running tests with notebook directory {self.nbdir.name!r}")

    @property
    def will_run(self):
        should_run = all(have[a] for a in self.requirements + [self.engine])
        return should_run

    def _init_server(self):
        "Start the notebook server in a separate process"
        self.server_command = command = [sys.executable,
            '-m', 'notebook',
            '--no-browser',
            '--notebook-dir', self.nbdir.name,
            '--NotebookApp.token=',
            f'--NotebookApp.base_url={self.base_url}',
        ]
        # ipc doesn't work on Windows, and darwin has crazy-long temp paths,
        # which run afoul of ipc's maximum path length.
        if sys.platform.startswith('linux'):
            command.append('--KernelManager.transport=ipc')
        self.stream_capturer = c = StreamCapturer()
        c.start()
        env = os.environ.copy()
        env.update(self.env)
        self.server = subprocess.Popen(command,
            stdout = c.writefd,
            stderr = subprocess.STDOUT,
            cwd=self.nbdir.name,
            env=env,
        )
        with patch.dict('os.environ', {'HOME': self.home.name}):
            runtime_dir = jupyter_runtime_dir()
        self.server_info_file = os.path.join(
            runtime_dir,
            f'nbserver-{self.server.pid}.json'
        )
        self._wait_for_server()

    def _wait_for_server(self):
        """Wait 30 seconds for the notebook server to start"""
        for i in range(300):
            if self.server.poll() is not None:
                return self._failed_to_start()
            if os.path.exists(self.server_info_file):
                try:
                    self._load_server_info()
                except ValueError:
                    # If the server is halfway through writing the file, we may
                    # get invalid JSON; it should be ready next iteration.
                    pass
                else:
                    return
            time.sleep(0.1)
        print(
            f"Notebook server-info file never arrived: {self.server_info_file}",
            file=sys.stderr
        )

    def _failed_to_start(self):
        """Notebook server exited prematurely"""
        captured = self.stream_capturer.get_buffer().decode('utf-8', 'replace')
        print("Notebook failed to start: ", file=sys.stderr)
        print(self.server_command)
        print(captured, file=sys.stderr)

    def _load_server_info(self):
        """Notebook server started, load connection info from JSON"""
        with open(self.server_info_file) as f:
            info = json.load(f)
        self.server_port = info['port']

    def cleanup(self):
        if hasattr(self, 'server'):
            try:
                self.server.terminate()
            except OSError:
                # already dead
                pass
            # wait 10s for the server to shutdown
            try:
                popen_wait(self.server, NOTEBOOK_SHUTDOWN_TIMEOUT)
            except TimeoutExpired:
                # server didn't terminate, kill it
                try:
                    print("Failed to terminate notebook server, killing it.",
                        file=sys.stderr
                    )
                    self.server.kill()
                except OSError:
                    # already dead
                    pass
            # wait another 10s
            try:
                popen_wait(self.server, NOTEBOOK_SHUTDOWN_TIMEOUT)
            except TimeoutExpired:
                print(
                    f"Notebook server still running ({self.server_info_file})",
                    file=sys.stderr
                )

            self.stream_capturer.halt()
        TestController.cleanup(self)


def prepare_controllers(options):
    """Returns two lists of TestController instances, those to run, and those
    not to run."""
    testgroups = options.testgroups
    if not testgroups:
        testgroups = all_js_groups()

    engine = 'slimerjs' if options.slimerjs else 'phantomjs'
    c_js = [JSController(name, xunit=options.xunit, engine=engine, url=options.url) for name in testgroups]

    controllers = c_js
    to_run = [c for c in controllers if c.will_run]
    not_run = [c for c in controllers if not c.will_run]
    return to_run, not_run

def do_run(controller, buffer_output=True):
    """Setup and run a test controller.

    If buffer_output is True, no output is displayed, to avoid it appearing
    interleaved. In this case, the caller is responsible for displaying test
    output on failure.

    Returns
    -------
    controller : TestController
      The same controller as passed in, as a convenience for using map() type
      APIs.
    exitcode : int
      The exit code of the test subprocess. Non-zero indicates failure.
    """
    try:
        try:
            controller.setup()
            if not buffer_output:
                controller.print_extra_info()
            controller.launch(buffer_output=buffer_output)
        except Exception:
            import traceback
            traceback.print_exc()
            return controller, 1  # signal failure

        exitcode = controller.wait()
        return controller, exitcode

    except KeyboardInterrupt:
        return controller, -signal.SIGINT
    finally:
        controller.cleanup()

def report():
    """Return a string with a summary report of test-related variables."""
    inf = get_sys_info()
    out = []
    def _add(name, value):
        out.append((name, value))

    _add('Python version', inf['sys_version'].replace('\n',''))
    _add('sys.executable', inf['sys_executable'])
    _add('Platform', inf['platform'])

    width = max(len(n) for (n,v) in out)
    out = [f"{n:<{width}}: {v}\n" for (n, v) in out]

    avail = []
    not_avail = []

    for k, is_avail in have.items():
        if is_avail:
            avail.append(k)
        else:
            not_avail.append(k)

    if avail:
        out.append('\nTools and libraries available at test time:\n')
        avail.sort()
        out.append('   ' + ' '.join(avail)+'\n')

    if not_avail:
        out.append('\nTools and libraries NOT available at test time:\n')
        not_avail.sort()
        out.append('   ' + ' '.join(not_avail)+'\n')

    return ''.join(out)

def run_jstestall(options):
    """Run the entire Javascript test suite.

    This function constructs TestControllers and runs them in subprocesses.

    Parameters
    ----------

    All parameters are passed as attributes of the options object.

    testgroups : list of str
      Run only these sections of the test suite. If empty, run all the available
      sections.

    fast : int or None
      Run the test suite in parallel, using n simultaneous processes. If None
      is passed, one process is used per CPU core. Default 1 (i.e. sequential)

    inc_slow : bool
      Include slow tests. By default, these tests aren't run.

    slimerjs : bool
      Use slimerjs if it's installed instead of phantomjs for casperjs tests.

    url : unicode
      Address:port to use when running the JS tests.

    xunit : bool
      Produce Xunit XML output. This is written to multiple foo.xunit.xml files.

    extra_args : list
      Extra arguments to pass to the test subprocesses, e.g. '-v'
    """
    to_run, not_run = prepare_controllers(options)

    def justify(ltext, rtext, width=70, fill='-'):
        ltext += ' '
        rtext = (' ' + rtext).rjust(width - len(ltext), fill)
        return ltext + rtext

    # Run all test runners, tracking execution time
    failed = []
    t_start = time.time()

    print()
    if options.fast == 1:
        # This actually means sequential, i.e. with 1 job
        for controller in to_run:
            print('Test group:', controller.section)
            sys.stdout.flush()  # Show in correct order when output is piped
            controller, res = do_run(controller, buffer_output=False)
            if res:
                failed.append(controller)
                if res == -signal.SIGINT:
                    print("Interrupted")
                    break
            print()

    else:
        # Run tests concurrently
        try:
            pool = multiprocessing.pool.ThreadPool(options.fast)
            for (controller, res) in pool.imap_unordered(do_run, to_run):
                res_string = 'OK' if res == 0 else 'FAILED'
                print(justify('Test group: ' + controller.section, res_string))
                if res:
                    controller.print_extra_info()
                    print(bytes_to_str(controller.stdout))
                    failed.append(controller)
                    if res == -signal.SIGINT:
                        print("Interrupted")
                        break
        except KeyboardInterrupt:
            return

    for controller in not_run:
        print(justify('Test group: ' + controller.section, 'NOT RUN'))

    t_end = time.time()
    t_tests = t_end - t_start
    nrunners = len(to_run)
    nfail = len(failed)
    # summarize results
    print('_'*70)
    print('Test suite completed for system with the following information:')
    print(report())
    took = f"Took {t_tests:.3f}s."
    print('Status: ', end='')
    if not failed:
        print(f'OK ({nrunners} test groups).', took)
    else:
        # If anything went wrong, point out what command to rerun manually to
        # see the actual errors and individual summary
        failed_sections = [c.section for c in failed]
        print(f'ERROR - {nfail} out of {nrunners} test groups failed ({", ".join(failed_sections)}).', took)
        print()
        print('You may wish to rerun these, with:')
        print('  python -m notebook.jstest', *failed_sections)
        print()

    if failed:
        # Ensure that our exit code indicates failure
        sys.exit(1)

argparser = argparse.ArgumentParser(description='Run Jupyter Notebook Javascript tests')
argparser.add_argument('testgroups', nargs='*',
                    help='Run specified groups of tests. If omitted, run '
                    'all tests.')
argparser.add_argument('--slimerjs', action='store_true',
                    help="Use slimerjs if it's installed instead of phantomjs for casperjs tests.")
argparser.add_argument('--url', help="URL to use for the JS tests.")
argparser.add_argument('-j', '--fast', nargs='?', const=None, default=1, type=int,
                    help='Run test sections in parallel. This starts as many '
                    'processes as you have cores, or you can specify a number.')
argparser.add_argument('--xunit', action='store_true',
                    help='Produce Xunit XML results')
argparser.add_argument('--subproc-streams', default='capture',
                    help="What to do with stdout/stderr from subprocesses. "
                    "'capture' (default), 'show' and 'discard' are the options.")

def default_options():
    """Get an argparse Namespace object with the default arguments, to pass to
    :func:`run_iptestall`.
    """
    options = argparser.parse_args([])
    options.extra_args = []
    return options

def main():
    try:
        ix = sys.argv.index('--')
    except ValueError:
        to_parse = sys.argv[1:]
        extra_args = []
    else:
        to_parse = sys.argv[1:ix]
        extra_args = sys.argv[ix+1:]

    options = argparser.parse_args(to_parse)
    options.extra_args = extra_args

    run_jstestall(options)


if __name__ == '__main__':
    main()
