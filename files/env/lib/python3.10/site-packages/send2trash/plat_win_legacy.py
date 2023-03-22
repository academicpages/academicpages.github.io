# Copyright 2017 Virgil Dupras

# This software is licensed under the "BSD" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.hardcoded.net/licenses/bsd_license

from __future__ import unicode_literals
import os.path as op
from .compat import text_type
from .util import preprocess_paths

from ctypes import (
    windll,
    Structure,
    byref,
    c_uint,
    create_unicode_buffer,
    addressof,
    GetLastError,
    FormatError,
)
from ctypes.wintypes import HWND, UINT, LPCWSTR, BOOL

kernel32 = windll.kernel32
GetShortPathNameW = kernel32.GetShortPathNameW

shell32 = windll.shell32
SHFileOperationW = shell32.SHFileOperationW


class SHFILEOPSTRUCTW(Structure):
    _fields_ = [
        ("hwnd", HWND),
        ("wFunc", UINT),
        ("pFrom", LPCWSTR),
        ("pTo", LPCWSTR),
        ("fFlags", c_uint),
        ("fAnyOperationsAborted", BOOL),
        ("hNameMappings", c_uint),
        ("lpszProgressTitle", LPCWSTR),
    ]


FO_MOVE = 1
FO_COPY = 2
FO_DELETE = 3
FO_RENAME = 4

FOF_MULTIDESTFILES = 1
FOF_SILENT = 4
FOF_NOCONFIRMATION = 16
FOF_ALLOWUNDO = 64
FOF_NOERRORUI = 1024


def prefix_and_path(path):
    r"""Guess the long-path prefix based on the kind of *path*.
    Local paths (C:\folder\file.ext) and UNC names (\\server\folder\file.ext)
    are handled.

    Return a tuple of the long-path prefix and the prefixed path.
    """
    prefix, long_path = "\\\\?\\", path

    if not path.startswith(prefix):
        if path.startswith("\\\\"):
            # Likely a UNC name
            prefix = "\\\\?\\UNC"
            long_path = prefix + path[1:]
        else:
            # Likely a local path
            long_path = prefix + path
    elif path.startswith(prefix + "UNC\\"):
        # UNC name with long-path prefix
        prefix = "\\\\?\\UNC"

    return prefix, long_path


def get_awaited_path_from_prefix(prefix, path):
    """Guess the correct path to pass to the SHFileOperationW() call.
    The long-path prefix must be removed, so we should take care of
    different long-path prefixes.
    """
    if prefix == "\\\\?\\UNC":
        # We need to prepend a backslash for UNC names, as it was removed
        # in prefix_and_path().
        return "\\" + path[len(prefix) :]
    return path[len(prefix) :]


def get_short_path_name(long_name):
    prefix, long_path = prefix_and_path(long_name)
    buf_size = GetShortPathNameW(long_path, None, 0)
    # FIX: https://github.com/hsoft/send2trash/issues/31
    # If buffer size is zero, an error has occurred.
    if not buf_size:
        err_no = GetLastError()
        raise WindowsError(err_no, FormatError(err_no), long_path)
    output = create_unicode_buffer(buf_size)
    GetShortPathNameW(long_path, output, buf_size)
    return get_awaited_path_from_prefix(prefix, output.value)


def send2trash(paths):
    paths = preprocess_paths(paths)
    # convert data type
    paths = [
        text_type(path, "mbcs") if not isinstance(path, text_type) else path
        for path in paths
    ]
    # convert to full paths
    paths = [op.abspath(path) if not op.isabs(path) else path for path in paths]
    # get short path to handle path length issues
    paths = [get_short_path_name(path) for path in paths]
    fileop = SHFILEOPSTRUCTW()
    fileop.hwnd = 0
    fileop.wFunc = FO_DELETE
    # FIX: https://github.com/hsoft/send2trash/issues/17
    # Starting in python 3.6.3 it is no longer possible to use:
    # LPCWSTR(path + '\0') directly as embedded null characters are no longer
    # allowed in strings
    # Workaround
    #  - create buffer of c_wchar[] (LPCWSTR is based on this type)
    #  - buffer is two c_wchar characters longer (double null terminator)
    #  - cast the address of the buffer to a LPCWSTR
    # NOTE: based on how python allocates memory for these types they should
    # always be zero, if this is ever not true we can go back to explicitly
    # setting the last two characters to null using buffer[index] = '\0'.
    # Additional note on another issue here, unicode_buffer expects length in
    # bytes essentially, so having multi-byte characters causes issues if just
    # passing pythons string length.  Instead of dealing with this difference we
    # just create a buffer then a new one with an extra null.  Since the non-length
    # specified version apparently stops after the first null, join with a space first.
    buffer = create_unicode_buffer(" ".join(paths))
    # convert to a single string of null terminated paths
    path_string = "\0".join(paths)
    buffer = create_unicode_buffer(path_string, len(buffer) + 1)
    fileop.pFrom = LPCWSTR(addressof(buffer))
    fileop.pTo = None
    fileop.fFlags = FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_NOERRORUI | FOF_SILENT
    fileop.fAnyOperationsAborted = 0
    fileop.hNameMappings = 0
    fileop.lpszProgressTitle = None
    result = SHFileOperationW(byref(fileop))
    if result:
        raise WindowsError(result, FormatError(result), paths)
