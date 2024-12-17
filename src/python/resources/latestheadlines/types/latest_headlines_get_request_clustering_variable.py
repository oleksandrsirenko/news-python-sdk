# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LatestHeadlinesGetRequestClusteringVariable(str, enum.Enum):
    CONTENT = "content"
    TITLE = "title"
    SUMMARY = "summary"

    def visit(
        self,
        content: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        summary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LatestHeadlinesGetRequestClusteringVariable.CONTENT:
            return content()
        if self is LatestHeadlinesGetRequestClusteringVariable.TITLE:
            return title()
        if self is LatestHeadlinesGetRequestClusteringVariable.SUMMARY:
            return summary()
