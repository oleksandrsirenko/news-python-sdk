# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .dto_responses_author_search_response_article_result import DtoResponsesAuthorSearchResponseArticleResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LatestHeadlinesResponse(pydantic.BaseModel):
    """
    The response model for the `Latest headlines` request.

    Response field behavior:
    - Required fields are guaranteed to be present and non-null.
    - Optional fields may be `null`/`undefined` if the data couldn't be extracted
    during processing.
    - To access article properties in the `articles` response array,
    use array index notation. For example, `articles[n].title`, where `n`
    is the zero-based index of the article object (0, 1, 2, etc.).
    - The `nlp` property within the article object `articles[n].nlp`
    is only available with NLP-enabled subscription plans.
    """

    status: str = pydantic.Field(description="The status of the response.")
    total_hits: int = pydantic.Field(description="The total number of articles matching the search criteria.")
    page: int = pydantic.Field(description="The current page number of the results.")
    total_pages: int = pydantic.Field(description="The total number of pages available for the given search criteria.")
    page_size: int = pydantic.Field(description="The number of articles per page.")
    articles: typing.List[DtoResponsesAuthorSearchResponseArticleResult] = pydantic.Field(
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
