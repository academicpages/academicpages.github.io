"""
Timezone utilities

Just UTC-awareness right now
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from datetime import tzinfo, timedelta, datetime

# constant for zero offset
ZERO = timedelta(0)

class tzUTC(tzinfo):
    """tzinfo object for UTC (zero offset)"""

    def utcoffset(self, d):
        return ZERO

    def dst(self, d):
        return ZERO

UTC = tzUTC()

def utc_aware(unaware):
    """decorator for adding UTC tzinfo to datetime's utcfoo methods"""
    def utc_method(*args, **kwargs):
        dt = unaware(*args, **kwargs)
        return dt.replace(tzinfo=UTC)
    return utc_method

utcfromtimestamp = utc_aware(datetime.utcfromtimestamp)
utcnow = utc_aware(datetime.utcnow)

def isoformat(dt):
    """Return iso-formatted timestamp
    
    Like .isoformat(), but uses Z for UTC instead of +00:00
    """
    return dt.isoformat().replace('+00:00', 'Z')
