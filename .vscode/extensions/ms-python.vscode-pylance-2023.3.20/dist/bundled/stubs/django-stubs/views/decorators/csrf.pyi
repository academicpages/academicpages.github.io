from typing import Any, Callable, TypeVar

from django.middleware.csrf import CsrfViewMiddleware

_F = TypeVar("_F", bound=Callable[..., Any])

def csrf_protect(__view: _F) -> _F: ...

class _EnsureCsrfToken(CsrfViewMiddleware): ...

def requires_csrf_token(__view: _F) -> _F: ...

class _EnsureCsrfCookie(CsrfViewMiddleware):
    get_response: None
    def process_view(
        self, request: Any, callback: Any, callback_args: Any, callback_kwargs: Any
    ) -> Any: ...

def ensure_csrf_cookie(__view: _F) -> _F: ...
def csrf_exempt(view_func: _F) -> _F: ...
