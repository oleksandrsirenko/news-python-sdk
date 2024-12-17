# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .dto_responses_more_like_this_response_article_result import DtoResponsesMoreLikeThisResponseArticleResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DtoResponsesMoreLikeThisResponseFailedSearchResponse(pydantic.BaseModel):
    """
    The response model for a failed `Search similar` request.
    """

    status: typing.Optional[str] = pydantic.Field(description="The status of the response.")
    total_hits: typing.Optional[int] = pydantic.Field(
        description="The total number of articles matching the search criteria."
    )
    page: typing.Optional[int] = pydantic.Field(description="The current page number of the results.")
    total_pages: typing.Optional[int] = pydantic.Field(
        description="The total number of pages available for the given search criteria."
    )
    page_size: typing.Optional[int] = pydantic.Field(description="The number of articles per page.")
    articles: typing.Optional[typing.List[DtoResponsesMoreLikeThisResponseArticleResult]] = pydantic.Field(
        description="A list of articles matching the search criteria."
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
