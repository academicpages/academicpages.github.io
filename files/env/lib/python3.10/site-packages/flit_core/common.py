import ast
from contextlib import contextmanager
import hashlib
import logging
import os

from pathlib import Path
import re

log = logging.getLogger(__name__)

from .versionno import normalise_version

class Module(object):
    """This represents the module/package that we are going to distribute
    """
    in_namespace_package = False
    namespace_package_name = None

    def __init__(self, name, directory=Path()):
        self.name = name

        # It must exist either as a .py file or a directory, but not both
        name_as_path = name.replace('.', os.sep)
        pkg_dir = directory / name_as_path
        py_file = directory / (name_as_path+'.py')
        src_pkg_dir = directory / 'src' / name_as_path
        src_py_file = directory / 'src' / (name_as_path+'.py')

        existing = set()
        if pkg_dir.is_dir():
            self.path = pkg_dir
            self.is_package = True
            self.prefix = ''
            existing.add(pkg_dir)
        if py_file.is_file():
            self.path = py_file
            self.is_package = False
            self.prefix = ''
            existing.add(py_file)
        if src_pkg_dir.is_dir():
            self.path = src_pkg_dir
            self.is_package = True
            self.prefix = 'src'
            existing.add(src_pkg_dir)
        if src_py_file.is_file():
            self.path = src_py_file
            self.is_package = False
            self.prefix = 'src'
            existing.add(src_py_file)

        if len(existing) > 1:
            raise ValueError(
                "Multiple files or folders could be module {}: {}"
                .format(name, ", ".join([str(p) for p in sorted(existing)]))
            )
        elif not existing:
            raise ValueError("No file/folder found for module {}".format(name))

        self.source_dir = directory / self.prefix

        if '.' in name:
            self.namespace_package_name = name.rpartition('.')[0]
            self.in_namespace_package = True

    @property
    def file(self):
        if self.is_package:
            return self.path / '__init__.py'
        else:
            return self.path

    def iter_files(self):
        """Iterate over the files contained in this module.

        Yields absolute paths - caller may want to make them relative.
        Excludes any __pycache__ and *.pyc files.
        """
        def _include(path):
            name = os.path.basename(path)
            if (name == '__pycache__') or name.endswith('.pyc'):
                return False
            return True

        if self.is_package:
            # Ensure we sort all files and directories so the order is stable
            for dirpath, dirs, files in os.walk(str(self.path)):
                for file in sorted(files):
                    full_path = os.path.join(dirpath, file)
                    if _include(full_path):
                        yield full_path

                dirs[:] = [d for d in sorted(dirs) if _include(d)]

        else:
            yield str(self.path)

class ProblemInModule(ValueError): pass
class NoDocstringError(ProblemInModule): pass
class NoVersionError(ProblemInModule): pass
class InvalidVersion(ProblemInModule): pass

class VCSError(Exception):
    def __init__(self, msg, directory):
        self.msg = msg
        self.directory = directory

    def __str__(self):
        return self.msg + ' ({})'.format(self.directory)


@contextmanager
def _module_load_ctx():
    """Preserve some global state that modules might change at import time.

    - Handlers on the root logger.
    """
    logging_handlers = logging.root.handlers[:]
    try:
        yield
    finally:
        logging.root.handlers = logging_handlers

def get_docstring_and_version_via_ast(target):
    """
    Return a tuple like (docstring, version) for the given module,
    extracted by parsing its AST.
    """
    # read as bytes to enable custom encodings
    with target.file.open('rb') as f:
        node = ast.parse(f.read())
    for child in node.body:
        # Only use the version from the given module if it's a simple
        # string assignment to __version__
        is_version_str = (
                isinstance(child, ast.Assign)
                and len(child.targets) == 1
                and isinstance(child.targets[0], ast.Name)
                and child.targets[0].id == "__version__"
                and isinstance(child.value, ast.Str)
        )
        if is_version_str:
            version = child.value.s
            break
    else:
        version = None
    return ast.get_docstring(node), version


