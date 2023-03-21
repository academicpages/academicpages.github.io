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

-- Language Features - Folding Range --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import Optional

from pygls.lsp.types.basic_structures import (Model, NumType, PartialResultParams,
                                              StaticRegistrationOptions, TextDocumentIdentifier,
                                              TextDocumentRegistrationOptions,
                                              WorkDoneProgressOptions, WorkDoneProgressParams)


class FoldingRangeClientCapabilities(Model):
    dynamic_registration: Optional[bool]
    range_limit: Optional[NumType]
    line_folding_only: Optional[bool]


class FoldingRangeOptions(WorkDoneProgressOptions):
    pass


class FoldingRangeRegistrationOptions(FoldingRangeOptions,
                                      TextDocumentRegistrationOptions,
                                      StaticRegistrationOptions):
    pass


class FoldingRangeParams(WorkDoneProgressParams, PartialResultParams):
    text_document: TextDocumentIdentifier


class FoldingRangeKind(str, enum.Enum):
    Comment = 'comment'
    Imports = 'imports'
    Region = 'region'


class FoldingRange(Model):
    start_line: int
    end_line: int
    start_character: Optional[int]
    end_character: Optional[int]
    kind: Optional[FoldingRangeKind]
