import os
import shutil
import sys
import time
from subprocess import PIPE
from subprocess import Popen
from tempfile import mkdtemp


def _launch(extra_env):
    env = os.environ.copy()
    env.update(extra_env)
    return Popen(
        [sys.executable, "-c", "from jupyter_client.kernelapp import main; main()"],
        env=env,
        stderr=PIPE,
    )


WAIT_TIME = 10
POLL_FREQ = 10


def test_kernelapp_lifecycle():
    # Check that 'jupyter kernel' starts and terminates OK.
    runtime_dir = mkdtemp()
    startup_dir = mkdtemp()
    started = os.path.join(startup_dir, "started")
    try:
        p = _launch(
            {
                "JUPYTER_RUNTIME_DIR": runtime_dir,
                "JUPYTER_CLIENT_TEST_RECORD_STARTUP_PRIVATE": started,
            }
        )
        # Wait for start
        for _ in range(WAIT_TIME * POLL_FREQ):
            if os.path.isfile(started):
                break
            time.sleep(1 / POLL_FREQ)
        else:
            raise AssertionError("No started file created in {} seconds".format(WAIT_TIME))

        # Connection file should be there by now
        for _ in range(WAIT_TIME * POLL_FREQ):
            files = os.listdir(runtime_dir)
            if files:
                break
            time.sleep(1 / POLL_FREQ)
        else:
            raise AssertionError("No connection file created in {} seconds".format(WAIT_TIME))
        assert len(files) == 1
        cf = files[0]
        assert cf.startswith("kernel")
        assert cf.endswith(".json")

        # Send SIGTERM to shut down
        time.sleep(1)
        p.terminate()
        _, stderr = p.communicate(timeout=WAIT_TIME)
        assert cf in stderr.decode("utf-8", "replace")
    finally:
        shutil.rmtree(runtime_dir)
        shutil.rmtree(startup_dir)
