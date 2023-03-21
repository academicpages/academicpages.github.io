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

-- Language Features - Signature Help --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import List, Optional, Tuple, Union

from pygls.lsp.types.basic_structures import (MarkupContent, MarkupKind, Model, NumType,
                                              TextDocumentPositionParams, WorkDoneProgressOptions,
                                              WorkDoneProgressParams)


class SignatureHelpInformationParameterInformationClientCapabilities(Model):
    label_offset_support: Optional[bool]


class SignatureHelpInformationClientCapabilities(Model):
    documentation_format: Optional[List[MarkupKind]]
    parameter_information: Optional[SignatureHelpInformationParameterInformationClientCapabilities]
    active_parameter_support: Optional[bool]


class SignatureHelpClientCapabilities(Model):
    dynamic_registration: Optional[bool]
    signature_information: Optional[SignatureHelpInformationClientCapabilities]
    context_support: Optional[bool]


class SignatureHelpOptions(WorkDoneProgressOptions):
    trigger_characters: Optional[List[str]]
    retrigger_characters: Optional[List[str]]


class SignatureHelpTriggerKind(enum.IntEnum):
    Invoked = 1
    TriggerCharacter = 2
    ContentChange = 3


class ParameterInformation(Model):
    label: Union[str, Tuple[int, int]]
    documentation: Optional[Union[str, MarkupContent]]


class SignatureInformation(Model):
    label: str
    documentation: Optional[Union[str, MarkupContent]]
    parameters: Optional[List[ParameterInformation]]
    active_parameter: Optional[int]


class SignatureHelp(Model):
    signatures: List[SignatureInformation]
    active_signature: Optional[NumType]
    active_parameter: Optional[NumType]


class SignatureHelpContext(Model):
    trigger_kind: SignatureHelpTriggerKind
    is_retrigger: bool
    trigger_character: Optional[str]
    active_signature_help: Optional[SignatureHelp]


class SignatureHelpParams(TextDocumentPositionParams, WorkDoneProgressParams):
    context: Optional[SignatureHelpContext]
