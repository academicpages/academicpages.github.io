from datetime import datetime, timedelta, tzinfo

from pytz import BaseTzInfo

STDOFFSET: timedelta
DSTOFFSET: timedelta
DSTDIFF: timedelta
ZERO: timedelta

class _FallbackLocalTimezone(tzinfo):
    def utcoffset(self, dt: datetime | None) -> timedelta: ...
    def dst(self, dt: datetime | None) -> timedelta: ...
    def tzname(self, dt: datetime | None) -> str: ...

def get_localzone() -> BaseTzInfo: ...

LOCALTZ: BaseTzInfo | _FallbackLocalTimezone
