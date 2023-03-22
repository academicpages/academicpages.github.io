import difflib
from email.headerregistry import Address
import errno
import logging
import os
import os.path as osp
from pathlib import Path
import re

from .vendor import tomli
from .versionno import normalise_version

log = logging.getLogger(__name__)


class ConfigError(ValueError):
    pass

metadata_list_fields = {
    'classifiers',
    'requires',
    'dev-requires'
}

metadata_allowed_fields = {
    'module',
    'author',
    'author-email',
    'maintainer',
    'maintainer-email',
    'home-page',
    'license',
    'keywords',
    'requires-python',
    'dist-name',
    'description-file',
    'requires-extra',
} | metadata_list_fields

metadata_required_fields = {
    'module',
    'author',
}

pep621_allowed_fields = {
    'name',
    'version',
    'description',
    'readme',
    'requires-python',
    'license',
    'authors',
    'maintainers',
    'keywords',
    'classifiers',
    'urls',
    'scripts',
    'gui-scripts',
    'entry-points',
    'dependencies',
    'optional-dependencies',
    'dynamic',
}


def read_flit_config(path):
    """Read and check the `pyproject.toml` file with data about the package.
    """
    d = tomli.loads(path.read_text('utf-8'))
    return prep_toml_config(d, path)


class EntryPointsConflict(ConfigError):
    def __str__(self):
        return ('Please specify console_scripts entry points, or [scripts] in '
            'flit config, not both.')

def prep_toml_config(d, path):
    """Validate config loaded from pyproject.toml and prepare common metadata
    
    Returns a LoadedConfig object.
    """
    dtool = d.get('tool', {}).get('flit', {})

    if 'project' in d:
        # Metadata in [project] table (PEP 621)
        if 'metadata' in dtool:
            raise ConfigError(
                "Use [project] table for metadata or [tool.flit.metadata], not both."
            )
        if ('scripts' in dtool) or ('entrypoints' in dtool):
            raise ConfigError(
                "Don't mix [project] metadata with [tool.flit.scripts] or "
                "[tool.flit.entrypoints]. Use [project.scripts],"
                "[project.gui-scripts] or [project.entry-points] as replacements."
            )
        loaded_cfg = read_pep621_metadata(d['project'], path)

        module_tbl = dtool.get('module', {})
        if 'name' in module_tbl:
            loaded_cfg.module = module_tbl['name']
    elif 'metadata' in dtool:
        # Metadata in [tool.flit.metadata] (pre PEP 621 format)
        if 'module' in dtool:
            raise ConfigError(
                "Use [tool.flit.module] table with new-style [project] metadata, "
                "not [tool.flit.metadata]"
            )
        loaded_cfg = _prep_metadata(dtool['metadata'], path)
        loaded_cfg.dynamic_metadata = ['version', 'description']

        if 'entrypoints' in dtool:
            loaded_cfg.entrypoints = flatten_entrypoints(dtool['entrypoints'])

        if 'scripts' in dtool:
            loaded_cfg.add_scripts(dict(dtool['scripts']))
    else:
        raise ConfigError(
            "Neither [project] nor [tool.flit.metadata] found in pyproject.toml"
        )

    unknown_sections = set(dtool) - {
        'metadata', 'module', 'scripts', 'entrypoints', 'sdist'
    }
    unknown_sections = [s for s in unknown_sections if not s.lower().startswith('x-')]
    if unknown_sections:
        raise ConfigError('Unexpected tables in pyproject.toml: ' + ', '.join(
            '[tool.flit.{}]'.format(s) for s in unknown_sections
        ))

    if 'sdist' in dtool:
        unknown_keys = set(dtool['sdist']) - {'include', 'exclude'}
        if unknown_keys:
            raise ConfigError(
                "Unknown keys in [tool.flit.sdist]:" + ", ".join(unknown_keys)
            )

        loaded_cfg.sdist_include_patterns = _check_glob_patterns(
            dtool['sdist'].get('include', []), 'include'
        )
        loaded_cfg.sdist_exclude_patterns = _check_glob_patterns(
            dtool['sdist'].get('exclude', []), 'exclude'
        )

    return loaded_cfg

