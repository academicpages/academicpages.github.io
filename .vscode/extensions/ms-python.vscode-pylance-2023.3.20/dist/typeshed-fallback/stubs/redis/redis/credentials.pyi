from abc import abstractmethod

class CredentialProvider:
    @abstractmethod
    def get_credentials(self) -> tuple[str] | tuple[str, str]: ...

class UsernamePasswordCredentialProvider(CredentialProvider):
    username: str
    password: str
    def __init__(self, username: str | None = ..., password: str | None = ...) -> None: ...
    def get_credentials(self) -> tuple[str] | tuple[str, str]: ...
