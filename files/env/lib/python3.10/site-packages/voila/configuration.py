#############################################################################
# Copyright (c) 2018, QuantStack                                            #
# Copyright (c) 2018, Voilà Contributors                                    #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import traitlets.config
from traitlets import Unicode, Bool, Dict, List, Int, Enum, Type


class VoilaConfiguration(traitlets.config.Configurable):
    """Common configuration options between the server extension and the application."""
    allow_template_override = Enum(['YES', 'NOTEBOOK', 'NO'], 'YES', help='''
    Allow overriding the template (YES), or not (NO), or only from the notebook metadata.
    ''', config=True)
    allow_theme_override = Enum(['YES', 'NOTEBOOK', 'NO'], 'YES', help='''
    Allow overriding the theme (YES), or not (NO), or only from the notebook metadata.
    ''', config=True)
    template = Unicode(
        'lab',
        config=True,
        allow_none=True,
        help=(
            'template name to be used by voila.'
        )
    )
    resources = Dict(
        allow_none=True,
        config=True,
        help="""
        extra resources used by templates;
        example use with --template=reveal
        --VoilaConfiguration.resources="{'reveal': {'transition': 'fade', 'scroll': True}}"
        """
    )
    theme = Unicode('light', config=True)
    strip_sources = Bool(True, config=True, help='Strip sources from rendered html')
    enable_nbextensions = Bool(False, config=True, help=('Set to True for Voilà to load notebook extensions'))
    nbextensions_path = Unicode('', config=True, help='Set to override default path provided by Jupyter Server')

    file_whitelist = List(
        Unicode(),
        [r'.*\.(png|jpg|gif|svg)'],
        config=True,
        help=r"""
    List of regular expressions for controlling which static files are served.
    All files that are served should at least match 1 whitelist rule, and no blacklist rule
    Example: --VoilaConfiguration.file_whitelist="['.*\.(png|jpg|gif|svg)', 'public.*']"
    """,
    )

    file_blacklist = List(
        Unicode(),
        [r'.*\.(ipynb|py)'],
        config=True,
        help=r"""
    List of regular expressions for controlling which static files are forbidden to be served.
    All files that are served should at least match 1 whitelist rule, and no blacklist rule
    Example:
    --VoilaConfiguration.file_whitelist="['.*']" # all files
    --VoilaConfiguration.file_blacklist="['private.*', '.*\.(ipynb)']" # except files in the private dir and notebook files
    """
    )

    language_kernel_mapping = Dict(
        {},
        config=True,
        help="""Mapping of language name to kernel name
        Example mapping python to use xeus-python, and C++11 to use xeus-cling:
        --VoilaConfiguration.extension_language_mapping='{"python": "xpython", "C++11": "xcpp11"}'
        """,
    )

    extension_language_mapping = Dict(
        {},
        config=True,
        help='''Mapping of file extension to kernel language
        Example mapping .py files to a python language kernel, and .cpp to a C++11 language kernel:
        --VoilaConfiguration.extension_language_mapping='{".py": "python", ".cpp": "C++11"}'
        ''',
    )

    http_keep_alive_timeout = Int(10, config=True, help="""
    When a cell takes a long time to execute, the http connection can timeout (possibly because of a proxy).
    Voila sends a 'heartbeat' message after the timeout is passed to keep the http connection alive.
    """)

    show_tracebacks = Bool(False, config=True, help=(
        'Whether to send tracebacks to clients on exceptions.'
    ))

    multi_kernel_manager_class = Type(
        config=True,
        default_value='jupyter_server.services.kernels.kernelmanager.AsyncMappingKernelManager',
        # default_value='voila.voila_kernel_manager.VoilaKernelManager',
        klass='jupyter_client.multikernelmanager.MultiKernelManager',
        help="""The kernel manager class. This is useful to specify a different kernel manager,
        for example a kernel manager with support for pooling.
        """
    )

    http_header_envs = List(
        Unicode(),
        [],
        help=r"""
    List of HTTP Headers that should be passed as env vars to the kernel.
    Example: --VoilaConfiguration.http_header_envs="['X-CDSDASHBOARDS-JH-USER']"
    """,
    ).tag(config=True)

    preheat_kernel = Bool(
        False,
        config=True,
        help="""Flag to enable or disable pre-heat kernel option.
        """
    )
    default_pool_size = Int(
        1,
        config=True,
        help="""Size of pre-heated kernel pool for each notebook. Zero or negative number means disabled.
        """
    )
