from _typeshed import Incomplete

class ApiClientAsync:
    PRIMITIVE_TYPES: Incomplete
    NATIVE_TYPES_MAPPING: Incomplete
    configuration: Incomplete
    pool_threads: Incomplete
    rest_client: Incomplete
    default_headers: Incomplete
    cookie: Incomplete
    def __init__(
        self,
        configuration: Incomplete | None = ...,
        header_name: Incomplete | None = ...,
        header_value: Incomplete | None = ...,
        cookie: Incomplete | None = ...,
        pool_threads: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    async def close(self) -> None: ...
    @property
    def pool(self): ...
    @property
    def user_agent(self): ...
    @user_agent.setter
    def user_agent(self, value) -> None: ...
    def set_default_header(self, header_name, header_value) -> None: ...
    def sanitize_for_serialization(self, obj): ...
    def deserialize(self, response, response_type): ...
    def call_api(
        self,
        resource_path,
        method,
        path_params: Incomplete | None = ...,
        query_params: Incomplete | None = ...,
        header_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        files: Incomplete | None = ...,
        response_type: Incomplete | None = ...,
        auth_settings: Incomplete | None = ...,
        async_req: Incomplete | None = ...,
        _return_http_data_only: Incomplete | None = ...,
        collection_formats: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        urlopen_kw: Incomplete | None = ...,
    ): ...
    def request(
        self,
        method,
        url,
        query_params: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        post_params: Incomplete | None = ...,
        body: Incomplete | None = ...,
        _preload_content: bool = ...,
        _request_timeout: Incomplete | None = ...,
        **urlopen_kw,
    ): ...
    def parameters_to_tuples(self, params, collection_formats): ...
    def prepare_post_parameters(self, post_params: Incomplete | None = ..., files: Incomplete | None = ...): ...
    def select_header_accept(self, accepts): ...
    def select_header_content_type(self, content_types): ...
    def update_params_for_auth(self, headers, querys, auth_settings) -> None: ...
