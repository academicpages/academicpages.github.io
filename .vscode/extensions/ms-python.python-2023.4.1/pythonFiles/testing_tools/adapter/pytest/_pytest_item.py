# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
During "collection", pytest finds all the tests it supports.  These are
called "items".  The process is top-down, mostly tracing down through
the file system.  Aside from its own machinery, pytest supports hooks
that find tests.  Effectively, pytest starts with a set of "collectors";
objects that can provide a list of tests and sub-collectors.  All
collectors in the resulting tree are visited and the tests aggregated.
For the most part, each test's (and collector's) parent is identified
as the collector that collected it.

Collectors and items are collectively identified as "nodes".  The pytest
API relies on collector and item objects providing specific methods and
attributes.  In addition to corresponding base classes, pytest provides
a number of concrete implementations.

The following are the known pytest node types:

  Node
      Collector
          FSCollector
              Session (the top-level collector)
              File
                  Module
                      Package
                      DoctestTextfile
                      DoctestModule
          PyCollector
              (Module)
                  (...)
              Class
                  UnitTestCase
              Instance
      Item
          Function
              TestCaseFunction
          DoctestItem

Here are the unique attrs for those classes:

  Node
      name
      nodeid (readonly)
      config
      session
      (parent) - the parent node
      (fspath) - the file from which the node was collected
      ----
      own_marksers - explicit markers (e.g. with @pytest.mark())
      keywords
      extra_keyword_matches

  Item
      location - where the actual test source code is: (relfspath, lno, fullname)
      user_properties

  PyCollector
      module
      class
      instance
      obj

  Function
      module
      class
      instance
      obj
      function
      (callspec)
      (fixturenames)
      funcargs
      originalname - w/o decorations, e.g. [...] for parameterized

  DoctestItem
      dtest
      obj

When parsing an item, we make use of the following attributes:

* name
* nodeid
* __class__
    + __name__
* fspath
* location
* function
    + __name__
    + __code__
    + __closure__
