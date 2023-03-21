from _typeshed import Incomplete
from typing import Any

class StripeError(Exception):
    http_body: Any
    http_status: Any
    json_body: Any
    headers: Any
    code: Any
    request_id: Any
    error: Any
    def __init__(
        self,
        message: Incomplete | None = ...,
        http_body: Incomplete | None = ...,
        http_status: Incomplete | None = ...,
        json_body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        code: Incomplete | None = ...,
    ) -> None: ...
    @property
    def user_message(self): ...
    def construct_error_object(self): ...

class APIError(StripeError): ...

class APIConnectionError(StripeError):
    should_retry: Any
    def __init__(
        self,
        message,
        http_body: Incomplete | None = ...,
        http_status: Incomplete | None = ...,
        json_body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        code: Incomplete | None = ...,
        should_retry: bool = ...,
    ) -> None: ...

class StripeErrorWithParamCode(StripeError): ...

class CardError(StripeErrorWithParamCode):
    param: Any
    def __init__(
        self,
        message,
        param,
        code,
        http_body: Incomplete | None = ...,
        http_status: Incomplete | None = ...,
        json_body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
    ) -> None: ...

class IdempotencyError(StripeError): ...

class InvalidRequestError(StripeErrorWithParamCode):
    param: Any
    def __init__(
        self,
        message,
        param,
        code: Incomplete | None = ...,
        http_body: Incomplete | None = ...,
        http_status: Incomplete | None = ...,
        json_body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
    ) -> None: ...

class AuthenticationError(StripeError): ...
class PermissionError(StripeError): ...
class RateLimitError(StripeError): ...

class SignatureVerificationError(StripeError):
    sig_header: Any
    def __init__(self, message, sig_header, http_body: Incomplete | None = ...) -> None: ...
