# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from __future__ import print_function

import json


def report_discovered(
    tests,
    parents,
    # *,
    pretty=False,
    simple=False,
    _send=print,
    **_ignored
):
    """Serialize the discovered tests and write to stdout."""
    if simple:
        data = [
            {
                "id": test.id,
                "name": test.name,
                "testroot": test.path.root,
                "relfile": test.path.relfile,
                "lineno": test.lineno,
                "testfunc": test.path.func,
                "subtest": test.path.sub or None,
                "markers": test.markers or [],
            }
            for test in tests
        ]
    else:
        byroot = {}
        for parent in parents:
            rootdir = parent.name if parent.root is None else parent.root
            try:
                root = byroot[rootdir]
            except KeyError:
                root = byroot[rootdir] = {
                    "id": rootdir,
                    "parents": [],
                    "tests": [],
                }
            if not parent.root:
                root["id"] = parent.id
                continue
            root["parents"].append(
                {
                    # "id" must match what the testing framework recognizes.
                    "id": parent.id,
                    "kind": parent.kind,
                    "name": parent.name,
                    "parentid": parent.parentid,
                }
            )
            if parent.relpath is not None:
                root["parents"][-1]["relpath"] = parent.relpath
        for test in tests:
            # We are guaranteed that the parent was added.
            root = byroot[test.path.root]
            testdata = {
                # "id" must match what the testing framework recognizes.
                "id": test.id,
                "name": test.name,
                # TODO: Add a "kind" field
                #  (e.g. "unittest", "function", "doctest")
                "source": test.source,
                "markers": test.markers or [],
                "parentid": test.parentid,
            }
            root["tests"].append(testdata)
        data = [
            {
                "rootid": byroot[root]["id"],
                "root": root,
                "parents": byroot[root]["parents"],
                "tests": byroot[root]["tests"],
            }
            for root in sorted(byroot)
        ]

    kwargs = {}
    if pretty:
        # human-formatted
        kwargs = dict(
            sort_keys=True,
            indent=4,
            separators=(",", ": "),
            # ...
        )
    serialized = json.dumps(data, **kwargs)

    _send(serialized)
