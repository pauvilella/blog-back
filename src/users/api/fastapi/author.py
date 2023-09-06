import logging
from typing import List

from application.api.middlewares import handle_jwt
from application.config.app_settings import app_settings
from fastapi import APIRouter, Depends

from users.api.schemas.author import AuthorsGetResponse, PatchAuthorMeRequest, PatchAuthorMeResponse
from users.core.dtos.author import AuthorDTO
from users.core.use_cases.authors.get_authors import GetAuthorsUseCase
from users.core.use_cases.authors.patch_author import PatchAuthorUseCase


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/authors")


@router.get(
    '/',
    tags=['Authors'],
)
def get_authors(data_from_jwt: dict = Depends(handle_jwt)) -> List[AuthorsGetResponse]:
    authors: List[AuthorDTO] = GetAuthorsUseCase().get_authors()
    return [AuthorsGetResponse.parse_obj(author) for author in authors]


@router.patch(
    '/me',
    tags=['Authors'],
)
def patch_author_me(
    author_fields: PatchAuthorMeRequest, data_from_jwt: dict = Depends(handle_jwt)
) -> PatchAuthorMeResponse:
    return PatchAuthorMeResponse.parse_obj(
        PatchAuthorUseCase().patch_author(user_email=data_from_jwt['user_email'], author_fields=author_fields)
    )
