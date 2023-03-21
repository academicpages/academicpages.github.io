from _typeshed import Incomplete
from typing import Any

from boto.connection import AWSAuthConnection
from boto.exception import BotoClientError

from .bucket import Bucket

def check_lowercase_bucketname(n): ...
def assert_case_insensitive(f): ...

class _CallingFormat:
    def get_bucket_server(self, server, bucket): ...
    def build_url_base(self, connection, protocol, server, bucket, key: str = ...): ...
    def build_host(self, server, bucket): ...
    def build_auth_path(self, bucket, key: str = ...): ...
    def build_path_base(self, bucket, key: str = ...): ...

class SubdomainCallingFormat(_CallingFormat):
    def get_bucket_server(self, server, bucket): ...

class VHostCallingFormat(_CallingFormat):
    def get_bucket_server(self, server, bucket): ...

class OrdinaryCallingFormat(_CallingFormat):
    def get_bucket_server(self, server, bucket): ...
    def build_path_base(self, bucket, key: str = ...): ...

class ProtocolIndependentOrdinaryCallingFormat(OrdinaryCallingFormat):
    def build_url_base(self, connection, protocol, server, bucket, key: str = ...): ...

class Location:
    DEFAULT: str
    EU: str
    EUCentral1: str
    USWest: str
    USWest2: str
    SAEast: str
    APNortheast: str
    APSoutheast: str
    APSoutheast2: str
    CNNorth1: str

class NoHostProvided: ...
class HostRequiredError(BotoClientError): ...

class S3Connection(AWSAuthConnection):
    DefaultHost: Any
    DefaultCallingFormat: Any
    QueryString: str
    calling_format: Any
    bucket_class: type[Bucket]
    anon: Any
    def __init__(
        self,
        aws_access_key_id: Incomplete | None = ...,
        aws_secret_access_key: Incomplete | None = ...,
        is_secure: bool = ...,
        port: Incomplete | None = ...,
        proxy: Incomplete | None = ...,
        proxy_port: Incomplete | None = ...,
        proxy_user: Incomplete | None = ...,
        proxy_pass: Incomplete | None = ...,
        host: Any = ...,
        debug: int = ...,
        https_connection_factory: Incomplete | None = ...,
        calling_format: Any = ...,
        path: str = ...,
        provider: str = ...,
        bucket_class: type[Bucket] = ...,
        security_token: Incomplete | None = ...,
        suppress_consec_slashes: bool = ...,
        anon: bool = ...,
        validate_certs: Incomplete | None = ...,
        profile_name: Incomplete | None = ...,
    ) -> None: ...
    def __iter__(self): ...
    def __contains__(self, bucket_name): ...
    def set_bucket_class(self, bucket_class: type[Bucket]) -> None: ...
    def build_post_policy(self, expiration_time, conditions): ...
    def build_post_form_args(
        self,
        bucket_name,
        key,
        expires_in: int = ...,
        acl: Incomplete | None = ...,
        success_action_redirect: Incomplete | None = ...,
        max_content_length: Incomplete | None = ...,
        http_method: str = ...,
        fields: Incomplete | None = ...,
        conditions: Incomplete | None = ...,
        storage_class: str = ...,
        server_side_encryption: Incomplete | None = ...,
    ): ...
    def generate_url_sigv4(
        self,
        expires_in,
        method,
        bucket: str = ...,
        key: str = ...,
        headers: dict[str, str] | None = ...,
        force_http: bool = ...,
        response_headers: dict[str, str] | None = ...,
        version_id: Incomplete | None = ...,
        iso_date: Incomplete | None = ...,
    ): ...
    def generate_url(
        self,
        expires_in,
        method,
        bucket: str = ...,
        key: str = ...,
        headers: dict[str, str] | None = ...,
        query_auth: bool = ...,
        force_http: bool = ...,
        response_headers: dict[str, str] | None = ...,
        expires_in_absolute: bool = ...,
        version_id: Incomplete | None = ...,
    ): ...
    def get_all_buckets(self, headers: dict[str, str] | None = ...): ...
    def get_canonical_user_id(self, headers: dict[str, str] | None = ...): ...
    def get_bucket(self, bucket_name: str, validate: bool = ..., headers: dict[str, str] | None = ...) -> Bucket: ...
    def head_bucket(self, bucket_name, headers: dict[str, str] | None = ...): ...
    def lookup(self, bucket_name, validate: bool = ..., headers: dict[str, str] | None = ...): ...
    def create_bucket(
        self, bucket_name, headers: dict[str, str] | None = ..., location: Any = ..., policy: Incomplete | None = ...
    ): ...
    def delete_bucket(self, bucket, headers: dict[str, str] | None = ...): ...
    def make_request(  # type: ignore[override]
        self,
        method,
        bucket: str = ...,
        key: str = ...,
        headers: Incomplete | None = ...,
        data: str = ...,
        query_args: Incomplete | None = ...,
        sender: Incomplete | None = ...,
        override_num_retries: Incomplete | None = ...,
        retry_handler: Incomplete | None = ...,
        *args,
        **kwargs,
    ): ...
