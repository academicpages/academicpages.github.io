"""Read and write notebooks in JSON format."""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import copy
import json

from .nbbase import from_dict
from .rwbase import (
    NotebookReader,
    NotebookWriter,
    rejoin_lines,
    split_lines,
    strip_transient,
)


class BytesEncoder(json.JSONEncoder):
    """A JSON encoder that accepts b64 (and other *ascii*) bytestrings."""

    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode("ascii")
        return json.JSONEncoder.default(self, obj)


class JSONReader(NotebookReader):
    def reads(self, s, **kwargs):
        nb = json.loads(s, **kwargs)
        nb = self.to_notebook(nb, **kwargs)
        nb = strip_transient(nb)
        return nb

    def to_notebook(self, d, **kwargs):
        return rejoin_lines(from_dict(d))


class JSONWriter(NotebookWriter):
    def writes(self, nb, **kwargs):
        kwargs["cls"] = BytesEncoder
        kwargs["indent"] = 1
        kwargs["sort_keys"] = True
        kwargs["separators"] = (",", ": ")
        nb = copy.deepcopy(nb)
        nb = strip_transient(nb)
        if kwargs.pop("split_lines", True):
            nb = split_lines(nb)
        return json.dumps(nb, **kwargs)


_reader = JSONReader()
_writer = JSONWriter()

reads = _reader.reads
read = _reader.read
to_notebook = _reader.to_notebook
write = _writer.write
writes = _writer.writes
