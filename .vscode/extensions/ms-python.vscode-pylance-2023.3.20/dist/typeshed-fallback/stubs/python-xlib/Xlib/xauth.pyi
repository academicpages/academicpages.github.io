from _typeshed import FileDescriptorOrPath

FamilyInternet: int
FamilyDECnet: int
FamilyChaos: int
FamilyServerInterpreted: int
FamilyInternetV6: int
FamilyLocal: int

class Xauthority:
    entries: list[tuple[bytes, bytes, bytes, bytes, bytes]]
    def __init__(self, filename: FileDescriptorOrPath | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> tuple[bytes, bytes, bytes, bytes, bytes]: ...
    def get_best_auth(
        self, family: bytes, address: bytes, dispno: bytes, types: tuple[bytes, ...] = ...
    ) -> tuple[bytes, bytes]: ...
