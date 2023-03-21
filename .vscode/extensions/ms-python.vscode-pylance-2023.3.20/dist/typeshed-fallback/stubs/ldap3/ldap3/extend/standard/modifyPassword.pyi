from _typeshed import Incomplete

from ...extend.operation import ExtendedOperation
from ...protocol.rfc3062 import PasswdModifyRequestValue, PasswdModifyResponseValue

class ModifyPassword(ExtendedOperation):
    request_name: str
    request_value: PasswdModifyRequestValue
    asn1_spec: PasswdModifyResponseValue
    response_attribute: str
    def config(self) -> None: ...
    def __init__(
        self,
        connection,
        user: Incomplete | None = ...,
        old_password: Incomplete | None = ...,
        new_password: Incomplete | None = ...,
        hash_algorithm: Incomplete | None = ...,
        salt: Incomplete | None = ...,
        controls: Incomplete | None = ...,
    ) -> None: ...
    def populate_result(self) -> None: ...
