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

-- Window --

Class attributes are named with camel case notation because client is expecting
that.
"""
import enum
from typing import Callable, List, Optional

from pygls.lsp.types.basic_structures import URI, Model, NumType, ProgressToken, Range


class MessageType(enum.IntEnum):
    Error = 1
    Warning = 2
    Info = 3
    Log = 4


class ShowMessageParams(Model):
    type: MessageType
    message: str


class MessageActionItem(Model):
    title: str


class ShowMessageRequestParams(Model):
    type: MessageType
    message: str
    actions: Optional[List[MessageActionItem]]


class ShowDocumentClientCapabilities(Model):
    support: Optional[bool]


class ShowDocumentParams(Model):
    uri: URI
    external: Optional[bool]
    take_focus: Optional[bool]
    selection: Optional[Range]


class ShowDocumentResult(Model):
    success: bool


class ShowMessageRequestActionItem(Model):
    additional_properties_support: Optional[bool]


class ShowMessageRequestClientCapabilities(Model):
    message_action_item: Optional[ShowMessageRequestActionItem]


class LogMessageParams(Model):
    type: NumType
    message: str


class WorkDoneProgressCreateParams(Model):
    token: ProgressToken


class WorkDoneProgressCancelParams(Model):
    token: ProgressToken


ShowDocumentCallbackType = Callable[[ShowDocumentResult], None]
