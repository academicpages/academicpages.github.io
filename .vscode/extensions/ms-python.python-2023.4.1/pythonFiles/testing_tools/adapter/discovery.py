# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from __future__ import absolute_import, print_function

import re

from .util import fix_fileid, DIRNAME, NORMCASE
from .info import ParentInfo


FILE_ID_RE = re.compile(
    r"""
        ^
        (?:
          ( .* [.] (?: py | txt ) \b ) # .txt for doctest files
          ( [^.] .* )?
          )
        $
        """,
    re.VERBOSE,
)


def fix_nodeid(
    nodeid,
    kind,
    rootdir=None,
    # *,
    _fix_fileid=fix_fileid,
):
    if not nodeid:
        raise ValueError("missing nodeid")
    if nodeid == ".":
        return nodeid

    fileid = nodeid
    remainder = ""
    if kind not in ("folder", "file"):
        m = FILE_ID_RE.match(nodeid)
        if m:
            fileid, remainder = m.groups()
        elif len(nodeid) > 1:
            fileid = nodeid[:2]
            remainder = nodeid[2:]
    fileid = _fix_fileid(fileid, rootdir)
    return fileid + (remainder or "")


class DiscoveredTests(object):
    """A container for the discovered tests and their parents."""

    def __init__(self):
        self.reset()

    def __len__(self):
        return len(self._tests)

    def __getitem__(self, index):
        return self._tests[index]

    @property
    def parents(self):
        return sorted(
            self._parents.values(),
            # Sort by (name, id).
            key=lambda p: (NORMCASE(p.root or p.name), p.id),
        )

    def reset(self):
        """Clear out any previously discovered tests."""
        self._parents = {}
        self._tests = []

    def add_test(self, test, parents):
        """Add the given test and its parents."""
        parentid = self._ensure_parent(test.path, parents)
        # Updating the parent ID and the test ID aren't necessary if the
        # provided test and parents (from the test collector) are
        # properly generated.  However, we play it safe here.
        test = test._replace(
            # Clean up the ID.
            id=fix_nodeid(test.id, "test", test.path.root),
            parentid=parentid,
        )
        self._tests.append(test)

    def _ensure_parent(
        self,
        path,
        parents,
        # *,
        _dirname=DIRNAME,
    ):
        rootdir = path.root
        relpath = path.relfile

        _parents = iter(parents)
        nodeid, name, kind = next(_parents)
        # As in add_test(), the node ID *should* already be correct.
        nodeid = fix_nodeid(nodeid, kind, rootdir)
        _parentid = nodeid
        for parentid, parentname, parentkind in _parents:
            # As in add_test(), the parent ID *should* already be correct.
            parentid = fix_nodeid(parentid, kind, rootdir)
            if kind in ("folder", "file"):
                info = ParentInfo(nodeid, kind, name, rootdir, relpath, parentid)
                relpath = _dirname(relpath)
            else:
                info = ParentInfo(nodeid, kind, name, rootdir, None, parentid)
            self._parents[(rootdir, nodeid)] = info
            nodeid, name, kind = parentid, parentname, parentkind
        assert nodeid == "."
        info = ParentInfo(nodeid, kind, name=rootdir)
        self._parents[(rootdir, nodeid)] = info

        return _parentid
