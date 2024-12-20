# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthorsGetRequestPublishedDatePrecision(str, enum.Enum):
    FULL = "full"
    TIMEZONE_UNKNOWN = "timezone unknown"
    DATE = "date"

    def visit(
        self,
        full: typing.Callable[[], T_Result],
        timezone_unknown: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorsGetRequestPublishedDatePrecision.FULL:
            return full()
        if self is AuthorsGetRequestPublishedDatePrecision.TIMEZONE_UNKNOWN:
            return timezone_unknown()
        if self is AuthorsGetRequestPublishedDatePrecision.DATE:
            return date()
