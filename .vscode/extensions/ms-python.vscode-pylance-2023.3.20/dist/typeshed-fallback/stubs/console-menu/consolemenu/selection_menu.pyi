from collections.abc import Iterable

from consolemenu import ConsoleMenu as ConsoleMenu
from consolemenu.items import SelectionItem as SelectionItem
from consolemenu.menu_formatter import MenuFormatBuilder
from consolemenu.screen import Screen

class SelectionMenu(ConsoleMenu):
    def __init__(
        self,
        strings: Iterable[str],
        title: str | None = ...,
        subtitle: str | None = ...,
        screen: Screen | None = ...,
        formatter: MenuFormatBuilder | None = ...,
        prologue_text: str | None = ...,
        epilogue_text: str | None = ...,
        show_exit_option: bool = ...,
        exit_option_text: str = ...,
        clear_screen: bool = ...,
    ) -> None: ...
    @classmethod
    def get_selection(
        cls,
        strings: Iterable[str],
        title: str = ...,
        subtitle: str | None = ...,
        show_exit_option: bool = ...,
        _menu: ConsoleMenu | None = ...,
    ) -> int: ...
    def append_string(self, string: str) -> None: ...
