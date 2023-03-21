import io
from _typeshed import Incomplete

class RESTResponse(io.IOBase):
    urllib3_response: Incomplete
    status: Incomplete
    reason: Incomplete
    data: Incomplete
    def __init__(self, resp) -> None: ...
    def getheaders(self): ...
    def getheader(self, name, default: Incomplete | None = ...): ...

class RESTClientObject:
    configuration: Incomplete
    pools_size: Incomplete
    maxsize: Incomplete
    retries: Incomplete
    pool_manager: Incomplete
    def __init__(self, configuration, pools_size: int = ..., maxsize: Incomplete | None = ..., retries: bool = ...) -> None: ...
    def request(
        self,
        method,
        url,
        query_params: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def GET(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def HEAD(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def OPTIONS(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def DELETE(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def POST(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def PUT(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def PATCH(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
