from _typeshed import Incomplete
from typing import Any

def constant_to_class_kind(value): ...
def constant_to_attribute_usage(value): ...
def attribute_usage_to_constant(value): ...
def quoted_string_to_list(quoted_string): ...
def oids_string_to_list(oid_string): ...
def extension_to_tuple(extension_string): ...
def list_to_string(list_object): ...

class BaseServerInfo:
    raw: Any
    def __init__(self, raw_attributes) -> None: ...
    @classmethod
    def from_json(cls, json_definition, schema: Incomplete | None = ..., custom_formatter: Incomplete | None = ...): ...
    @classmethod
    def from_file(cls, target, schema: Incomplete | None = ..., custom_formatter: Incomplete | None = ...): ...
    def to_file(self, target, indent: int = ..., sort: bool = ...) -> None: ...
    def to_json(self, indent: int = ..., sort: bool = ...): ...

class DsaInfo(BaseServerInfo):
    alt_servers: Any
    naming_contexts: Any
    supported_controls: Any
    supported_extensions: Any
    supported_features: Any
    supported_ldap_versions: Any
    supported_sasl_mechanisms: Any
    vendor_name: Any
    vendor_version: Any
    schema_entry: Any
    other: Any
    def __init__(self, attributes, raw_attributes) -> None: ...

class SchemaInfo(BaseServerInfo):
    schema_entry: Any
    create_time_stamp: Any
    modify_time_stamp: Any
    attribute_types: Any
    object_classes: Any
    matching_rules: Any
    matching_rule_uses: Any
    dit_content_rules: Any
    dit_structure_rules: Any
    name_forms: Any
    ldap_syntaxes: Any
    other: Any
    def __init__(self, schema_entry, attributes, raw_attributes) -> None: ...
    def is_valid(self): ...

class BaseObjectInfo:
    oid: Any
    name: Any
    description: Any
    obsolete: Any
    extensions: Any
    experimental: Any
    raw_definition: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...
    @property
    def oid_info(self): ...
    @classmethod
    def from_definition(cls, definitions): ...

class MatchingRuleInfo(BaseObjectInfo):
    syntax: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        syntax: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class MatchingRuleUseInfo(BaseObjectInfo):
    apply_to: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        apply_to: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class ObjectClassInfo(BaseObjectInfo):
    superior: Any
    kind: Any
    must_contain: Any
    may_contain: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        superior: Incomplete | None = ...,
        kind: Incomplete | None = ...,
        must_contain: Incomplete | None = ...,
        may_contain: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class AttributeTypeInfo(BaseObjectInfo):
    superior: Any
    equality: Any
    ordering: Any
    substring: Any
    syntax: Any
    min_length: Any
    single_value: Any
    collective: Any
    no_user_modification: Any
    usage: Any
    mandatory_in: Any
    optional_in: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        superior: Incomplete | None = ...,
        equality: Incomplete | None = ...,
        ordering: Incomplete | None = ...,
        substring: Incomplete | None = ...,
        syntax: Incomplete | None = ...,
        min_length: Incomplete | None = ...,
        single_value: bool = ...,
        collective: bool = ...,
        no_user_modification: bool = ...,
        usage: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class LdapSyntaxInfo(BaseObjectInfo):
    def __init__(
        self,
        oid: Incomplete | None = ...,
        description: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class DitContentRuleInfo(BaseObjectInfo):
    auxiliary_classes: Any
    must_contain: Any
    may_contain: Any
    not_contains: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        auxiliary_classes: Incomplete | None = ...,
        must_contain: Incomplete | None = ...,
        may_contain: Incomplete | None = ...,
        not_contains: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class DitStructureRuleInfo(BaseObjectInfo):
    superior: Any
    name_form: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        name_form: Incomplete | None = ...,
        superior: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...

class NameFormInfo(BaseObjectInfo):
    object_class: Any
    must_contain: Any
    may_contain: Any
    def __init__(
        self,
        oid: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        obsolete: bool = ...,
        object_class: Incomplete | None = ...,
        must_contain: Incomplete | None = ...,
        may_contain: Incomplete | None = ...,
        extensions: Incomplete | None = ...,
        experimental: Incomplete | None = ...,
        definition: Incomplete | None = ...,
    ) -> None: ...
