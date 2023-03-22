from collections import defaultdict
from copy import copy
from glob import glob
from gzip import GzipFile
import io
import logging
import os
import os.path as osp
from pathlib import Path
from posixpath import join as pjoin
import tarfile

from . import common

log = logging.getLogger(__name__)


def clean_tarinfo(ti, mtime=None):
    """Clean metadata from a TarInfo object to make it more reproducible.

    - Set uid & gid to 0
    - Set uname and gname to ""
    - Normalise permissions to 644 or 755
    - Set mtime if not None
    """
    ti = copy(ti)
    ti.uid = 0
    ti.gid = 0
    ti.uname = ''
    ti.gname = ''
    ti.mode = common.normalize_file_permissions(ti.mode)
    if mtime is not None:
        ti.mtime = mtime
    return ti


class FilePatterns:
    """Manage a set of file inclusion/exclusion patterns relative to basedir"""
    def __init__(self, patterns, basedir):
        self.basedir = basedir

        self.dirs = set()
        self.files = set()

        for pattern in patterns:
            for path in sorted(glob(osp.join(basedir, pattern))):
                rel = osp.relpath(path, basedir)
                if osp.isdir(path):
                    self.dirs.add(rel)
                else:
                    self.files.add(rel)

    def match_file(self, rel_path):
        if rel_path in self.files:
            return True

        return any(rel_path.startswith(d + os.sep) for d in self.dirs)

    def match_dir(self, rel_path):
        if rel_path in self.dirs:
            return True

        # Check if it's a subdirectory of any directory in the list
        return any(rel_path.startswith(d + os.sep) for d in self.dirs)


class SdistBuilder:
    """Builds a minimal sdist

    These minimal sdists should work for PEP 517.
    The class is extended in flit.sdist to make a more 'full fat' sdist,
    which is what should normally be published to PyPI.
    """
    def __init__(self, module, metadata, cfgdir, reqs_by_extra, entrypoints,
                 extra_files, include_patterns=(), exclude_patterns=()):
        self.module = module
        self.metadata = metadata
        self.cfgdir = cfgdir
        self.reqs_by_extra = reqs_by_extra
        self.entrypoints = entrypoints
        self.extra_files = extra_files
        self.includes = FilePatterns(include_patterns, str(cfgdir))
        self.excludes = FilePatterns(exclude_patterns, str(cfgdir))

    @classmethod
    def from_ini_path(cls, ini_path: Path):
        # Local import so bootstrapping doesn't try to load toml
        from .config import read_flit_config
        ini_info = read_flit_config(ini_path)
        srcdir = ini_path.parent
        module = common.Module(ini_info.module, srcdir)
        metadata = common.make_metadata(module, ini_info)
        extra_files = [ini_path.name] + ini_info.referenced_files
        return cls(
            module, metadata, srcdir, ini_info.reqs_by_extra,
            ini_info.entrypoints, extra_files, ini_info.sdist_include_patterns,
            ini_info.sdist_exclude_patterns,
        )

    def prep_entry_points(self):
        # Reformat entry points from dict-of-dicts to dict-of-lists
        res = defaultdict(list)
        for groupname, group in self.entrypoints.items():
            for name, ep in sorted(group.items()):
                res[groupname].append('{} = {}'.format(name, ep))

        return dict(res)

    def select_files(self):
        """Pick which files from the source tree will be included in the sdist

        This is overridden in flit itself to use information from a VCS to
        include tests, docs, etc. for a 'gold standard' sdist.
        """
        cfgdir_s = str(self.cfgdir)
        return [
            osp.relpath(p, cfgdir_s) for p in self.module.iter_files()
        ] + self.extra_files

    def apply_includes_excludes(self, files):
        cfgdir_s = str(self.cfgdir)
        files = {f for f in files if not self.excludes.match_file(f)}

        for f_rel in self.includes.files:
            if not self.excludes.match_file(f_rel):
                files.add(f_rel)

        for rel_d in self.includes.dirs:
            for dirpath, dirs, dfiles in os.walk(osp.join(cfgdir_s, rel_d)):
                for file in dfiles:
                    f_abs = osp.join(dirpath, file)
                    f_rel = osp.relpath(f_abs, cfgdir_s)
                    if not self.excludes.match_file(f_rel):
                        files.add(f_rel)

                # Filter subdirectories before os.walk scans them
                dirs[:] = [d for d in dirs if not self.excludes.match_dir(
                    osp.relpath(osp.join(dirpath, d), cfgdir_s)
                )]

        crucial_files = set(
            self.extra_files + [str(self.module.file.relative_to(self.cfgdir))]
        )
        missing_crucial = crucial_files - files
        if missing_crucial:
            raise Exception("Crucial files were excluded from the sdist: {}"
                            .format(", ".join(missing_crucial)))

        return sorted(files)

    def add_setup_py(self, files_to_add, target_tarfile):
        """No-op here; overridden in flit to generate setup.py"""
        pass

    @property
    def dir_name(self):
        return '{}-{}'.format(self.metadata.name, self.metadata.version)

    def build(self, target_dir, gen_setup_py=True):
        os.makedirs(str(target_dir), exist_ok=True)
        target = target_dir / '{}-{}.tar.gz'.format(
                self.metadata.name, self.metadata.version
        )
        source_date_epoch = os.environ.get('SOURCE_DATE_EPOCH', '')
        mtime = int(source_date_epoch) if source_date_epoch else None
        gz = GzipFile(str(target), mode='wb', mtime=mtime)
        tf = tarfile.TarFile(str(target), mode='w', fileobj=gz,
                             format=tarfile.PAX_FORMAT)

        try:
            files_to_add = self.apply_includes_excludes(self.select_files())

            for relpath in files_to_add:
                path = str(self.cfgdir / relpath)
                ti = tf.gettarinfo(path, arcname=pjoin(self.dir_name, relpath))
                ti = clean_tarinfo(ti, mtime)

                if ti.isreg():
                    with open(path, 'rb') as f:
                        tf.addfile(ti, f)
                else:
                    tf.addfile(ti)  # Symlinks & ?

            if gen_setup_py:
                self.add_setup_py(files_to_add, tf)

            stream = io.StringIO()
            self.metadata.write_metadata_file(stream)
            pkg_info = stream.getvalue().encode()
            ti = tarfile.TarInfo(pjoin(self.dir_name, 'PKG-INFO'))
            ti.size = len(pkg_info)
            tf.addfile(ti, io.BytesIO(pkg_info))

        finally:
            tf.close()
            gz.close()

        log.info("Built sdist: %s", target)
        return target
