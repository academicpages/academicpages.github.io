from _typeshed import Incomplete
from collections.abc import Iterable

import _win32typing

error: Incomplete
langid: Incomplete

def AddSourceToRegistry(
    appName, msgDLL: Incomplete | None = ..., eventLogType: str = ..., eventLogFlags: Incomplete | None = ...
) -> None: ...
def RemoveSourceFromRegistry(appName, eventLogType: str = ...) -> None: ...
def ReportEvent(
    appName: str,
    eventID: int,
    eventCategory: int = ...,
    eventType: int = ...,
    strings: Iterable[str] | None = ...,
    data: bytes | None = ...,
    sid: _win32typing.PySID | None = ...,
) -> None: ...
def FormatMessage(eventLogRecord: _win32typing.PyEventLogRecord, logType: str = ...): ...
def SafeFormatMessage(eventLogRecord, logType: Incomplete | None = ...): ...
def FeedEventLogRecords(feeder, machineName: Incomplete | None = ..., logName: str = ..., readFlags: Incomplete | None = ...): ...
