from .enums import PageMode

class ViewerPreferences:
    hide_toolbar: bool
    hide_menubar: bool
    hide_window_u_i: bool
    fit_window: bool
    center_window: bool
    display_doc_title: bool
    def __init__(
        self,
        hide_toolbar: bool = ...,
        hide_menubar: bool = ...,
        hide_window_u_i: bool = ...,
        fit_window: bool = ...,
        center_window: bool = ...,
        display_doc_title: bool = ...,
        non_full_screen_page_mode: PageMode | str = ...,
    ) -> None: ...
    @property
    def non_full_screen_page_mode(self): ...
    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, page_mode) -> None: ...
    def serialize(self): ...
