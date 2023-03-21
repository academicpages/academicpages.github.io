from typing import Optional, Set, Type

from cattrs._compat import ExceptionGroup


class StructureHandlerNotFoundError(Exception):
    """Error raised when structuring cannot find a handler for converting inputs into :attr:`type_`."""

    def __init__(self, message: str, type_: Type) -> None:
        super().__init__(message)
        self.type_ = type_


class BaseValidationError(ExceptionGroup):
    cl: Type

    def __new__(cls, message, excs, cl: Type):
        obj = super().__new__(cls, message, excs)
        obj.cl = cl
        return obj

    def derive(self, excs):
        return ClassValidationError(self.message, excs, self.cl)


class IterableValidationError(BaseValidationError):
    """Raised when structuring an iterable."""

    pass


class ClassValidationError(BaseValidationError):
    """Raised when validating a class if any attributes are invalid."""

    pass


class ForbiddenExtraKeysError(Exception):
    """Raised when `forbid_extra_keys` is activated and such extra keys are detected during structuring.

    The attribute `extra_fields` is a sequence of those extra keys, which were the cause of this error,
    and `cl` is the class which was structured with those extra keys.
    """

    def __init__(
        self, message: Optional[str], cl: Type, extra_fields: Set[str]
    ) -> None:
        self.cl = cl
        self.extra_fields = extra_fields

        msg = (
            message
            if message
            else f"Extra fields in constructor for {cl.__name__}: {', '.join(extra_fields)}"
        )

        super().__init__(msg)