def flatten_entrypoints(ep):
    """Flatten nested entrypoints dicts.

    Entry points group names can include dots. But dots in TOML make nested
    dictionaries:

    [entrypoints.a.b]    # {'entrypoints': {'a': {'b': {}}}}

    The proper way to avoid this is:

    [entrypoints."a.b"]  # {'entrypoints': {'a.b': {}}}

    But since there isn't a need for arbitrarily nested mappings in entrypoints,
    flit allows you to use the former. This flattens the nested dictionaries
    from loading pyproject.toml.
    """
    def _flatten(d, prefix):
        d1 = {}
        for k, v in d.items():
            if isinstance(v, dict):
                for flattened in _flatten(v, prefix+'.'+k):
                    yield flattened
            else:
                d1[k] = v

        if d1:
            yield prefix, d1

    res = {}
    for k, v in ep.items():
        res.update(_flatten(v, k))
    return res


def _check_glob_patterns(pats, clude):
    """Check and normalise glob patterns for sdist include/exclude"""
    if not isinstance(pats, list):
        raise ConfigError("sdist {} patterns must be a list".format(clude))

    # Windows filenames can't contain these (nor * or ?, but they are part of
    # glob patterns) - https://stackoverflow.com/a/31976060/434217
    bad_chars = re.compile(r'[\000-\037<>:"\\]')

    normed = []

    for p in pats:
        if bad_chars.search(p):
            raise ConfigError(
                '{} pattern {!r} contains bad characters (<>:\"\\ or control characters)'
                .format(clude, p)
            )
        if '**' in p:
            raise ConfigError(
                "Recursive globbing (**) is not supported yet (in {} pattern {!r})"
                .format(clude, p)
            )

        normp = osp.normpath(p)

        if osp.isabs(normp):
            raise ConfigError(
                '{} pattern {!r} is an absolute path'.format(clude, p)
            )
        if osp.normpath(p).startswith('..' + os.sep):
            raise ConfigError(
                '{} pattern {!r} points out of the directory containing pyproject.toml'
                .format(clude, p)
            )
        normed.append(normp)

    return normed


class LoadedConfig(object):
    def __init__(self):
        self.module = None
        self.metadata = {}
        self.reqs_by_extra = {}
        self.entrypoints = {}
        self.referenced_files = []
        self.sdist_include_patterns = []
        self.sdist_exclude_patterns = []
        self.dynamic_metadata = []

    def add_scripts(self, scripts_dict):
        if scripts_dict:
            if 'console_scripts' in self.entrypoints:
                raise EntryPointsConflict
            else:
                self.entrypoints['console_scripts'] = scripts_dict

readme_ext_to_content_type = {
    '.rst': 'text/x-rst',
    '.md': 'text/markdown',
    '.txt': 'text/plain',
}


def description_from_file(rel_path: str, proj_dir: Path, guess_mimetype=True):
    if osp.isabs(rel_path):
        raise ConfigError("Readme path must be relative")

    desc_path = proj_dir / rel_path
    try:
        with desc_path.open('r', encoding='utf-8') as f:
            raw_desc = f.read()
    except IOError as e:
        if e.errno == errno.ENOENT:
            raise ConfigError(
                "Description file {} does not exist".format(desc_path)
            )
        raise

    if guess_mimetype:
        ext = desc_path.suffix.lower()
        try:
            mimetype = readme_ext_to_content_type[ext]
        except KeyError:
            log.warning("Unknown extension %r for description file.", ext)
            log.warning("  Recognised extensions: %s",
                        " ".join(readme_ext_to_content_type))
            mimetype = None
    else:
        mimetype = None

    return raw_desc, mimetype


