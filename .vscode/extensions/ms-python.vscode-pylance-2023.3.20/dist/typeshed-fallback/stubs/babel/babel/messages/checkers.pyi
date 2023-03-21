from collections.abc import Callable

from babel.messages.catalog import Catalog, Message

def num_plurals(catalog: Catalog | None, message: Message) -> None: ...
def python_format(catalog: Catalog | None, message: Message) -> None: ...

checkers: list[Callable[[Catalog | None, Message], object]]
