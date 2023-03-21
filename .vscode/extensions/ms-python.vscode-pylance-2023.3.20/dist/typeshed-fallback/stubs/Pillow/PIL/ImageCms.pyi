from _typeshed import Incomplete
from enum import IntEnum
from typing import Any
from typing_extensions import Literal

from .Image import ImagePointHandler

DESCRIPTION: str
VERSION: str
core: Any

class Intent(IntEnum):
    PERCEPTUAL: int
    RELATIVE_COLORIMETRIC: int
    SATURATION: int
    ABSOLUTE_COLORIMETRIC: int

INTENT_PERCEPTUAL: Literal[Intent.PERCEPTUAL]
INTENT_RELATIVE_COLORIMETRIC: Literal[Intent.RELATIVE_COLORIMETRIC]
INTENT_SATURATION: Literal[Intent.SATURATION]
INTENT_ABSOLUTE_COLORIMETRIC: Literal[Intent.ABSOLUTE_COLORIMETRIC]

class Direction(IntEnum):
    INPUT: int
    OUTPUT: int
    PROOF: int

DIRECTION_INPUT: Literal[Direction.INPUT]
DIRECTION_OUTPUT: Literal[Direction.OUTPUT]
DIRECTION_PROOF: Literal[Direction.PROOF]

FLAGS: Any

class ImageCmsProfile:
    def __init__(self, profile) -> None: ...
    def tobytes(self): ...

class ImageCmsTransform(ImagePointHandler):
    transform: Any
    input_mode: Any
    output_mode: Any
    output_profile: Any
    def __init__(
        self,
        input,
        output,
        input_mode,
        output_mode,
        intent=...,
        proof: Incomplete | None = ...,
        proof_intent=...,
        flags: int = ...,
    ) -> None: ...
    def point(self, im): ...
    def apply(self, im, imOut: Incomplete | None = ...): ...
    def apply_in_place(self, im): ...

def get_display_profile(handle: Incomplete | None = ...): ...

class PyCMSError(Exception): ...

def profileToProfile(
    im,
    inputProfile,
    outputProfile,
    renderingIntent=...,
    outputMode: Incomplete | None = ...,
    inPlace: bool = ...,
    flags: int = ...,
): ...
def getOpenProfile(profileFilename): ...
def buildTransform(inputProfile, outputProfile, inMode, outMode, renderingIntent=..., flags: int = ...): ...
def buildProofTransform(
    inputProfile, outputProfile, proofProfile, inMode, outMode, renderingIntent=..., proofRenderingIntent=..., flags=...
): ...

buildTransformFromOpenProfiles = buildTransform
buildProofTransformFromOpenProfiles = buildProofTransform

def applyTransform(im, transform, inPlace: bool = ...): ...
def createProfile(colorSpace, colorTemp: int = ...): ...
def getProfileName(profile): ...
def getProfileInfo(profile): ...
def getProfileCopyright(profile): ...
def getProfileManufacturer(profile): ...
def getProfileModel(profile): ...
def getProfileDescription(profile): ...
def getDefaultIntent(profile): ...
def isIntentSupported(profile, intent, direction): ...
def versions(): ...
