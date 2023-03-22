# SPDX-License-Identifier: MIT

"""
The secure Argon2 password hashing algorithm.
"""

from . import exceptions, low_level, profiles
from ._legacy import hash_password, hash_password_raw, verify_password
from ._password_hasher import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_RANDOM_SALT_LENGTH,
    DEFAULT_TIME_COST,
    PasswordHasher,
)
from ._utils import Parameters, extract_parameters
from .low_level import Type


__version__ = "21.3.0"

__title__ = "argon2-cffi"
__description__ = (__doc__ or "").strip()
__url__ = "https://argon2-cffi.readthedocs.io/"
__uri__ = __url__

__author__ = "Hynek Schlawack"
__email__ = "hs@ox.cx"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2015 " + __author__


__all__ = [
    "DEFAULT_HASH_LENGTH",
    "DEFAULT_MEMORY_COST",
    "DEFAULT_PARALLELISM",
    "DEFAULT_RANDOM_SALT_LENGTH",
    "DEFAULT_TIME_COST",
    "Parameters",
    "PasswordHasher",
    "Type",
    "exceptions",
    "extract_parameters",
    "hash_password",
    "hash_password_raw",
    "low_level",
    "profiles",
    "verify_password",
]
