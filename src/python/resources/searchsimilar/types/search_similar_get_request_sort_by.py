# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SearchSimilarGetRequestSortBy(str, enum.Enum):
    RELEVANCY = "relevancy"
    DATE = "date"
    RANK = "rank"

    def visit(
        self,
        relevancy: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        rank: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchSimilarGetRequestSortBy.RELEVANCY:
            return relevancy()
        if self is SearchSimilarGetRequestSortBy.DATE:
            return date()
        if self is SearchSimilarGetRequestSortBy.RANK:
            return rank()