# This file was auto-generated by Fern from our API Definition.

import typing

from ....types.dto_responses_more_like_this_response_failed_search_response import (
    DtoResponsesMoreLikeThisResponseFailedSearchResponse,
)
from ....types.dto_responses_more_like_this_response_search_response import (
    DtoResponsesMoreLikeThisResponseSearchResponse,
)

SearchSimilarPostResponse = typing.Union[
    DtoResponsesMoreLikeThisResponseSearchResponse, DtoResponsesMoreLikeThisResponseFailedSearchResponse
]