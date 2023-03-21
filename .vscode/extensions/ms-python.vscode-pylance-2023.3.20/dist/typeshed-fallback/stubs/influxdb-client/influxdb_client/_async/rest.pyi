import io
from _typeshed import Incomplete

class RESTResponseAsync(io.IOBase):
    aiohttp_response: Incomplete
    status: Incomplete
    reason: Incomplete
    data: Incomplete
    def __init__(self, resp, data) -> None: ...
    def getheaders(self): ...
    def getheader(self, name, default: Incomplete | None = ...): ...

class RESTClientObjectAsync:
    proxy: Incomplete
    proxy_headers: Incomplete
    allow_redirects: Incomplete
    max_redirects: Incomplete
    pool_manager: Incomplete
    def __init__(self, configuration, pools_size: int = ..., maxsize: Incomplete | None = ..., **kwargs) -> None: ...
    async def close(self) -> None: ...
    async def request(
        self,
        method,
        url,
        query_params: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def GET(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def HEAD(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def OPTIONS(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def DELETE(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def POST(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def PUT(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
    async def PATCH(
        self,
        url,
        headers: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
    ): ...
