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

-- Language Features - Document Symbol --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import List, Optional

from pygls.lsp.types.basic_structures import (Location, Model, PartialResultParams, Range,
                                              TextDocumentIdentifier, WorkDoneProgressOptions,
                                              WorkDoneProgressParams)


class SymbolKind(enum.IntEnum):
    File = 1
    Module = 2
    Namespace = 3
    Package = 4
    Class = 5
    Method = 6
    Property = 7
    Field = 8
    Constructor = 9
    Enum = 10
    Interface = 11
    Function = 12
    Variable = 13
    Constant = 14
    String = 15
    Number = 16
    Boolean = 17
    Array = 18
    Object = 19
    Key = 20
    Null = 21
    EnumMember = 22
    Struct = 23
    Event = 24
    Operator = 25
    TypeParameter = 26


class SymbolTag(enum.IntEnum):
    Deprecated = 1


class WorkspaceCapabilitiesSymbolKind(Model):
    value_set: Optional[List[SymbolKind]]


class WorkspaceCapabilitiesTagSupport(Model):
    value_set: List[SymbolKind]


class DocumentSymbolCapabilitiesTagSupport(Model):
    value_set: List[SymbolTag]


class DocumentSymbolClientCapabilities(Model):
    dynamic_registration: Optional[bool]
    symbol_kind: Optional[WorkspaceCapabilitiesSymbolKind]
    hierarchical_document_symbol_support: Optional[bool]
    tag_support: Optional[WorkspaceCapabilitiesTagSupport]
    label_support: Optional[bool]


class DocumentSymbolOptions(WorkDoneProgressOptions):
    label: Optional[str]


class DocumentSymbolParams(WorkDoneProgressParams, PartialResultParams):
    text_document: TextDocumentIdentifier


class DocumentSymbol(Model):
    name: str
    kind: SymbolKind
    range: Range
    selection_range: Range
    detail: Optional[str]
    children: Optional[List['DocumentSymbol']]
    tags: Optional[List[SymbolTag]]
    deprecated: Optional[bool]


DocumentSymbol.update_forward_refs()


class SymbolInformation(Model):
    name: str
    kind: SymbolKind
    location: Location
    container_name: Optional[str]
    tags: Optional[List[SymbolTag]]
    deprecated: Optional[bool]
