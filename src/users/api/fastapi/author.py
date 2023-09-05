import logging
from typing import List

from application.api.middlewares import handle_jwt
from application.config.app_settings import app_settings
from fastapi import APIRouter, Depends

from users.api.schemas.author import AuthorsGetResponse
from users.core.dtos.author import AuthorDTO
from users.core.use_cases.authors.get_authors import GetAuthorsUseCase


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/authors")


@router.get(
    '/',
    tags=['Authors'],
)
def get_authors(data_from_jwt: dict = Depends(handle_jwt)) -> List[AuthorsGetResponse]:
    authors: List[AuthorDTO] = GetAuthorsUseCase().get_authors()
    return [AuthorsGetResponse.parse_obj(author) for author in authors]