* own_markers
"""

from __future__ import absolute_import, print_function

import sys

import _pytest.doctest
import _pytest.unittest
import pytest

from ..info import SingleTestInfo, SingleTestPath
from ..util import NORMCASE, PATH_SEP, fix_fileid


def should_never_reach_here(item, **extra):
    """Indicates a code path we should never reach."""
    print("The Python extension has run into an unexpected situation")
    print("while processing a pytest node during test discovery.  Please")
    print("Please open an issue at:")
    print("  https://github.com/microsoft/vscode-python/issues")
    print("and paste the following output there.")
    print()
    for field, info in _summarize_item(item):
        print("{}: {}".format(field, info))
    if extra:
        print()
        print("extra info:")
        for name, info in extra.items():
            print("{:10}".format(name + ":"), end="")
            if isinstance(info, str):
                print(info)
            else:
                try:
                    print(*info)
                except TypeError:
                    print(info)
    print()
    print("traceback:")
    import traceback

    traceback.print_stack()

    msg = "Unexpected pytest node (see printed output)."
    exc = NotImplementedError(msg)
    exc.item = item
    return exc


def parse_item(
    item,
    # *,
    _get_item_kind=(lambda *a: _get_item_kind(*a)),
    _parse_node_id=(lambda *a: _parse_node_id(*a)),
    _split_fspath=(lambda *a: _split_fspath(*a)),
    _get_location=(lambda *a: _get_location(*a)),
):
    """Return (TestInfo, [suite ID]) for the given item.

    The suite IDs, if any, are in parent order with the item's direct
    parent at the beginning.  The parent of the last suite ID (or of
    the test if there are no suites) is the file ID, which corresponds
    to TestInfo.path.

    """
    # _debug_item(item, showsummary=True)
    kind, _ = _get_item_kind(item)
    # Skip plugin generated tests
    if kind is None:
        return None, None

    if kind == "function" and item.originalname and item.originalname != item.name:
        # split out parametrized decorations `node[params]`) before parsing
        # and manually attach parametrized portion back in when done.
        parameterized = item.name[len(item.originalname) :]
        (parentid, parents, fileid, testfunc, _) = _parse_node_id(
            item.nodeid[: -len(parameterized)], kind
        )
        nodeid = "{}{}".format(parentid, parameterized)
        parents = [(parentid, item.originalname, kind)] + parents
        name = parameterized[1:-1] or "<empty>"
    else:
        (nodeid, parents, fileid, testfunc, parameterized) = _parse_node_id(
            item.nodeid, kind
        )
        name = item.name

    # Note: testfunc does not necessarily match item.function.__name__.
    # This can result from importing a test function from another module.

    # Figure out the file.
    testroot, relfile = _split_fspath(str(item.fspath), fileid, item)
    location, fullname = _get_location(item, testroot, relfile)
    if kind == "function":
        if testfunc and fullname != testfunc + parameterized:
            raise should_never_reach_here(
                item,
                fullname=fullname,
                testfunc=testfunc,
                parameterized=parameterized,
                # ...
            )
    elif kind == "doctest":
        if testfunc and fullname != testfunc and fullname != "[doctest] " + testfunc:
            raise should_never_reach_here(
                item,
                fullname=fullname,
                testfunc=testfunc,
                # ...
            )
        testfunc = None

    # Sort out the parent.
    if parents:
        parentid, _, _ = parents[0]
    else:
        parentid = None

    # Sort out markers.
    #  See: https://docs.pytest.org/en/latest/reference.html#marks
    markers = set()
    for marker in getattr(item, "own_markers", []):
        if marker.name == "parameterize":
            # We've already covered these.
            continue
        elif marker.name == "skip":
            markers.add("skip")
        elif marker.name == "skipif":
            markers.add("skip-if")
        elif marker.name == "xfail":
            markers.add("expected-failure")
        # We can add support for other markers as we need them?

    test = SingleTestInfo(
        id=nodeid,
        name=name,
        path=SingleTestPath(
            root=testroot,
            relfile=relfile,
            func=testfunc,
            sub=[parameterized] if parameterized else None,
        ),
        source=location,
        markers=sorted(markers) if markers else None,
        parentid=parentid,
    )
    if parents and parents[-1] == (".", None, "folder"):  # This should always be true?
        parents[-1] = (".", testroot, "folder")
    return test, parents


def _split_fspath(
    fspath,
    fileid,
    item,
    # *,
    _normcase=NORMCASE,
):
    """Return (testroot, relfile) for the given fspath.

    "relfile" will match "fileid".
    """
    # "fileid" comes from nodeid and is always relative to the testroot
    # (with a "./" prefix).  There are no guarantees about casing, so we
    # normcase just be to sure.
    relsuffix = fileid[1:]  # Drop (only) the "." prefix.
    if not _normcase(fspath).endswith(_normcase(relsuffix)):
        raise should_never_reach_here(
            item,
            fspath=fspath,
            fileid=fileid,
            # ...
        )
    testroot = fspath[: -len(fileid) + 1]  # Ignore the "./" prefix.
    relfile = "." + fspath[-len(fileid) + 1 :]  # Keep the pathsep.
    return testroot, relfile


def _get_location(
    item,
    testroot,
    relfile,
    # *,
    _matches_relfile=(lambda *a: _matches_relfile(*a)),
    _is_legacy_wrapper=(lambda *a: _is_legacy_wrapper(*a)),
    _unwrap_decorator=(lambda *a: _unwrap_decorator(*a)),
    _pathsep=PATH_SEP,
):
    """Return (loc str, fullname) for the given item."""
    # When it comes to normcase, we favor relfile (from item.fspath)
    # over item.location in this function.

    srcfile, lineno, fullname = item.location
    if _matches_relfile(srcfile, testroot, relfile):
        srcfile = relfile
    else:
        # pytest supports discovery of tests imported from other
        # modules.  This is reflected by a different filename
        # in item.location.

        if _is_legacy_wrapper(srcfile):
            srcfile = relfile
            unwrapped = _unwrap_decorator(item.function)
            if unwrapped is None:
                # It was an invalid legacy wrapper so we just say
                # "somewhere in relfile".
                lineno = None
            else:
                _srcfile, lineno = unwrapped
                if not _matches_relfile(_srcfile, testroot, relfile):
                    # For legacy wrappers we really expect the wrapped
                    # function to be in relfile.  So here we ignore any
                    # other file and just say "somewhere in relfile".
                    lineno = None
        elif _matches_relfile(srcfile, testroot, relfile):
            srcfile = relfile
        # Otherwise we just return the info from item.location as-is.

        if not srcfile.startswith("." + _pathsep):
            srcfile = "." + _pathsep + srcfile

    if lineno is None:
        lineno = -1  # i.e. "unknown"

    # from pytest, line numbers are 0-based
    location = "{}:{}".format(srcfile, int(lineno) + 1)
    return location, fullname


def _matches_relfile(
    srcfile,
    testroot,
    relfile,
    # *,
    _normcase=NORMCASE,
    _pathsep=PATH_SEP,
):
    """Return True if "srcfile" matches the given relfile."""
    testroot = _normcase(testroot)
    srcfile = _normcase(srcfile)
    relfile = _normcase(relfile)
    if srcfile == relfile:
        return True
    elif srcfile == relfile[len(_pathsep) + 1 :]:
        return True
    elif srcfile == testroot + relfile[1:]:
        return True
    else:
        return False


def _is_legacy_wrapper(
    srcfile,
    # *,
    _pathsep=PATH_SEP,
    _pyversion=sys.version_info,
):
    """Return True if the test might be wrapped.

    In Python 2 unittest's decorators (e.g. unittest.skip) do not wrap
    properly, so we must manually unwrap them.
    """
    if _pyversion > (3,):
        return False
    if (_pathsep + "unittest" + _pathsep + "case.py") not in srcfile:
        return False
    return True


def _unwrap_decorator(func):
    """Return (filename, lineno) for the func the given func wraps.

    If the wrapped func cannot be identified then return None.  Likewise
    for the wrapped filename.  "lineno" is None if it cannot be found
    but the filename could.
    """
    try:
        func = func.__closure__[0].cell_contents
    except (IndexError, AttributeError):
        return None
    else:
        if not callable(func):
            return None
        try:
            filename = func.__code__.co_filename
        except AttributeError:
            return None
        else:
            try:
                lineno = func.__code__.co_firstlineno - 1
            except AttributeError:
                return (filename, None)
            else:
                return filename, lineno


def _parse_node_id(
    testid,
    kind,
    # *,
    _iter_nodes=(lambda *a: _iter_nodes(*a)),
):
    """Return the components of the given node ID, in heirarchical order."""
    nodes = iter(_iter_nodes(testid, kind))

    testid, name, kind = next(nodes)
    parents = []
    parameterized = None
    if kind == "doctest":
        parents = list(nodes)
        fileid, _, _ = parents[0]
        return testid, parents, fileid, name, parameterized
    elif kind is None:
        fullname = None
    else:
        if kind == "subtest":
            node = next(nodes)
            parents.append(node)
            funcid, funcname, _ = node
            parameterized = testid[len(funcid) :]
        elif kind == "function":
            funcname = name
        else:
            raise should_never_reach_here(
                testid,
                kind=kind,
                # ...
            )
        fullname = funcname

    for node in nodes:
        parents.append(node)
        parentid, name, kind = node
        if kind == "file":
            fileid = parentid
            break
        elif fullname is None:
            # We don't guess how to interpret the node ID for these tests.
            continue
        elif kind == "suite":
            fullname = name + "." + fullname
        else:
            raise should_never_reach_here(
                testid,
                node=node,
                # ...
            )
    else:
        fileid = None
    parents.extend(nodes)  # Add the rest in as-is.

    return (
        testid,
        parents,
        fileid,
        fullname,
        parameterized or "",
    )


def _iter_nodes(
    testid,
    kind,
    # *,
    _normalize_test_id=(lambda *a: _normalize_test_id(*a)),
    _normcase=NORMCASE,
    _pathsep=PATH_SEP,
):
    """Yield (nodeid, name, kind) for the given node ID and its parents."""
    nodeid, testid = _normalize_test_id(testid, kind)
    if len(nodeid) > len(testid):
        testid = "." + _pathsep + testid

    parentid, _, name = nodeid.rpartition("::")
    if not parentid:
        if kind is None:
            # This assumes that plugins can generate nodes that do not
            # have a parent.  All the builtin nodes have one.
            yield (nodeid, name, kind)
            return
        # We expect at least a filename and a name.
        raise should_never_reach_here(
            nodeid,
            # ...
        )
    yield (nodeid, name, kind)

    # Extract the suites.
    while "::" in parentid:
        suiteid = parentid
        parentid, _, name = parentid.rpartition("::")
        yield (suiteid, name, "suite")

    # Extract the file and folders.
    fileid = parentid
    raw = testid[: len(fileid)]
    _parentid, _, filename = _normcase(fileid).rpartition(_pathsep)
    parentid = fileid[: len(_parentid)]
    raw, name = raw[: len(_parentid)], raw[-len(filename) :]
    yield (fileid, name, "file")
    # We're guaranteed at least one (the test root).
    while _pathsep in _normcase(parentid):
        folderid = parentid
        _parentid, _, foldername = _normcase(folderid).rpartition(_pathsep)
        parentid = folderid[: len(_parentid)]
        raw, name = raw[: len(parentid)], raw[-len(foldername) :]
        yield (folderid, name, "folder")
    # We set the actual test root later at the bottom of parse_item().
    testroot = None
    yield (parentid, testroot, "folder")


def _normalize_test_id(
    testid,
    kind,
    # *,
    _fix_fileid=fix_fileid,
    _pathsep=PATH_SEP,
):
    """Return the canonical form for the given node ID."""
    while "::()::" in testid:
        testid = testid.replace("::()::", "::")
    while ":::" in testid:
        testid = testid.replace(":::", "::")
    if kind is None:
        return testid, testid
    orig = testid

    # We need to keep the testid as-is, or else pytest won't recognize
    # it when we try to use it later (e.g. to run a test).  The only
    # exception is that we add a "./" prefix for relative paths.
    # Note that pytest always uses "/" as the path separator in IDs.
    fileid, sep, remainder = testid.partition("::")
    fileid = _fix_fileid(fileid)
    if not fileid.startswith("./"):  # Absolute "paths" not expected.
        raise should_never_reach_here(
            testid,
            fileid=fileid,
            # ...
        )
    testid = fileid + sep + remainder

    return testid, orig


def _get_item_kind(item):
    """Return (kind, isunittest) for the given item."""
    if isinstance(item, _pytest.doctest.DoctestItem):
        return "doctest", False
    elif isinstance(item, _pytest.unittest.TestCaseFunction):
        return "function", True
    elif isinstance(item, pytest.Function):
        # We *could* be more specific, e.g. "method", "subtest".
        return "function", False
    else:
        return None, False


#############################
# useful for debugging

_FIELDS = [
    "nodeid",
    "kind",
    "class",
    "name",
    "fspath",
    "location",
    "function",
    "markers",
    "user_properties",
    "attrnames",
]


def _summarize_item(item):
    if not hasattr(item, "nodeid"):
        yield "nodeid", item
        return

    for field in _FIELDS:
        try:
            if field == "kind":
                yield field, _get_item_kind(item)
            elif field == "class":
                yield field, item.__class__.__name__
            elif field == "markers":
                yield field, item.own_markers
                # yield field, list(item.iter_markers())
            elif field == "attrnames":
                yield field, dir(item)
            else:
                yield field, getattr(item, field, "<???>")
        except Exception as exc:
            yield field, "<error {!r}>".format(exc)


def _debug_item(item, showsummary=False):
    item._debugging = True
    try:
        summary = dict(_summarize_item(item))
    finally:
        item._debugging = False

    if showsummary:
        print(item.nodeid)
        for key in (
            "kind",
            "class",
            "name",
            "fspath",
            "location",
            "func",
            "markers",
            "props",
        ):
            print("  {:12} {}".format(key, summary[key]))
        print()

    return summary
