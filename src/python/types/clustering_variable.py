# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClusteringVariable(str, enum.Enum):
    """
    Specifies which part of the article to use for determining similarity when clustering.

    Possible values are:
    - `content`: Uses the full article content (default).
    - `title`: Uses only the article title.
    - `summary`: Uses the article summary.

    To learn more, see [Clustering news articles](/docs/v3/documentation/guides-and-concepts/clustering-news-articles).
    """

    CONTENT = "content"
    TITLE = "title"
    SUMMARY = "summary"

    def visit(
        self,
        content: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        summary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClusteringVariable.CONTENT:
            return content()
        if self is ClusteringVariable.TITLE:
            return title()
        if self is ClusteringVariable.SUMMARY:
            return summary()