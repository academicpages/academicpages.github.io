# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import argparse
import enum
import inspect
import os
import pathlib
import unittest
from typing import List, Tuple, TypedDict, Union

# Types


# Inherit from str so it's JSON serializable.
class TestNodeTypeEnum(str, enum.Enum):
    class_ = "class"
    file = "file"
    folder = "folder"
    test = "test"


class TestData(TypedDict):
    name: str
    path: str
    type_: TestNodeTypeEnum
    id_: str


class TestItem(TestData):
    lineno: str
    runID: str


class TestNode(TestData):
    children: "List[TestNode | TestItem]"


# Helper functions for data retrieval.


def get_test_case(suite):
    """Iterate through a unittest test suite and return all test cases."""
    for test in suite:
        if isinstance(test, unittest.TestCase):
            yield test
        else:
            for test_case in get_test_case(test):
                yield test_case


def get_source_line(obj) -> str:
    """Get the line number of a test case start line."""
    try:
        sourcelines, lineno = inspect.getsourcelines(obj)
    except:
        try:
            # tornado-specific, see https://github.com/microsoft/vscode-python/issues/17285.
            sourcelines, lineno = inspect.getsourcelines(obj.orig_method)
        except:
            return "*"

    # Return the line number of the first line of the test case definition.
    for i, v in enumerate(sourcelines):
        if v.strip().startswith(("def", "async def")):
            return str(lineno + i)

    return "*"


# Helper functions for test tree building.


def build_test_node(path: str, name: str, type_: TestNodeTypeEnum) -> TestNode:
    """Build a test node with no children. A test node can be a folder, a file or a class."""
    ## figure out if we are folder, file, or class
    id_gen = path
    if type_ == TestNodeTypeEnum.folder or type_ == TestNodeTypeEnum.file:
        id_gen = path
    else:
        # means we have to build test node for class
        id_gen = path + "\\" + name

    return {"path": path, "name": name, "type_": type_, "children": [], "id_": id_gen}


def get_child_node(
    name: str, path: str, type_: TestNodeTypeEnum, root: TestNode
) -> TestNode:
    """Find a child node in a test tree given its name and type. If the node doesn't exist, create it."""
    try:
        result = next(
            node
            for node in root["children"]
            if node["name"] == name and node["type_"] == type_
        )
    except StopIteration:
        result = build_test_node(path, name, type_)
        root["children"].append(result)

    return result  # type:ignore


def build_test_tree(
    suite: unittest.TestSuite, test_directory: str
) -> Tuple[Union[TestNode, None], List[str]]:
    """Build a test tree from a unittest test suite.

    This function returns the test tree, and any errors found by unittest.
    If no tests were discovered, return `None` and a list of errors (if any).

    Test tree structure:
    {
        "path": <test_directory path>,
        "type": "folder",
        "name": <folder name>,
        "children": [
            { files and folders }
            ...
            {
                "path": <file path>,
                "name": filename.py,
                "type_": "file",
                "children": [
                    {
                        "path": <class path>,
                        "name": <class name>,
                        "type_": "class",
                        "children": [
                            {
                                "path": <test path>,
                                "name": <test name>,
                                "type_": "test",
                                "lineno": <line number>
                                "id_": <test case id following format in line 196>,
                            }
                        ],
                        "id_": <class path path following format after path>
                    }
                ],
                "id_": <file path>
            }
        ],
        "id_": <test_directory path>
    }
    """
    errors = []
    directory_path = pathlib.PurePath(test_directory)
    root = build_test_node(test_directory, directory_path.name, TestNodeTypeEnum.folder)

    for test_case in get_test_case(suite):
        test_id = test_case.id()
        if test_id.startswith("unittest.loader._FailedTest"):
            errors.append(str(test_case._exception))  # type: ignore
        else:
            # Get the static test path components: filename, class name and function name.
            components = test_id.split(".")
            *folders, filename, class_name, function_name = components
            py_filename = f"{filename}.py"

            current_node = root

            # Find/build nodes for the intermediate folders in the test path.
            for folder in folders:
                current_node = get_child_node(
                    folder,
                    os.fsdecode(pathlib.PurePath(current_node["path"], folder)),
                    TestNodeTypeEnum.folder,
                    current_node,
                )

            # Find/build file node.
            path_components = [test_directory] + folders + [py_filename]
            file_path = os.fsdecode(pathlib.PurePath("/".join(path_components)))
            current_node = get_child_node(
                py_filename, file_path, TestNodeTypeEnum.file, current_node
            )

            # Find/build class node.
            current_node = get_child_node(
                class_name, file_path, TestNodeTypeEnum.class_, current_node
            )

            # Get test line number.
            test_method = getattr(test_case, test_case._testMethodName)
            lineno = get_source_line(test_method)

            # Add test node.
            test_node: TestItem = {
                "name": function_name,
                "path": file_path,
                "lineno": lineno,
                "type_": TestNodeTypeEnum.test,
                "id_": file_path + "\\" + class_name + "\\" + function_name,
                "runID": test_id,
            }  # concatenate class name and function test name
            current_node["children"].append(test_node)

    if not root["children"]:
        root = None

    return root, errors


def parse_unittest_args(args: List[str]) -> Tuple[str, str, Union[str, None]]:
    """Parse command-line arguments that should be forwarded to unittest to perform discovery.

    Valid unittest arguments are: -v, -s, -p, -t and their long-form counterparts,
    however we only care about the last three.

    The returned tuple contains the following items
    - start_directory: The directory where to start discovery, defaults to .
    - pattern: The pattern to match test files, defaults to test*.py
    - top_level_directory: The top-level directory of the project, defaults to None, and unittest will use start_directory behind the scenes.
    """

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--start-directory", "-s", default=".")
    arg_parser.add_argument("--pattern", "-p", default="test*.py")
    arg_parser.add_argument("--top-level-directory", "-t", default=None)

    parsed_args, _ = arg_parser.parse_known_args(args)

    return (
        parsed_args.start_directory,
        parsed_args.pattern,
        parsed_args.top_level_directory,
    )
