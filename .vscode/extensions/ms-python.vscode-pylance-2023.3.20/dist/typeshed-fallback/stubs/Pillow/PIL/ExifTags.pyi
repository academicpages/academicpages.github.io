from collections.abc import Mapping
from enum import IntEnum

TAGS: Mapping[int, str]
GPSTAGS: Mapping[int, str]

class Interop(IntEnum):
    InteropIndex: int
    InteropVersion: int
    RelatedImageFileFormat: int
    RelatedImageWidth: int
    RleatedImageHeight: int

class IFD(IntEnum):
    Exif: int
    GPSInfo: int
    Makernote: int
    Interop: int
    IFD1: int

class LightSource(IntEnum):
    Unknown: int
    Daylight: int
    Fluorescent: int
    Tungsten: int
    Flash: int
    Fine: int
    Cloudy: int
    Shade: int
    DaylightFluorescent: int
    DayWhiteFluorescent: int
    CoolWhiteFluorescent: int
    WhiteFluorescent: int
    StandardLightA: int
    StandardLightB: int
    StandardLightC: int
    D55: int
    D65: int
    D75: int
    D50: int
    ISO: int
    Other: int