def _prep_metadata(md_sect, path):
    """Process & verify the metadata from a config file
    
    - Pull out the module name we're packaging.
    - Read description-file and check that it's valid rst
    - Convert dashes in key names to underscores
      (e.g. home-page in config -> home_page in metadata) 
    """
    if not set(md_sect).issuperset(metadata_required_fields):
        missing = metadata_required_fields - set(md_sect)
        raise ConfigError("Required fields missing: " + '\n'.join(missing))

    res = LoadedConfig()

    res.module = md_sect.get('module')
    if not all([m.isidentifier() for m in res.module.split(".")]):
        raise ConfigError("Module name %r is not a valid identifier" % res.module)

    md_dict = res.metadata

    # Description file
    if 'description-file' in md_sect:
        desc_path = md_sect.get('description-file')
        res.referenced_files.append(desc_path)
        desc_content, mimetype = description_from_file(desc_path, path.parent)
        md_dict['description'] =  desc_content
        md_dict['description_content_type'] = mimetype

    if 'urls' in md_sect:
        project_urls = md_dict['project_urls'] = []
        for label, url in sorted(md_sect.pop('urls').items()):
            project_urls.append("{}, {}".format(label, url))

    for key, value in md_sect.items():
        if key in {'description-file', 'module'}:
            continue
        if key not in metadata_allowed_fields:
            closest = difflib.get_close_matches(key, metadata_allowed_fields,
                                                n=1, cutoff=0.7)
            msg = "Unrecognised metadata key: {!r}".format(key)
            if closest:
                msg += " (did you mean {!r}?)".format(closest[0])
            raise ConfigError(msg)

        k2 = key.replace('-', '_')
        md_dict[k2] = value
        if key in metadata_list_fields:
            if not isinstance(value, list):
                raise ConfigError('Expected a list for {} field, found {!r}'
                                    .format(key, value))
            if not all(isinstance(a, str) for a in value):
                raise ConfigError('Expected a list of strings for {} field'
                                    .format(key))
        elif key == 'requires-extra':
            if not isinstance(value, dict):
                raise ConfigError('Expected a dict for requires-extra field, found {!r}'
                                    .format(value))
            if not all(isinstance(e, list) for e in value.values()):
                raise ConfigError('Expected a dict of lists for requires-extra field')
            for e, reqs in value.items():
                if not all(isinstance(a, str) for a in reqs):
                    raise ConfigError('Expected a string list for requires-extra. (extra {})'
                                        .format(e))
        else:
            if not isinstance(value, str):
                raise ConfigError('Expected a string for {} field, found {!r}'
                                    .format(key, value))

    # What we call requires in the ini file is technically requires_dist in
    # the metadata.
    if 'requires' in md_dict:
        md_dict['requires_dist'] = md_dict.pop('requires')

    # And what we call dist-name is name in the metadata
    if 'dist_name' in md_dict:
        md_dict['name'] = md_dict.pop('dist_name')

    # Move dev-requires into requires-extra
    reqs_noextra = md_dict.pop('requires_dist', [])
    res.reqs_by_extra = md_dict.pop('requires_extra', {})
    dev_requires = md_dict.pop('dev_requires', None)
    if dev_requires is not None:
        if 'dev' in res.reqs_by_extra:
            raise ConfigError(
                'dev-requires occurs together with its replacement requires-extra.dev.')
        else:
            log.warning(
                '"dev-requires = ..." is obsolete. Use "requires-extra = {"dev" = ...}" instead.')
            res.reqs_by_extra['dev'] = dev_requires

    # Add requires-extra requirements into requires_dist
    md_dict['requires_dist'] = \
        reqs_noextra + list(_expand_requires_extra(res.reqs_by_extra))

    md_dict['provides_extra'] = sorted(res.reqs_by_extra.keys())

    # For internal use, record the main requirements as a '.none' extra.
    res.reqs_by_extra['.none'] = reqs_noextra

    return res

def _expand_requires_extra(re):
    for extra, reqs in sorted(re.items()):
        for req in reqs:
            if ';' in req:
                name, envmark = req.split(';', 1)
                yield '{} ; extra == "{}" and ({})'.format(name, extra, envmark)
            else:
                yield '{} ; extra == "{}"'.format(req, extra)


def _check_type(d, field_name, cls):
    if not isinstance(d[field_name], cls):
        raise ConfigError(
            "{} field should be {}, not {}".format(field_name, cls, type(d[field_name]))
        )

