from consolemenu import ConsoleMenu as ConsoleMenu
from consolemenu.console_menu import MenuItem
from consolemenu.items import SubmenuItem as SubmenuItem
from consolemenu.menu_formatter import MenuFormatBuilder

class MultiSelectMenu(ConsoleMenu):
    ack_item_completion: bool
    def __init__(
        self,
        title: str | None = ...,
        subtitle: str | None = ...,
        formatter: MenuFormatBuilder | None = ...,
        prologue_text: str | None = ...,
        epilogue_text: str | None = ...,
        ack_item_completion: bool = ...,
        show_exit_option: bool = ...,
        exit_option_text: str = ...,
        clear_screen: bool = ...,
    ) -> None: ...
    def append_item(self, item: MenuItem) -> None: ...
    current_option: int
    def process_user_input(self) -> None: ...