# To ensure we're actually loading the specified file, give it a unique name to
# avoid any cached import. In normal use we'll only load one module per process,
# so it should only matter for the tests, but we'll do it anyway.
_import_i = 0


def get_docstring_and_version_via_import(target):
    """
    Return a tuple like (docstring, version) for the given module,
    extracted by importing the module and pulling __doc__ & __version__
    from it.
    """
    global _import_i
    _import_i += 1

    log.debug("Loading module %s", target.file)
    from importlib.machinery import SourceFileLoader
    sl = SourceFileLoader('flit_core.dummy.import%d' % _import_i, str(target.file))
    with _module_load_ctx():
        m = sl.load_module()
    docstring = m.__dict__.get('__doc__', None)
    version = m.__dict__.get('__version__', None)
    return docstring, version


def get_info_from_module(target, for_fields=('version', 'description')):
    """Load the module/package, get its docstring and __version__
    """
    if not for_fields:
        return {}

    # What core metadata calls Summary, PEP 621 calls description
    want_summary = 'description' in for_fields
    want_version = 'version' in for_fields

    log.debug("Loading module %s", target.file)

    # Attempt to extract our docstring & version by parsing our target's
    # AST, falling back to an import if that fails. This allows us to
    # build without necessarily requiring that our built package's
    # requirements are installed.
    docstring, version = get_docstring_and_version_via_ast(target)
    if (want_summary and not docstring) or (want_version and not version):
        docstring, version = get_docstring_and_version_via_import(target)

    res = {}

    if want_summary:
        if (not docstring) or not docstring.strip():
            raise NoDocstringError(
                'Flit cannot package module without docstring, or empty docstring. '
                'Please add a docstring to your module ({}).'.format(target.file)
            )
        res['summary'] = docstring.lstrip().splitlines()[0]

    if want_version:
        res['version'] = check_version(version)

    return res

def check_version(version):
    """
    Check whether a given version string match PEP 440, and do normalisation.

    Raise InvalidVersion/NoVersionError with relevant information if
    version is invalid.

    Log a warning if the version is not canonical with respect to PEP 440.

    Returns the version in canonical PEP 440 format.
    """
    if not version:
        raise NoVersionError('Cannot package module without a version string. '
                             'Please define a `__version__ = "x.y.z"` in your module.')
    if not isinstance(version, str):
        raise InvalidVersion('__version__ must be a string, not {}.'
                                .format(type(version)))

    # Import here to avoid circular import
    version = normalise_version(version)

    return version


script_template = """\
#!{interpreter}
# -*- coding: utf-8 -*-
import re
import sys
from {module} import {import_name}
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\\.pyw|\\.exe)?$', '', sys.argv[0])
    sys.exit({func}())
"""

def parse_entry_point(ep):
    """Check and parse a 'package.module:func' style entry point specification.

    Returns (modulename, funcname)
    """
    if ':' not in ep:
        raise ValueError("Invalid entry point (no ':'): %r" % ep)
    mod, func = ep.split(':')

    for piece in func.split('.'):
        if not piece.isidentifier():
            raise ValueError("Invalid entry point: %r is not an identifier" % piece)
    for piece in mod.split('.'):
        if not piece.isidentifier():
            raise ValueError("Invalid entry point: %r is not a module path" % piece)

    return mod, func

def write_entry_points(d, fp):
    """Write entry_points.txt from a two-level dict

    Sorts on keys to ensure results are reproducible.
    """
    for group_name in sorted(d):
        fp.write(u'[{}]\n'.format(group_name))
        group = d[group_name]
        for name in sorted(group):
            val = group[name]
            fp.write(u'{}={}\n'.format(name, val))
        fp.write(u'\n')

def hash_file(path, algorithm='sha256'):
    with open(path, 'rb') as f:
        h = hashlib.new(algorithm, f.read())
    return h.hexdigest()

