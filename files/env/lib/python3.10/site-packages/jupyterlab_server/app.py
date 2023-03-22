"""JupyterLab Server Application"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin
from traitlets import Dict, Integer, Unicode, observe

from ._version import __version__
from .handlers import LabConfig, add_handlers


class LabServerApp(ExtensionAppJinjaMixin, LabConfig, ExtensionApp):
    """A Lab Server Application that runs out-of-the-box"""

    name = "jupyterlab_server"
    extension_url = "/lab"
    app_name = "JupyterLab Server Application"
    file_url_prefix = "/lab/tree"  # type:ignore

    @property
    def app_namespace(self):
        return self.name

    default_url = Unicode("/lab", help="The default URL to redirect to from `/`")

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    app_version = Unicode("", help="The version of the application.").tag(default=__version__)

    blacklist_uris = Unicode(
        "", config=True, help="Deprecated, use `LabServerApp.blocked_extensions_uris`"
    )

    blocked_extensions_uris = Unicode(
        "",
        config=True,
        help="""
        A list of comma-separated URIs to get the blocked extensions list

        .. versionchanged:: 2.0.0
            `LabServerApp.blacklist_uris` renamed to `blocked_extensions_uris`
        """,
    )

    whitelist_uris = Unicode(
        "", config=True, help="Deprecated, use `LabServerApp.allowed_extensions_uris`"
    )

    allowed_extensions_uris = Unicode(
        "",
        config=True,
        help="""
        "A list of comma-separated URIs to get the allowed extensions list

        .. versionchanged:: 2.0.0
            `LabServerApp.whitetlist_uris` renamed to `allowed_extensions_uris`
        """,
    )

    listings_refresh_seconds = Integer(
        60 * 60, config=True, help="The interval delay in seconds to refresh the lists"
    )

    listings_request_options = Dict(
        {},
        config=True,
        help="The optional kwargs to use for the listings HTTP requests \
            as described on https://2.python-requests.org/en/v2.7.0/api/#requests.request",
    )

    _deprecated_aliases = {
        "blacklist_uris": ("blocked_extensions_uris", "1.2"),
        "whitelist_uris": ("allowed_extensions_uris", "1.2"),
    }

    # Method copied from
    # https://github.com/jupyterhub/jupyterhub/blob/d1a85e53dccfc7b1dd81b0c1985d158cc6b61820/jupyterhub/auth.py#L143-L161
    @observe(*list(_deprecated_aliases))
    def _deprecated_trait(self, change):
        """observer for deprecated traits"""
        old_attr = change.name
        new_attr, version = self._deprecated_aliases.get(old_attr)  # type:ignore
        new_value = getattr(self, new_attr)
        if new_value != change.new:
            # only warn if different
            # protects backward-compatible config from warnings
            # if they set the same value under both names
            self.log.warning(
                "{cls}.{old} is deprecated in JupyterLab {version}, use {cls}.{new} instead".format(
                    cls=self.__class__.__name__,
                    old=old_attr,
                    new=new_attr,
                    version=version,
                )
            )
            setattr(self, new_attr, change.new)

    def initialize_templates(self):
        """Initialize templates."""
        self.static_paths = [self.static_dir]
        self.template_paths = [self.templates_dir]

    def initialize_handlers(self):
        """Initialize handlers."""
        add_handlers(self.handlers, self)


main = launch_new_instance = LabServerApp.launch_instance
