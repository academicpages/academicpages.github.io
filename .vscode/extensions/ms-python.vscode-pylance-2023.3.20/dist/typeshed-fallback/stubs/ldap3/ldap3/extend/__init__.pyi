from _typeshed import Incomplete
from typing import Any

class ExtendedOperationContainer:
    def __init__(self, connection) -> None: ...

class StandardExtendedOperations(ExtendedOperationContainer):
    def who_am_i(self, controls: Incomplete | None = ...): ...
    def modify_password(
        self,
        user: Incomplete | None = ...,
        old_password: Incomplete | None = ...,
        new_password: Incomplete | None = ...,
        hash_algorithm: Incomplete | None = ...,
        salt: Incomplete | None = ...,
        controls: Incomplete | None = ...,
    ): ...
    def paged_search(
        self,
        search_base,
        search_filter,
        search_scope=...,
        dereference_aliases=...,
        attributes: Incomplete | None = ...,
        size_limit: int = ...,
        time_limit: int = ...,
        types_only: bool = ...,
        get_operational_attributes: bool = ...,
        controls: Incomplete | None = ...,
        paged_size: int = ...,
        paged_criticality: bool = ...,
        generator: bool = ...,
    ): ...
    def persistent_search(
        self,
        search_base: str = ...,
        search_filter: str = ...,
        search_scope=...,
        dereference_aliases=...,
        attributes=...,
        size_limit: int = ...,
        time_limit: int = ...,
        controls: Incomplete | None = ...,
        changes_only: bool = ...,
        show_additions: bool = ...,
        show_deletions: bool = ...,
        show_modifications: bool = ...,
        show_dn_modifications: bool = ...,
        notifications: bool = ...,
        streaming: bool = ...,
        callback: Incomplete | None = ...,
    ): ...
    def funnel_search(
        self,
        search_base: str = ...,
        search_filter: str = ...,
        search_scope=...,
        dereference_aliases=...,
        attributes=...,
        size_limit: int = ...,
        time_limit: int = ...,
        controls: Incomplete | None = ...,
        streaming: bool = ...,
        callback: Incomplete | None = ...,
    ): ...

class NovellExtendedOperations(ExtendedOperationContainer):
    def get_bind_dn(self, controls: Incomplete | None = ...): ...
    def get_universal_password(self, user, controls: Incomplete | None = ...): ...
    def set_universal_password(self, user, new_password: Incomplete | None = ..., controls: Incomplete | None = ...): ...
    def list_replicas(self, server_dn, controls: Incomplete | None = ...): ...
    def partition_entry_count(self, partition_dn, controls: Incomplete | None = ...): ...
    def replica_info(self, server_dn, partition_dn, controls: Incomplete | None = ...): ...
    def start_transaction(self, controls: Incomplete | None = ...): ...
    def end_transaction(self, commit: bool = ..., controls: Incomplete | None = ...): ...
    def add_members_to_groups(self, members, groups, fix: bool = ..., transaction: bool = ...): ...
    def remove_members_from_groups(self, members, groups, fix: bool = ..., transaction: bool = ...): ...
    def check_groups_memberships(self, members, groups, fix: bool = ..., transaction: bool = ...): ...

class MicrosoftExtendedOperations(ExtendedOperationContainer):
    def dir_sync(
        self,
        sync_base,
        sync_filter: str = ...,
        attributes=...,
        cookie: Incomplete | None = ...,
        object_security: bool = ...,
        ancestors_first: bool = ...,
        public_data_only: bool = ...,
        incremental_values: bool = ...,
        max_length: int = ...,
        hex_guid: bool = ...,
    ): ...
    def modify_password(self, user, new_password, old_password: Incomplete | None = ..., controls: Incomplete | None = ...): ...
    def unlock_account(self, user): ...
    def add_members_to_groups(self, members, groups, fix: bool = ...): ...
    def remove_members_from_groups(self, members, groups, fix: bool = ...): ...
    def persistent_search(
        self, search_base: str = ..., search_scope=..., attributes=..., streaming: bool = ..., callback: Incomplete | None = ...
    ): ...

class ExtendedOperationsRoot(ExtendedOperationContainer):
    standard: Any
    novell: Any
    microsoft: Any
    def __init__(self, connection) -> None: ...
