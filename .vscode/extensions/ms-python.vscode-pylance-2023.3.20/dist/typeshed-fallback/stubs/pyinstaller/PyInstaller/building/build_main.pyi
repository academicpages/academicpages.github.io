# Referenced in: https://pyinstaller.org/en/stable/hooks.html?highlight=get_hook_config#PyInstaller.utils.hooks.get_hook_config
# Not to be imported during runtime, but is the type reference for hooks and analysis configuration

from _typeshed import Incomplete, StrPath
from collections.abc import Iterable
from typing import Any

from PyInstaller.building.datastruct import Target

class Analysis(Target):
    # https://pyinstaller.org/en/stable/hooks-config.html#hook-configuration-options
    hooksconfig: dict[str, dict[str, object]]
    def __init__(
        self,
        scripts: Iterable[StrPath],
        pathex: Incomplete | None = None,
        binaries: Incomplete | None = None,
        datas: Incomplete | None = None,
        hiddenimports: Incomplete | None = None,
        hookspath: Incomplete | None = None,
        hooksconfig: dict[str, dict[str, Any]] | None = None,
        excludes: Incomplete | None = None,
        runtime_hooks: Incomplete | None = None,
        cipher: Incomplete | None = None,
        win_no_prefer_redirects: bool = False,
        win_private_assemblies: bool = False,
        noarchive: bool = False,
        module_collection_mode: Incomplete | None = None,
    ) -> None: ...
