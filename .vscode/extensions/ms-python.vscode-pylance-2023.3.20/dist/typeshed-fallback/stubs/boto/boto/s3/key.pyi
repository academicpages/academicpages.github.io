from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, overload

class Key:
    DefaultContentType: str
    RestoreBody: str
    BufferSize: Any
    base_user_settable_fields: Any
    base_fields: Any
    bucket: Any
    name: str
    metadata: Any
    cache_control: Any
    content_type: Any
    content_encoding: Any
    content_disposition: Any
    content_language: Any
    filename: Any
    etag: Any
    is_latest: bool
    last_modified: Any
    owner: Any
    path: Any
    resp: Any
    mode: Any
    size: Any
    version_id: Any
    source_version_id: Any
    delete_marker: bool
    encrypted: Any
    ongoing_restore: Any
    expiry_date: Any
    local_hashes: Any
    def __init__(self, bucket: Incomplete | None = ..., name: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    @property
    def provider(self): ...
    key: Any
    md5: Any
    base64md5: Any
    storage_class: Any
    def get_md5_from_hexdigest(self, md5_hexdigest): ...
    def handle_encryption_headers(self, resp): ...
    def handle_version_headers(self, resp, force: bool = ...): ...
    def handle_restore_headers(self, response): ...
    def handle_addl_headers(self, headers): ...
    def open_read(
        self,
        headers: dict[str, str] | None = ...,
        query_args: str = ...,
        override_num_retries: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
    ): ...
    def open_write(self, headers: dict[str, str] | None = ..., override_num_retries: Incomplete | None = ...): ...
    def open(
        self,
        mode: str = ...,
        headers: dict[str, str] | None = ...,
        query_args: Incomplete | None = ...,
        override_num_retries: Incomplete | None = ...,
    ): ...
    closed: bool
    def close(self, fast: bool = ...): ...
    def next(self): ...
    __next__: Any
    def read(self, size: int = ...): ...
    def change_storage_class(self, new_storage_class, dst_bucket: Incomplete | None = ..., validate_dst_bucket: bool = ...): ...
    def copy(
        self,
        dst_bucket,
        dst_key,
        metadata: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        preserve_acl: bool = ...,
        encrypt_key: bool = ...,
        validate_dst_bucket: bool = ...,
    ): ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
    def exists(self, headers: dict[str, str] | None = ...): ...
    def delete(self, headers: dict[str, str] | None = ...): ...
    def get_metadata(self, name): ...
    def set_metadata(self, name, value): ...
    def update_metadata(self, d): ...
    def set_acl(self, acl_str, headers: dict[str, str] | None = ...): ...
    def get_acl(self, headers: dict[str, str] | None = ...): ...
    def get_xml_acl(self, headers: dict[str, str] | None = ...): ...
    def set_xml_acl(self, acl_str, headers: dict[str, str] | None = ...): ...
    def set_canned_acl(self, acl_str, headers: dict[str, str] | None = ...): ...
    def get_redirect(self): ...
    def set_redirect(self, redirect_location, headers: dict[str, str] | None = ...): ...
    def make_public(self, headers: dict[str, str] | None = ...): ...
    def generate_url(
        self,
        expires_in,
        method: str = ...,
        headers: dict[str, str] | None = ...,
        query_auth: bool = ...,
        force_http: bool = ...,
        response_headers: dict[str, str] | None = ...,
        expires_in_absolute: bool = ...,
        version_id: Incomplete | None = ...,
        policy: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        encrypt_key: bool = ...,
    ): ...
    def send_file(
        self,
        fp,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        query_args: Incomplete | None = ...,
        chunked_transfer: bool = ...,
        size: Incomplete | None = ...,
    ): ...
    def should_retry(self, response, chunked_transfer: bool = ...): ...
    def compute_md5(self, fp, size: Incomplete | None = ...): ...
    def set_contents_from_stream(
        self,
        fp,
        headers: dict[str, str] | None = ...,
        replace: bool = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        policy: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        query_args: Incomplete | None = ...,
        size: Incomplete | None = ...,
    ): ...
    def set_contents_from_file(
        self,
        fp,
        headers: dict[str, str] | None = ...,
        replace: bool = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        policy: Incomplete | None = ...,
        md5: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        query_args: Incomplete | None = ...,
        encrypt_key: bool = ...,
        size: Incomplete | None = ...,
        rewind: bool = ...,
    ): ...
    def set_contents_from_filename(
        self,
        filename,
        headers: dict[str, str] | None = ...,
        replace: bool = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        policy: Incomplete | None = ...,
        md5: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        encrypt_key: bool = ...,
    ): ...
    def set_contents_from_string(
        self,
        string_data: str | bytes,
        headers: dict[str, str] | None = ...,
        replace: bool = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        policy: Incomplete | None = ...,
        md5: Incomplete | None = ...,
        reduced_redundancy: bool = ...,
        encrypt_key: bool = ...,
    ) -> None: ...
    def get_file(
        self,
        fp,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        torrent: bool = ...,
        version_id: Incomplete | None = ...,
        override_num_retries: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
    ): ...
    def get_torrent_file(
        self, fp, headers: dict[str, str] | None = ..., cb: Callable[[int, int], object] | None = ..., num_cb: int = ...
    ): ...
    def get_contents_to_file(
        self,
        fp,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        torrent: bool = ...,
        version_id: Incomplete | None = ...,
        res_download_handler: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
    ): ...
    def get_contents_to_filename(
        self,
        filename,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        torrent: bool = ...,
        version_id: Incomplete | None = ...,
        res_download_handler: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
    ): ...
    @overload
    def get_contents_as_string(
        self,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        torrent: bool = ...,
        version_id: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
        encoding: None = ...,
    ) -> bytes: ...
    @overload
    def get_contents_as_string(
        self,
        headers: dict[str, str] | None = ...,
        cb: Callable[[int, int], object] | None = ...,
        num_cb: int = ...,
        torrent: bool = ...,
        version_id: Incomplete | None = ...,
        response_headers: dict[str, str] | None = ...,
        *,
        encoding: str,
    ) -> str: ...
    def add_email_grant(self, permission, email_address, headers: dict[str, str] | None = ...): ...
    def add_user_grant(
        self, permission, user_id, headers: dict[str, str] | None = ..., display_name: Incomplete | None = ...
    ): ...
    def set_remote_metadata(self, metadata_plus, metadata_minus, preserve_acl, headers: dict[str, str] | None = ...): ...
    def restore(self, days, headers: dict[str, str] | None = ...): ...
