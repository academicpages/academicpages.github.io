# SPDX-License-Identifier: MIT

"""
Legacy mid-level functions.
"""

import os

from typing import Optional

from ._password_hasher import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_RANDOM_SALT_LENGTH,
    DEFAULT_TIME_COST,
)
from ._typing import Literal
from .low_level import Type, hash_secret, hash_secret_raw, verify_secret


def hash_password(
    password: bytes,
    salt: Optional[bytes] = None,
    time_cost: int = DEFAULT_TIME_COST,
    memory_cost: int = DEFAULT_MEMORY_COST,
    parallelism: int = DEFAULT_PARALLELISM,
    hash_len: int = DEFAULT_HASH_LENGTH,
    type: Type = Type.I,
) -> bytes:
    """
    Legacy alias for :func:`hash_secret` with default parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)
    return hash_secret(
        password, salt, time_cost, memory_cost, parallelism, hash_len, type
    )


def hash_password_raw(
    password: bytes,
    salt: Optional[bytes] = None,
    time_cost: int = DEFAULT_TIME_COST,
    memory_cost: int = DEFAULT_MEMORY_COST,
    parallelism: int = DEFAULT_PARALLELISM,
    hash_len: int = DEFAULT_HASH_LENGTH,
    type: Type = Type.I,
) -> bytes:
    """
    Legacy alias for :func:`hash_secret_raw` with default parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)
    return hash_secret_raw(
        password, salt, time_cost, memory_cost, parallelism, hash_len, type
    )


def verify_password(
    hash: bytes, password: bytes, type: Type = Type.I
) -> Literal[True]:
    """
    Legacy alias for :func:`verify_secret` with default parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
    return verify_secret(hash, password, type)