def _check_list_of_str(d, field_name):
    if not isinstance(d[field_name], list) or not all(
        isinstance(e, str) for e in d[field_name]
    ):
        raise ConfigError(
            "{} field should be a list of strings".format(field_name)
        )

def read_pep621_metadata(proj, path) -> LoadedConfig:
    lc = LoadedConfig()
    md_dict = lc.metadata

    if 'name' not in proj:
        raise ConfigError('name must be specified in [project] table')
    _check_type(proj, 'name', str)
    lc.module = md_dict['name'] = proj['name']

    unexpected_keys = proj.keys() - pep621_allowed_fields
    if unexpected_keys:
        log.warning("Unexpected names under [project]: %s", ', '.join(unexpected_keys))

    if 'version' in proj:
        _check_type(proj, 'version', str)
        md_dict['version'] = normalise_version(proj['version'])
    if 'description' in proj:
        _check_type(proj, 'description', str)
        md_dict['summary'] = proj['description']
    if 'readme' in proj:
        readme = proj['readme']
        if isinstance(readme, str):
            lc.referenced_files.append(readme)
            desc_content, mimetype = description_from_file(readme, path.parent)

        elif isinstance(readme, dict):
            unrec_keys = set(readme.keys()) - {'text', 'file', 'content-type'}
            if unrec_keys:
                raise ConfigError(
                    "Unrecognised keys in [project.readme]: {}".format(unrec_keys)
                )
            if 'content-type' in readme:
                mimetype = readme['content-type']
                mtype_base = mimetype.split(';')[0].strip()  # e.g. text/x-rst
                if mtype_base not in readme_ext_to_content_type.values():
                    raise ConfigError(
                        "Unrecognised readme content-type: {!r}".format(mtype_base)
                    )
                # TODO: validate content-type parameters (charset, md variant)?
            else:
                raise ConfigError(
                    "content-type field required in [project.readme] table"
                )
            if 'file' in readme:
                if 'text' in readme:
                    raise ConfigError(
                        "[project.readme] should specify file or text, not both"
                    )
                lc.referenced_files.append(readme['file'])
                desc_content, _ = description_from_file(
                    readme['file'], path.parent, guess_mimetype=False
                )
            elif 'text' in readme:
                desc_content = readme['text']
            else:
                raise ConfigError(
                    "file or text field required in [project.readme] table"
                )
        else:
            raise ConfigError(
                "project.readme should be a string or a table"
            )

        md_dict['description'] = desc_content
        md_dict['description_content_type'] = mimetype

    if 'requires-python' in proj:
        md_dict['requires_python'] = proj['requires-python']

    if 'license' in proj:
        _check_type(proj, 'license', dict)
        license_tbl = proj['license']
        unrec_keys = set(license_tbl.keys()) - {'text', 'file'}
        if unrec_keys:
            raise ConfigError(
                "Unrecognised keys in [project.license]: {}".format(unrec_keys)
            )

        # TODO: Do something with license info.
        # The 'License' field in packaging metadata is a brief description of
        # a license, not the full text or a file path. PEP 639 will improve on
        # how licenses are recorded.
        if 'file' in license_tbl:
            if 'text' in license_tbl:
                raise ConfigError(
                    "[project.license] should specify file or text, not both"
                )
            lc.referenced_files.append(license_tbl['file'])
        elif 'text' in license_tbl:
            pass
        else:
            raise ConfigError(
                "file or text field required in [project.license] table"
            )

    if 'authors' in proj:
        _check_type(proj, 'authors', list)
        md_dict.update(pep621_people(proj['authors']))

    if 'maintainers' in proj:
        _check_type(proj, 'maintainers', list)
        md_dict.update(pep621_people(proj['maintainers'], group_name='maintainer'))

    if 'keywords' in proj:
        _check_list_of_str(proj, 'keywords')
        md_dict['keywords'] = ",".join(proj['keywords'])

    if 'classifiers' in proj:
        _check_list_of_str(proj, 'classifiers')
        md_dict['classifiers'] = proj['classifiers']

    if 'urls' in proj:
        _check_type(proj, 'urls', dict)
        project_urls = md_dict['project_urls'] = []
        for label, url in sorted(proj['urls'].items()):
            project_urls.append("{}, {}".format(label, url))

    if 'entry-points' in proj:
        _check_type(proj, 'entry-points', dict)
        for grp in proj['entry-points'].values():
            if not isinstance(grp, dict):
                raise ConfigError(
                    "projects.entry-points should only contain sub-tables"
                )
            if not all(isinstance(k, str) for k in grp.values()):
                raise ConfigError(
                    "[projects.entry-points.*] tables should have string values"
                )
        if set(proj['entry-points'].keys()) & {'console_scripts', 'gui_scripts'}:
            raise ConfigError(
                "Scripts should be specified in [project.scripts] or "
                "[project.gui-scripts], not under [project.entry-points]"
            )
        lc.entrypoints = proj['entry-points']

    if 'scripts' in proj:
        _check_type(proj, 'scripts', dict)
        if not all(isinstance(k, str) for k in proj['scripts'].values()):
            raise ConfigError(
                "[projects.scripts] table should have string values"
            )
        lc.entrypoints['console_scripts'] = proj['scripts']

    if 'gui-scripts' in proj:
        _check_type(proj, 'gui-scripts', dict)
        if not all(isinstance(k, str) for k in proj['gui-scripts'].values()):
            raise ConfigError(
                "[projects.gui-scripts] table should have string values"
            )
        lc.entrypoints['gui_scripts'] = proj['gui-scripts']

    if 'dependencies' in proj:
        _check_list_of_str(proj, 'dependencies')
        reqs_noextra = proj['dependencies']
    else:
        reqs_noextra = []

    if 'optional-dependencies' in proj:
        _check_type(proj, 'optional-dependencies', dict)
        optdeps = proj['optional-dependencies']
        if not all(isinstance(e, list) for e in optdeps.values()):
            raise ConfigError(
                'Expected a dict of lists in optional-dependencies field'
            )
        for e, reqs in optdeps.items():
            if not all(isinstance(a, str) for a in reqs):
                raise ConfigError(
                    'Expected a string list for optional-dependencies ({})'.format(e)
                )

        lc.reqs_by_extra = optdeps.copy()
        md_dict['provides_extra'] = sorted(lc.reqs_by_extra.keys())

    md_dict['requires_dist'] = \
        reqs_noextra + list(_expand_requires_extra(lc.reqs_by_extra))

    # For internal use, record the main requirements as a '.none' extra.
    if reqs_noextra:
        lc.reqs_by_extra['.none'] = reqs_noextra

    if 'dynamic' in proj:
        _check_list_of_str(proj, 'dynamic')
        dynamic = set(proj['dynamic'])
        unrec_dynamic = dynamic - {'version', 'description'}
        if unrec_dynamic:
            raise ConfigError(
                "flit only supports dynamic metadata for 'version' & 'description'"
            )
        if dynamic.intersection(proj):
            raise ConfigError(
                "keys listed in project.dynamic must not be in [project] table"
            )
        lc.dynamic_metadata = dynamic

    if ('version' not in proj) and ('version' not in lc.dynamic_metadata):
        raise ConfigError(
            "version must be specified under [project] or listed as a dynamic field"
        )
    if ('description' not in proj) and ('description' not in lc.dynamic_metadata):
        raise ConfigError(
            "description must be specified under [project] or listed as a dynamic field"
        )

    return lc

def pep621_people(people, group_name='author') -> dict:
    """Convert authors/maintainers from PEP 621 to core metadata fields"""
    names, emails = [], []
    for person in people:
        if not isinstance(person, dict):
            raise ConfigError("{} info must be list of dicts".format(group_name))
        unrec_keys = set(person.keys()) - {'name', 'email'}
        if unrec_keys:
            raise ConfigError(
                "Unrecognised keys in {} info: {}".format(group_name, unrec_keys)
            )
        if 'email' in person:
            email = person['email']
            if 'name' in person:
                email = str(Address(person['name'], addr_spec=email))
            emails.append(email)
        elif 'name' in person:
            names.append(person['name'])

    res = {}
    if names:
        res[group_name] = ", ".join(names)
    if emails:
        res[group_name + '_email'] = ", ".join(emails)
    return res
