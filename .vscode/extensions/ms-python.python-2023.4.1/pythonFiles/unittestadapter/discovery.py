# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import argparse
import json
import os
import pathlib
import sys
import traceback
import unittest
from typing import List, Literal, Optional, Tuple, TypedDict, Union

# Add the path to pythonFiles to sys.path to find testing_tools.socket_manager.
PYTHON_FILES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PYTHON_FILES)

from testing_tools import socket_manager

# If I use from utils then there will be an import error in test_discovery.py.
from unittestadapter.utils import TestNode, build_test_tree, parse_unittest_args

# Add the lib path to sys.path to find the typing_extensions module.
sys.path.insert(0, os.path.join(PYTHON_FILES, "lib", "python"))

from typing_extensions import NotRequired

DEFAULT_PORT = "45454"


def parse_discovery_cli_args(args: List[str]) -> Tuple[int, Union[str, None]]:
    """Parse command-line arguments that should be processed by the script.

    So far this includes the port number that it needs to connect to, and the uuid passed by the TS side.
    The port is passed to the discovery.py script when it is executed, and
    defaults to DEFAULT_PORT if it can't be parsed.
    The uuid should be passed to the discovery.py script when it is executed, and defaults to None if it can't be parsed.
    If the arguments appear several times, the value returned by parse_cli_args will be the value of the last argument.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--port", default=DEFAULT_PORT)
    arg_parser.add_argument("--uuid")
    parsed_args, _ = arg_parser.parse_known_args(args)

    return int(parsed_args.port), parsed_args.uuid


class PayloadDict(TypedDict):
    cwd: str
    status: Literal["success", "error"]
    tests: NotRequired[TestNode]
    errors: NotRequired[List[str]]


def discover_tests(
    start_dir: str, pattern: str, top_level_dir: Optional[str], uuid: Optional[str]
) -> PayloadDict:
    """Returns a dictionary containing details of the discovered tests.

    The returned dict has the following keys:

    - cwd: Absolute path to the test start directory;
    - uuid: UUID sent by the caller of the Python script, that needs to be sent back as an integrity check;
    - status: Test discovery status, can be "success" or "error";
    - tests: Discoverered tests if any, not present otherwise. Note that the status can be "error" but the payload can still contain tests;
    - errors: Discovery errors if any, not present otherwise.

    Payload format for a successful discovery:
    {
        "status": "success",
        "cwd": <test discovery directory>,
        "tests": <test tree>
    }

    Payload format for a successful discovery with no tests:
    {
        "status": "success",
        "cwd": <test discovery directory>,
    }

    Payload format when there are errors:
    {
        "cwd": <test discovery directory>
        "errors": [list of errors]
        "status": "error",
    }
    """
    cwd = os.path.abspath(start_dir)
    payload: PayloadDict = {"cwd": cwd, "status": "success"}
    tests = None
    errors: List[str] = []

    try:
        loader = unittest.TestLoader()
        suite = loader.discover(start_dir, pattern, top_level_dir)

        tests, errors = build_test_tree(suite, cwd)  # test tree built succesfully here.

    except Exception:
        errors.append(traceback.format_exc())

    if tests is not None:
        payload["tests"] = tests

    if len(errors):
        payload["status"] = "error"
        payload["errors"] = errors

    return payload


if __name__ == "__main__":
    # Get unittest discovery arguments.
    argv = sys.argv[1:]
    index = argv.index("--udiscovery")

    start_dir, pattern, top_level_dir = parse_unittest_args(argv[index + 1 :])

    # Perform test discovery.
    port, uuid = parse_discovery_cli_args(argv[:index])
    payload = discover_tests(start_dir, pattern, top_level_dir, uuid)

    # Build the request data (it has to be a POST request or the Node side will not process it), and send it.
    addr = ("localhost", port)
    with socket_manager.SocketManager(addr) as s:
        data = json.dumps(payload)
        request = f"""POST / HTTP/1.1
Host: localhost:{port}
Content-Length: {len(data)}
Content-Type: application/json
Request-uuid: {uuid}

{data}"""
        result = s.socket.sendall(request.encode("utf-8"))  # type: ignore