def normalize_file_permissions(st_mode):
    """Normalize the permission bits in the st_mode field from stat to 644/755

    Popular VCSs only track whether a file is executable or not. The exact
    permissions can vary on systems with different umasks. Normalising
    to 644 (non executable) or 755 (executable) makes builds more reproducible.
    """
    # Set 644 permissions, leaving higher bits of st_mode unchanged
    new_mode = (st_mode | 0o644) & ~0o133
    if st_mode & 0o100:
        new_mode |= 0o111  # Executable: 644 -> 755
    return new_mode

class Metadata(object):

    summary = None
    home_page = None
    author = None
    author_email = None
    maintainer = None
    maintainer_email = None
    license = None
    description = None
    keywords = None
    download_url = None
    requires_python = None
    description_content_type = None

    platform = ()
    supported_platform = ()
    classifiers = ()
    provides = ()
    requires = ()
    obsoletes = ()
    project_urls = ()
    provides_dist = ()
    requires_dist = ()
    obsoletes_dist = ()
    requires_external = ()
    provides_extra = ()

    metadata_version = "2.1"

    def __init__(self, data):
        data = data.copy()
        self.name = data.pop('name')
        self.version = data.pop('version')

        for k, v in data.items():
            assert hasattr(self, k), "data does not have attribute '{}'".format(k)
            setattr(self, k, v)

    def _normalise_name(self, n):
        return n.lower().replace('-', '_')

    def write_metadata_file(self, fp):
        """Write out metadata in the email headers format"""
        fields = [
            'Metadata-Version',
            'Name',
            'Version',
        ]
        optional_fields = [
            'Summary',
            'Home-page',
            'License',
            'Keywords',
            'Author',
            'Author-email',
            'Maintainer',
            'Maintainer-email',
            'Requires-Python',
            'Description-Content-Type',
        ]

        for field in fields:
            value = getattr(self, self._normalise_name(field))
            fp.write(u"{}: {}\n".format(field, value))

        for field in optional_fields:
            value = getattr(self, self._normalise_name(field))
            if value is not None:
                # TODO: verify which fields can be multiline
                # The spec has multiline examples for Author, Maintainer &
                # License (& Description, but we put that in the body)
                # Indent following lines with 8 spaces:
                value = '\n        '.join(value.splitlines())
                fp.write(u"{}: {}\n".format(field, value))

        for clsfr in self.classifiers:
            fp.write(u'Classifier: {}\n'.format(clsfr))

        for req in self.requires_dist:
            fp.write(u'Requires-Dist: {}\n'.format(req))

        for url in self.project_urls:
            fp.write(u'Project-URL: {}\n'.format(url))

        for extra in self.provides_extra:
            fp.write(u'Provides-Extra: {}\n'.format(extra))

        if self.description is not None:
            fp.write(u'\n' + self.description + u'\n')

    @property
    def supports_py2(self):
        """Return True if Requires-Python indicates Python 2 support."""
        for part in (self.requires_python or "").split(","):
            if re.search(r"^\s*(>\s*(=\s*)?)?[3-9]", part):
                return False
        return True


def make_metadata(module, ini_info):
    md_dict = {'name': module.name, 'provides': [module.name]}
    md_dict.update(get_info_from_module(module, ini_info.dynamic_metadata))
    md_dict.update(ini_info.metadata)
    return Metadata(md_dict)



def normalize_dist_name(name: str, version: str) -> str:
    """Normalizes a name and a PEP 440 version

    The resulting string is valid as dist-info folder name
    and as first part of a wheel filename

    See https://packaging.python.org/specifications/binary-distribution-format/#escaping-and-unicode
    """
    normalized_name = re.sub(r'[-_.]+', '_', name, flags=re.UNICODE)
    assert check_version(version) == version
    assert '-' not in version, 'Normalized versions can’t have dashes'
    return '{}-{}'.format(normalized_name, version)


def dist_info_name(distribution, version):
    """Get the correct name of the .dist-info folder"""
    return normalize_dist_name(distribution, version) + '.dist-info'
