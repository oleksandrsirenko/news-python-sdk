# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .authors import Authors
from .dto_responses_more_like_this_response_article_result_all_domain_links import (
    DtoResponsesMoreLikeThisResponseArticleResultAllDomainLinks,
)
from .dto_responses_more_like_this_response_article_result_all_links import (
    DtoResponsesMoreLikeThisResponseArticleResultAllLinks,
)
from .journalists import Journalists
from .similar_document import SimilarDocument

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DtoResponsesMoreLikeThisResponseArticleResult(pydantic.BaseModel):
    """
    The data model for an article result in the `Search similar` articles
    request.

    Response field behavior:
    - Required fields are guaranteed to be present and non-null.
    - Optional fields may be `null`/`undefined` if the data couldn't be extracted
    during processing.
    """

    title: str = pydantic.Field(description="The title of the article.")
    author: typing.Optional[str] = pydantic.Field(description="The author of the article.")
    authors: typing.Optional[Authors] = pydantic.Field(description="The list of authors of the article.")
    journalists: typing.Optional[Journalists] = pydantic.Field(description="The list of journalists of the article.")
    published_date: typing.Optional[str] = pydantic.Field(description="The date when the article was published.")
    published_date_precision: typing.Optional[str] = pydantic.Field(description="The precision of the published date.")
    updated_date: typing.Optional[str] = pydantic.Field(description="The date when the article was last updated.")
    updated_date_precision: typing.Optional[str] = pydantic.Field(description="The precision of the updated date.")
    parse_date: typing.Optional[str] = pydantic.Field(description="The date when the article was parsed.")
    link: str = pydantic.Field(description="The link to the article.")
    domain_url: str = pydantic.Field(description="The domain URL of the article.")
    full_domain_url: str = pydantic.Field(description="The full domain URL of the article.")
    name_source: typing.Optional[str] = pydantic.Field(description="The source name of the article.")
    is_headline: typing.Optional[bool] = pydantic.Field(description="Indicates if the article is a headline.")
    paid_content: typing.Optional[bool] = pydantic.Field(description="Indicates if the article is paid content.")
    extraction_data: typing.Optional[str] = pydantic.Field(description="The data extracted from the article.")
    country: typing.Optional[str] = pydantic.Field(description="The country of the article.")
    rights: typing.Optional[str] = pydantic.Field(description="The rights associated with the article.")
    rank: int = pydantic.Field(description="The rank of the article.")
    media: typing.Optional[str] = pydantic.Field(description="The media associated with the article.")
    language: typing.Optional[str] = pydantic.Field(description="The language of the article.")
    description: typing.Optional[str] = pydantic.Field(description="The description of the article.")
    content: str = pydantic.Field(description="The content of the article.")
    word_count: typing.Optional[int] = pydantic.Field(description="The word count of the article.")
    is_opinion: typing.Optional[bool] = pydantic.Field(description="Indicates if the article is an opinion piece.")
    twitter_account: typing.Optional[str] = pydantic.Field(
        description="The Twitter account associated with the article."
    )
    all_links: typing.Optional[DtoResponsesMoreLikeThisResponseArticleResultAllLinks] = pydantic.Field(
        description="All the links mentioned in the article."
    )
    all_domain_links: typing.Optional[DtoResponsesMoreLikeThisResponseArticleResultAllDomainLinks] = pydantic.Field(
        description="All the domain links mentioned in the article."
    )
    nlp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="The natural language processing data associated with the article."
    )
    id: str = pydantic.Field(description="The unique identifier of the article.")
    score: float = pydantic.Field(description="The relevance score of the article.")
    similar_documents: typing.Optional[typing.List[SimilarDocument]] = pydantic.Field(
        description="A list of similar documents to the article."
    )

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
