from _typeshed import ReadableBuffer, SliceableBuffer
from collections.abc import Iterable, Sequence
from typing import SupportsFloat, TypeVar
from typing_extensions import SupportsIndex, TypeAlias

from Xlib._typing import Unused
from Xlib.display import Display
from Xlib.protocol import display, request, rq
from Xlib.xobject import drawable, resource

_T = TypeVar("_T")
_Floatable: TypeAlias = SupportsFloat | SupportsIndex | str | ReadableBuffer

extname: str
PropertyDeleted: int
PropertyCreated: int
PropertyModified: int
NotifyNormal: int
NotifyGrab: int
NotifyUngrab: int
NotifyWhileGrabbed: int
NotifyPassiveGrab: int
NotifyPassiveUngrab: int
NotifyAncestor: int
NotifyVirtual: int
NotifyInferior: int
NotifyNonlinear: int
NotifyNonlinearVirtual: int
NotifyPointer: int
NotifyPointerRoot: int
NotifyDetailNone: int
GrabtypeButton: int
GrabtypeKeycode: int
GrabtypeEnter: int
GrabtypeFocusIn: int
GrabtypeTouchBegin: int
AnyModifier: int
AnyButton: int
AnyKeycode: int
AsyncDevice: int
SyncDevice: int
ReplayDevice: int
AsyncPairedDevice: int
AsyncPair: int
SyncPair: int
SlaveSwitch: int
DeviceChange: int
MasterAdded: int
MasterRemoved: int
SlaveAdded: int
SlaveRemoved: int
SlaveAttached: int
SlaveDetached: int
DeviceEnabled: int
DeviceDisabled: int
AddMaster: int
RemoveMaster: int
AttachSlave: int
DetachSlave: int
AttachToMaster: int
Floating: int
ModeRelative: int
ModeAbsolute: int
MasterPointer: int
MasterKeyboard: int
SlavePointer: int
SlaveKeyboard: int
FloatingSlave: int
KeyClass: int
ButtonClass: int
ValuatorClass: int
ScrollClass: int
TouchClass: int
KeyRepeat: int
AllDevices: int
AllMasterDevices: int
DeviceChanged: int
KeyPress: int
KeyRelease: int
ButtonPress: int
ButtonRelease: int
Motion: int
Enter: int
Leave: int
FocusIn: int
FocusOut: int
HierarchyChanged: int
PropertyEvent: int
RawKeyPress: int
RawKeyRelease: int
RawButtonPress: int
RawButtonRelease: int
RawMotion: int
DeviceChangedMask: int
KeyPressMask: int
KeyReleaseMask: int
ButtonPressMask: int
ButtonReleaseMask: int
MotionMask: int
EnterMask: int
LeaveMask: int
FocusInMask: int
FocusOutMask: int
HierarchyChangedMask: int
PropertyEventMask: int
RawKeyPressMask: int
RawKeyReleaseMask: int
RawButtonPressMask: int
RawButtonReleaseMask: int
RawMotionMask: int
GrabModeSync: int
GrabModeAsync: int
GrabModeTouch: int
DEVICEID = rq.Card16
DEVICE = rq.Card16
DEVICEUSE = rq.Card8
PROPERTY_TYPE_FLOAT: str

# ignore[override] because of Liskov substitution principle violations
class FP1616(rq.Int32):
    def check_value(self, value: float) -> int: ...  # type: ignore[override]
    def parse_value(self, value: _Floatable, display: Unused) -> float: ...  # type: ignore[override]

class FP3232(rq.ValueField):
    structcode: str
    def check_value(self, value: _T) -> _T: ...  # type: ignore[override]
    def parse_value(self, value: tuple[_Floatable, _Floatable], display: Unused) -> float: ...  # type: ignore[override]

class XIQueryVersion(rq.ReplyRequest): ...

def query_version(self: Display | resource.Resource) -> XIQueryVersion: ...

class Mask(rq.List):
    def __init__(self, name: str) -> None: ...
    def pack_value(self, val: int | Iterable[int]) -> tuple[bytes, int, None]: ...  # type: ignore[override]

