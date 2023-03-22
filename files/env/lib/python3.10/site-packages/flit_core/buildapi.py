"""PEP-517 compliant buildsystem API"""
import logging
import io
import os
import os.path as osp
from pathlib import Path

from .common import (
    Module, make_metadata, write_entry_points, dist_info_name,
    get_docstring_and_version_via_ast,
)
from .config import read_flit_config
from .wheel import make_wheel_in, _write_wheel_file
from .sdist import SdistBuilder

log = logging.getLogger(__name__)

# PEP 517 specifies that the CWD will always be the source tree
pyproj_toml = Path('pyproject.toml')

def get_requires_for_build_wheel(config_settings=None):
    """Returns a list of requirements for building, as strings"""
    info = read_flit_config(pyproj_toml)
    # If we can get version & description from pyproject.toml (PEP 621), or
    # by parsing the module (_via_ast), we don't need any extra
    # dependencies. If not, we'll need to try importing it, so report any
    # runtime dependencies as build dependencies.
    want_summary = 'description' in info.dynamic_metadata
    want_version = 'version' in info.dynamic_metadata

    module = Module(info.module, Path.cwd())
    docstring, version = get_docstring_and_version_via_ast(module)

    if (want_summary and not docstring) or (want_version and not version):
        return info.metadata.get('requires_dist', [])
    else:
        return []

# Requirements to build an sdist are the same as for a wheel
get_requires_for_build_sdist = get_requires_for_build_wheel

# Requirements to build an editable are the same as for a wheel
get_requires_for_build_editable = get_requires_for_build_wheel

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    """Creates {metadata_directory}/foo-1.2.dist-info"""
    ini_info = read_flit_config(pyproj_toml)
    module = Module(ini_info.module, Path.cwd())
    metadata = make_metadata(module, ini_info)

    dist_info = osp.join(metadata_directory,
                         dist_info_name(metadata.name, metadata.version))
    os.mkdir(dist_info)

    with io.open(osp.join(dist_info, 'WHEEL'), 'w', encoding='utf-8') as f:
        _write_wheel_file(f, supports_py2=metadata.supports_py2)

    with io.open(osp.join(dist_info, 'METADATA'), 'w', encoding='utf-8') as f:
        metadata.write_metadata_file(f)

    if ini_info.entrypoints:
        with io.open(osp.join(dist_info, 'entry_points.txt'), 'w', encoding='utf-8') as f:
            write_entry_points(ini_info.entrypoints, f)

    return osp.basename(dist_info)

# Metadata for editable are the same as for a wheel
prepare_metadata_for_build_editable = prepare_metadata_for_build_wheel

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    """Builds a wheel, places it in wheel_directory"""
    info = make_wheel_in(pyproj_toml, Path(wheel_directory))
    return info.file.name

def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    """Builds an "editable" wheel, places it in wheel_directory"""
    info = make_wheel_in(pyproj_toml, Path(wheel_directory), editable=True)
    return info.file.name

def build_sdist(sdist_directory, config_settings=None):
    """Builds an sdist, places it in sdist_directory"""
    path = SdistBuilder.from_ini_path(pyproj_toml).build(Path(sdist_directory))
    return path.name
