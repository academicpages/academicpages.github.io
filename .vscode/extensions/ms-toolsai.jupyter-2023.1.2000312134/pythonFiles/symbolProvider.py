# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import ast
import json
import sys


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.symbols = {"classes": [], "methods": [], "functions": []}

    def visit_Module(self, node):
        self.visitChildren(node)

    def visitChildren(self, node, namespace=""):
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                self.visitDef(child, namespace)
            if isinstance(child, ast.ClassDef):
                self.visitClassDef(child, namespace)
            try:
                if isinstance(child, ast.AsyncFunctionDef):
                    self.visitDef(child, namespace)
            except Exception:
                pass

    def visitDef(self, node, namespace=""):
        end_position = self.getEndPosition(node)
        symbol = "functions" if namespace == "" else "methods"
        self.symbols[symbol].append(self.getDataObject(node, namespace))

    def visitClassDef(self, node, namespace=""):
        end_position = self.getEndPosition(node)
        self.symbols["classes"].append(self.getDataObject(node, namespace))

        if len(namespace) > 0:
            namespace = "{0}::{1}".format(namespace, node.name)
        else:
            namespace = node.name
        self.visitChildren(node, namespace)

    def getDataObject(self, node, namespace=""):
        end_position = self.getEndPosition(node)
        return {
            "namespace": namespace,
            "name": node.name,
            "range": {
                "start": {"line": node.lineno - 1, "character": node.col_offset},
                "end": {"line": end_position[0], "character": end_position[1]},
            },
        }

    def getEndPosition(self, node):
        if not hasattr(node, "body") or len(node.body) == 0:
            return (node.lineno - 1, node.col_offset)
        return self.getEndPosition(node.body[-1])


def provide_symbols(source):
    """Provides a list of all symbols in provided code.

    The list comprises of 3-item tuples that contain the starting line number,
    ending line number and whether the statement is a single line.

    """
    tree = ast.parse(source)
    visitor = Visitor()
    visitor.visit(tree)
    sys.stdout.write(json.dumps(visitor.symbols))
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        contents = sys.argv[2]
    else:
        with open(sys.argv[1], "r") as source:
            contents = source.read()

    try:
        default_encoding = sys.getdefaultencoding()
        encoded_contents = contents.encode(default_encoding, "surrogateescape")
        contents = encoded_contents.decode(default_encoding, "replace")
    except (UnicodeError, LookupError):
        pass
    if isinstance(contents, bytes):
        contents = contents.decode("utf8")
    provide_symbols(contents)
