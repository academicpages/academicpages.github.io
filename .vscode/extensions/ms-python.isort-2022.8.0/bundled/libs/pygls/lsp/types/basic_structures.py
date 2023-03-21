############################################################################
# Original work Copyright 2017 Palantir Technologies, Inc.                 #
# Original work licensed under the MIT License.                            #
# See ThirdPartyNotices.txt in the project root for license information.   #
# All modifications Copyright (c) Open Law Library. All rights reserved.   #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
"""This module contains Language Server Protocol types
https://microsoft.github.io/language-server-protocol/specification

-- Basic Structures --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import Any, Callable, Dict, List, NewType, Optional, TypeVar, Union

from pydantic import BaseModel, root_validator
from typeguard import check_type

ChangeAnnotationIdentifier = NewType('ChangeAnnotationIdentifier', str)
NumType = Union[int, float]
ProgressToken = Union[int, str]
URI = NewType('URI', str)
T = TypeVar('T')

ConfigCallbackType = Callable[[List[Any]], None]


def snake_to_camel(string: str) -> str:
    return ''.join(
        word.capitalize() if idx > 0 else word
        for idx, word in enumerate(string.split('_'))
    )


class Model(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
        fields = {
            'from_': 'from'
        }

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        # Serialize (.json()) fields that has default value which is not None
        for name, field in self.__fields__.items():
            if getattr(field, 'default', None) is not None:
                self.__fields_set__.add(name)


class JsonRpcMessage(Model):
    """A base json rpc message defined by LSP."""
    jsonrpc: str


class JsonRPCNotification(JsonRpcMessage):
    """A class that represents json rpc notification message."""
    method: str
    params: Any


class JsonRPCRequestMessage(JsonRpcMessage):
    """A class that represents json rpc request message."""
    id: Any
    method: str
    params: Any

    @root_validator
    def check_result_or_error(cls, values):
        # Workaround until pydantic supports StrictUnion
        # https://github.com/samuelcolvin/pydantic/pull/2092
        id_val = values.get('id')
        check_type('', id_val, Union[int, str])

        return values


class JsonRPCResponseMessage(JsonRpcMessage):
    """A class that represents json rpc response message."""
    id: Any
    result: Any
    error: Any

    @root_validator
    def check_result_or_error(cls, values):
        # Workaround until pydantic supports StrictUnion
        # https://github.com/samuelcolvin/pydantic/pull/2092
        id_val = values.get('id')
        check_type('', id_val, Union[int, str])

        result_val, error_val = values.get('result'), values.get('error')

        if result_val is not None and error_val is not None:
            raise ValueError('Fields "result" and "error" are both set!')

        return values


class Position(Model):
    line: int
    character: int

    def __eq__(self, other):
        return (
            isinstance(other, Position)
            and self.line == other.line
            and self.character == other.character)

    def __ge__(self, other):
        line_gt = self.line > other.line

        if line_gt:
            return line_gt

        if self.line == other.line:
            return self.character >= other.character

        return False

    def __gt__(self, other):
        line_gt = self.line > other.line

        if line_gt:
            return line_gt

        if self.line == other.line:
            return self.character > other.character

        return False

    def __le__(self, other):
        line_lt = self.line < other.line

        if line_lt:
            return line_lt

        if self.line == other.line:
            return self.character <= other.character

        return False

    def __lt__(self, other):
        line_lt = self.line < other.line

        if line_lt:
            return line_lt

        if self.line == other.line:
            return self.character < other.character

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.line, self.character))

    def __iter__(self):
        return iter((self.line, self.character))

    def __repr__(self):
        return f'{self.line}:{self.character}'


class Range(Model):
    start: Position
    end: Position

    def __eq__(self, other):
        return (
            isinstance(other, Range)
            and self.start == other.start
            and self.end == other.end)

    def __hash__(self):
        return hash((self.start, self.end))

    def __iter__(self):
        return iter((self.start, self.end))

    def __repr__(self):
        return f'{self.start!r}-{self.end!r}'


class Location(Model):
    uri: str
    range: Range

    def __eq__(self, other):
        return (
            isinstance(other, Location)
            and self.uri == other.uri
            and self.range == other.range)

    def __repr__(self):
        return f"{self.uri}:{self.range!r}"


class Trace(str, enum.Enum):
    Off = 'off'
    Messages = 'messages'
    Verbose = 'verbose'


class CancelParams(Model):
    id: Union[int, str]


class ProgressParams(Model):
    token: ProgressToken
    value: Any


class LogTraceParams(Model):
    message: str
    verbose: Optional[str]


class SetTraceParams(Model):
    value: Trace


class RegularExpressionsClientCapabilities(Model):
    engine: str
    version: Optional[str]


class ResolveSupportClientCapabilities(Model):
    properties: List[str]


class LocationLink(Model):
    target_uri: str
    target_range: Range
    target_selection_range: Range
    origin_selection_range: Optional[Range]


class DiagnosticSeverity(enum.IntEnum):
    Error = 1
    Warning = 2
    Information = 3
    Hint = 4


class DiagnosticTag(enum.IntEnum):
    Unnecessary = 1
    Deprecated = 2


class DiagnosticRelatedInformation(Model):
    location: Location
    message: str


class CodeDescription(Model):
    href: URI


class Diagnostic(Model):
    range: Range
    message: str
    severity: Optional[DiagnosticSeverity]
    code: Optional[Union[int, str]]
    code_description: Optional[CodeDescription]
    source: Optional[str]
    related_information: Optional[List[DiagnosticRelatedInformation]]
    tags: Optional[List[DiagnosticTag]]
    data: Optional[Any]


class Command(Model):
    title: str
    command: str
    arguments: Optional[List[Any]]


class TextEdit(Model):
    range: Range
    new_text: str


class AnnotatedTextEdit(TextEdit):
    annotation_id: ChangeAnnotationIdentifier


class ChangeAnnotation(Model):
    label: str
    needs_confirmation: Optional[bool]
    description: Optional[str]


class ResourceOperationKind(str, enum.Enum):
    Create = 'create'
    Rename = 'rename'
    Delete = 'delete'


class CreateFileOptions(Model):
    overwrite: Optional[bool]
    ignore_if_exists: Optional[bool]


class CreateFile(Model):
    kind: ResourceOperationKind = ResourceOperationKind.Create
    uri: str
    options: Optional[CreateFileOptions]
    annotation_id: Optional[ChangeAnnotationIdentifier]


class RenameFileOptions(Model):
    overwrite: Optional[bool]
    ignore_if_exists: Optional[bool]


class RenameFile(Model):
    kind: ResourceOperationKind = ResourceOperationKind.Rename
    old_uri: str
    new_uri: str
    options: Optional[RenameFileOptions]
    annotation_id: Optional[ChangeAnnotationIdentifier]


class DeleteFileOptions(Model):
    recursive: Optional[bool]
    ignore_if_exists: Optional[bool]


class DeleteFile(Model):
    kind: ResourceOperationKind = ResourceOperationKind.Delete
    uri: str
    options: Optional[DeleteFileOptions]
    annotation_id: Optional[ChangeAnnotationIdentifier]


class FailureHandlingKind(str, enum.Enum):
    Abort = 'abort'
    Transactional = 'transactional'
    TextOnlyTransactional = 'textOnlyTransactional'
    Undo = 'undo'


class ChangeAnnotationSupport(Model):
    groups_on_label: Optional[bool]


class WorkspaceEditClientCapabilities(Model):
    document_changes: Optional[bool]
    resource_operations: Optional[List[ResourceOperationKind]]
    failure_handling: Optional[FailureHandlingKind]
    normalizes_line_endings: Optional[bool]
    change_annotation_support: Optional[ChangeAnnotationSupport]


class TextDocumentIdentifier(Model):
    uri: str


class TextDocumentItem(Model):
    uri: str
    language_id: str
    version: NumType
    text: str


class VersionedTextDocumentIdentifier(TextDocumentIdentifier):
    version: NumType


class OptionalVersionedTextDocumentIdentifier(TextDocumentIdentifier):
    version: Optional[NumType]


class TextDocumentEdit(Model):
    text_document: OptionalVersionedTextDocumentIdentifier
    edits: List[Union[TextEdit, AnnotatedTextEdit]]


class TextDocumentPositionParams(Model):
    text_document: TextDocumentIdentifier
    position: Position


class DocumentFilter(Model):
    language: Optional[str]
    scheme: Optional[str]
    pattern: Optional[str]


DocumentSelector = List[DocumentFilter]


class StaticRegistrationOptions(Model):
    id: Optional[str]


class TextDocumentRegistrationOptions(Model):
    document_selector: Optional[DocumentSelector]


class MarkupKind(str, enum.Enum):
    PlainText = 'plaintext'
    Markdown = 'markdown'


class MarkupContent(Model):
    kind: MarkupKind
    value: str


class WorkspaceEdit(Model):
    changes: Optional[Dict[str, List[TextEdit]]]
    document_changes: Optional[Any]
    change_annotations: Optional[Dict[ChangeAnnotationIdentifier, ChangeAnnotation]]

    @root_validator
    def check_result_or_error(cls, values):
        # Workaround until pydantic supports StrictUnion
        # https://github.com/samuelcolvin/pydantic/pull/2092

        document_changes_val = values.get('document_changes')
        check_type(
            '',
            document_changes_val,
            Optional[Union[
                List[TextDocumentEdit],
                List[Union[TextDocumentEdit, CreateFile, RenameFile, DeleteFile]],
            ]]
        )

        return values


class WorkDoneProgressBegin(Model):
    kind: str = 'begin'
    title: str
    cancellable: Optional[bool]
    message: Optional[str]
    percentage: Optional[NumType]


class WorkDoneProgressReport(Model):
    kind: str = 'report'
    cancellable: Optional[bool]
    message: Optional[str]
    percentage: Optional[NumType]


class WorkDoneProgressEnd(Model):
    kind: str = 'end'
    message: Optional[str]


class WorkDoneProgressParams(Model):
    work_done_token: Optional[ProgressToken]


class WorkDoneProgressOptions(Model):
    work_done_progress: Optional[ProgressToken]


class PartialResultParams(Model):
    partial_result_token: Optional[ProgressToken]
