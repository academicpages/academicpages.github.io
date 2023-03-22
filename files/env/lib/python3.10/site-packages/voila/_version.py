#############################################################################
# Copyright (c) 2018, Voilà Contributors                                    #
# Copyright (c) 2018, QuantStack                                            #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import re

from collections import namedtuple

# Use "hatch version xx.yy.zz" to handle version changes
__version__ = "0.4.0"

# PEP440 version parser
_version_regex = re.compile(
    r"""
  (?P<major>\d+)
  \.
  (?P<minor>\d+)
  \.
  (?P<micro>\d+)
  (?P<releaselevel>((a|b|rc|\.dev)))?
  (?P<serial>\d+)?
  """,
    re.VERBOSE,
)

_version_fields = _version_regex.match(__version__).groupdict()  # type:ignore

VersionInfo = namedtuple("VersionInfo", ["major", "minor", "micro", "releaselevel", "serial"])

version_info = VersionInfo(
    *[
        field
        for field in (
            int(_version_fields["major"]),
            int(_version_fields["minor"]),
            int(_version_fields["micro"]),
            _version_fields["releaselevel"] or "",
            _version_fields["serial"] or "",
        )
    ]
)