EventMask: rq.Struct

class XISelectEvents(rq.Request): ...

def select_events(self: drawable.Window, event_masks: Sequence[tuple[int, Sequence[int]]]) -> XISelectEvents: ...

AnyInfo: rq.Struct

class ButtonMask:
    def __init__(self, value: int, length: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...
    def __len__(self) -> int: ...

class ButtonState(rq.ValueField):
    structcode: None
    def __init__(self, name: str) -> None: ...
    def parse_binary_value(  # type: ignore[override]  # length: None will error. See: https://github.com/python-xlib/python-xlib/pull/248
        self, data: SliceableBuffer, display: Unused, length: int, fmt: Unused
    ) -> tuple[ButtonMask, SliceableBuffer]: ...

ButtonInfo: rq.Struct
KeyInfo: rq.Struct
ValuatorInfo: rq.Struct
ScrollInfo: rq.Struct
TouchInfo: rq.Struct
INFO_CLASSES: dict[int, rq.Struct]

class ClassInfoClass:
    structcode: None
    def parse_binary(self, data: SliceableBuffer, display: display.Display | None) -> tuple[rq.DictWrapper, SliceableBuffer]: ...

ClassInfo: ClassInfoClass
DeviceInfo: rq.Struct

class XIQueryDevice(rq.ReplyRequest): ...

def query_device(self: Display | resource.Resource, deviceid: int) -> XIQueryDevice: ...

class XIListProperties(rq.ReplyRequest): ...

def list_device_properties(self: Display | resource.Resource, deviceid: int) -> XIListProperties: ...

class XIGetProperty(rq.ReplyRequest): ...

def get_device_property(
    self: Display | resource.Resource, deviceid: int, property: int, type: int, offset: int, length: int, delete: int = ...
) -> XIGetProperty: ...

class XIChangeProperty(rq.Request): ...

def change_device_property(
    self: Display | resource.Resource, deviceid: int, property: int, type: int, mode: int, value: Sequence[float] | Sequence[str]
) -> XIChangeProperty: ...

class XIDeleteProperty(rq.Request): ...

def delete_device_property(self: Display | resource.Resource, deviceid: int, property: int) -> XIDeleteProperty: ...

class XIGrabDevice(rq.ReplyRequest): ...

def grab_device(
    self: drawable.Window,
    deviceid: int,
    time: int,
    grab_mode: int,
    paired_device_mode: int,
    owner_events: bool,
    event_mask: Sequence[int],
) -> XIGrabDevice: ...

class XIUngrabDevice(rq.Request): ...

def ungrab_device(self: Display | resource.Resource, deviceid: int, time: int) -> XIUngrabDevice: ...

class XIPassiveGrabDevice(rq.ReplyRequest): ...

def passive_grab_device(
    self: drawable.Window,
    deviceid: int,
    time: int,
    detail: int,
    grab_type: int,
    grab_mode: int,
    paired_device_mode: int,
    owner_events: bool,
    event_mask: Sequence[int],
    modifiers: Sequence[int],
) -> XIPassiveGrabDevice: ...
def grab_keycode(
    self: drawable.Window,
    deviceid: int,
    time: int,
    keycode: int,
    grab_mode: int,
    paired_device_mode: int,
    owner_events: bool,
    event_mask: Sequence[int],
    modifiers: Sequence[int],
) -> XIPassiveGrabDevice: ...

class XIPassiveUngrabDevice(rq.Request): ...

def passive_ungrab_device(
    self: drawable.Window, deviceid: int, detail: int, grab_type: int, modifiers: Sequence[int]
) -> XIPassiveUngrabDevice: ...
def ungrab_keycode(self: drawable.Window, deviceid: int, keycode: int, modifiers: Sequence[int]) -> XIPassiveUngrabDevice: ...

HierarchyInfo: rq.Struct
HierarchyEventData: rq.Struct
ModifierInfo: rq.Struct
GroupInfo: rq.Struct
DeviceEventData: rq.Struct
DeviceChangedEventData: rq.Struct
PropertyEventData: rq.Struct

def init(disp: Display, info: request.QueryExtension) -> None: ...
