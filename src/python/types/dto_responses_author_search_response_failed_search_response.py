# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .dto_responses_author_search_response_article_result import DtoResponsesAuthorSearchResponseArticleResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DtoResponsesAuthorSearchResponseFailedSearchResponse(pydantic.BaseModel):
    """
    The response model for a failed `Authors` search request.
    """

    status: typing.Optional[str] = pydantic.Field(
        description="The status of the response, indicating no matches were found."
    )
    total_hits: typing.Optional[int] = pydantic.Field(
        description="The total number of articles matching the search criteria, always zero in this case."
    )
    page: typing.Optional[int] = pydantic.Field(
        description="The current page number of the results, always zero in this case."
    )
    total_pages: typing.Optional[int] = pydantic.Field(
        description="The total number of pages available for the given search criteria, always zero in this case."
    )
    page_size: typing.Optional[int] = pydantic.Field(
        description="The number of articles per page, always zero in this case."
    )
    articles: typing.Optional[typing.List[DtoResponsesAuthorSearchResponseArticleResult]] = pydantic.Field(
        description="An empty list of articles, as no matches were found."
    )
    user_input: typing.Dict[str, typing.Any] = pydantic.Field(description="The user input parameters for the search.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}