# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys


def parse_argv():
    """Parses arguments for use with the test launcher.
    Arguments are:
    1. Working directory.
    2. Test runner `pytest`
    3. Rest of the arguments are passed into the test runner.
    """
    cwd = sys.argv[1]
    testRunner = sys.argv[2]
    args = sys.argv[3:]

    return (cwd, testRunner, args)


def run(cwd, testRunner, args):
    """Runs the test
    cwd -- the current directory to be set
    testRunner -- test runner to be used `pytest`
    args -- arguments passed into the test runner
    """

    sys.path[0] = os.getcwd()
    os.chdir(cwd)

    try:
        if testRunner == "pytest":
            import pytest

            pytest.main(args)
        sys.exit(0)
    finally:
        pass


if __name__ == "__main__":
    cwd, testRunner, args = parse_argv()
    run(cwd, testRunner, args)
