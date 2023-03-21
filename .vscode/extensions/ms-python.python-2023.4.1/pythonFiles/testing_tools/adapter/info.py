# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from collections import namedtuple


class SingleTestPath(namedtuple("TestPath", "root relfile func sub")):
    """Where to find a single test."""

    def __new__(cls, root, relfile, func, sub=None):
        self = super(SingleTestPath, cls).__new__(
            cls,
            str(root) if root else None,
            str(relfile) if relfile else None,
            str(func) if func else None,
            [str(s) for s in sub] if sub else None,
        )
        return self

    def __init__(self, *args, **kwargs):
        if self.root is None:
            raise TypeError("missing id")
        if self.relfile is None:
            raise TypeError("missing kind")
        # self.func may be None (e.g. for doctests).
        # self.sub may be None.


class ParentInfo(namedtuple("ParentInfo", "id kind name root relpath parentid")):
    KINDS = ("folder", "file", "suite", "function", "subtest")

    def __new__(cls, id, kind, name, root=None, relpath=None, parentid=None):
        self = super(ParentInfo, cls).__new__(
            cls,
            id=str(id) if id else None,
            kind=str(kind) if kind else None,
            name=str(name) if name else None,
            root=str(root) if root else None,
            relpath=str(relpath) if relpath else None,
            parentid=str(parentid) if parentid else None,
        )
        return self

    def __init__(self, *args, **kwargs):
        if self.id is None:
            raise TypeError("missing id")
        if self.kind is None:
            raise TypeError("missing kind")
        if self.kind not in self.KINDS:
            raise ValueError("unsupported kind {!r}".format(self.kind))
        if self.name is None:
            raise TypeError("missing name")
        if self.root is None:
            if self.parentid is not None or self.kind != "folder":
                raise TypeError("missing root")
            if self.relpath is not None:
                raise TypeError("unexpected relpath {}".format(self.relpath))
        elif self.parentid is None:
            raise TypeError("missing parentid")
        elif self.relpath is None and self.kind in ("folder", "file"):
            raise TypeError("missing relpath")


class SingleTestInfo(
    namedtuple("TestInfo", "id name path source markers parentid kind")
):
    """Info for a single test."""

    MARKERS = ("skip", "skip-if", "expected-failure")
    KINDS = ("function", "doctest")

    def __new__(cls, id, name, path, source, markers, parentid, kind="function"):
        self = super(SingleTestInfo, cls).__new__(
            cls,
            str(id) if id else None,
            str(name) if name else None,
            path or None,
            str(source) if source else None,
            [str(marker) for marker in markers or ()],
            str(parentid) if parentid else None,
            str(kind) if kind else None,
        )
        return self

    def __init__(self, *args, **kwargs):
        if self.id is None:
            raise TypeError("missing id")
        if self.name is None:
            raise TypeError("missing name")
        if self.path is None:
            raise TypeError("missing path")
        if self.source is None:
            raise TypeError("missing source")
        else:
            srcfile, _, lineno = self.source.rpartition(":")
            if not srcfile or not lineno or int(lineno) < 0:
                raise ValueError("bad source {!r}".format(self.source))
        if self.markers:
            badmarkers = [m for m in self.markers if m not in self.MARKERS]
            if badmarkers:
                raise ValueError("unsupported markers {!r}".format(badmarkers))
        if self.parentid is None:
            raise TypeError("missing parentid")
        if self.kind is None:
            raise TypeError("missing kind")
        elif self.kind not in self.KINDS:
            raise ValueError("unsupported kind {!r}".format(self.kind))

    @property
    def root(self):
        return self.path.root

    @property
    def srcfile(self):
        return self.source.rpartition(":")[0]

    @property
    def lineno(self):
        return int(self.source.rpartition(":")[-1])
