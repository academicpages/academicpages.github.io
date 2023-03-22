#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import os
import json

from jupyter_core.paths import jupyter_path
import nbconvert.exporters.templateexporter


ROOT = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(ROOT, 'static')
# if the directory above us contains the following paths, it means we are installed in dev mode (pip install -e .)
DEV_MODE = os.path.exists(os.path.join(ROOT, '../setup.py')) and os.path.exists(os.path.join(ROOT, '../share'))


def collect_template_paths(app_names, template_name='default', prune=False, root_dirs=None):
    return collect_paths(app_names, template_name, include_root_paths=True, prune=prune, root_dirs=root_dirs)


def collect_static_paths(app_names, template_name='default', prune=False, root_dirs=None):
    return collect_paths(
        app_names, template_name, include_root_paths=False, prune=prune, root_dirs=root_dirs, subdir='static'
    )


def collect_paths(
    app_names, template_name='default', subdir=None, include_root_paths=True, prune=False, root_dirs=None
):
    """
    Voilà supports custom templates for rendering notebooks.
    For a specified template name, `collect_paths` can be used to collects
        - template paths
        - resources paths (by using the subdir arg)

    by looking in the standard Jupyter data directories:
    $PREFIX/share/jupyter/templates/<app_name>/<template_name>[/subdir]
    with different prefix values (user directory, sys prefix, and then system prefix) which
    allows users to override templates locally.
    The function will recursively load the base templates upon which the specified template
    may be based.
    """
    found_at_least_one = False
    paths = []
    full_paths = []  # only used for error reporting

    root_dirs = root_dirs or _default_root_dirs()

    # first find a list of the template 'hierarchy'
    template_names = _find_template_hierarchy(app_names, template_name, root_dirs)

    # the order of the loop determines the precedense of the template system
    # * first template_names, e.g. if we inherit from default template, we only
    #   want to find those files last
    for template_name in template_names:
        for root_dir in root_dirs:
            for app_name in app_names:
                app_dir = os.path.join(root_dir, app_name, 'templates')
                path = os.path.join(app_dir, template_name)
                if subdir:
                    path = os.path.join(path, subdir)
                if not prune or os.path.exists(path):
                    paths.append(path)
                    found_at_least_one = True
            # for app_name in app_names:
            #     app_dir = os.path.join(root_dir, app_name, 'templates')
            #     # we include app_dir for when we want to be explicit, but less than root_dir, e.g.
            #     # {% extends 'classic/base.html' %}
            #     paths.append(app_dir)
            #     full_paths.append(app_dir)  # only used for error msg
    if include_root_paths:
        for root_dir in root_dirs:
            # we include root_dir for when we want to be very explicit, e.g.
            # {% extends 'nbconvert/templates/classic/base.html' %}
            paths.append(root_dir)
            for app_name in app_names:
                app_dir = os.path.join(root_dir, app_name, 'templates')
                # we include app_dir for when we want to be explicit, but less than root_dir, e.g.
                # {% extends 'classic/base.html' %}
                paths.append(app_dir)

    if not found_at_least_one:
        paths = "\n\t".join(full_paths)
        raise ValueError(
            'No template sub-directory with name %r found in the following paths:\n\t%s' % (template_name, paths)
        )
    return paths


def _default_root_dirs():
    # We look at the usual jupyter locations, and for development purposes also
    # relative to the package directory (first entry, meaning with highest precedence)
    root_dirs = []
    if DEV_MODE:
        root_dirs.append(os.path.abspath(os.path.join(ROOT, '..', 'share', 'jupyter')))
    if nbconvert.exporters.templateexporter.DEV_MODE:
        root_dirs.append(os.path.abspath(os.path.join(nbconvert.exporters.templateexporter.ROOT, '..', '..', 'share', 'jupyter')))
    root_dirs.extend(jupyter_path())

    return root_dirs


def _find_template_hierarchy(app_names, template_name, root_dirs):
    template_names = []
    while template_name is not None:
        template_names.append(template_name)
        conf = {}
        for root_dir in root_dirs:
            for app_name in app_names:
                conf_file = os.path.join(root_dir, app_name, 'templates', template_name, 'conf.json')
                if os.path.exists(conf_file):
                    with open(conf_file) as f:
                        new_conf = json.load(f)
                        new_conf.update(conf)
                        conf = new_conf
        if 'base_template' in conf:
            template_name = conf['base_template']
        else:
            if template_name == 'base':
                # the default template has no base_template
                template_name = None
            else:
                # if not specified, 'base' is assumed
                template_name = 'base'
    return template_names
