from _typeshed import SupportsRead, SupportsWrite

from babel.messages.catalog import Catalog

LE_MAGIC: int
BE_MAGIC: int

def read_mo(fileobj: SupportsRead[bytes]) -> Catalog: ...
def write_mo(fileobj: SupportsWrite[bytes], catalog: Catalog, use_fuzzy: bool = ...) -> None: ...
