import logging

from application.config.app_settings import app_settings
from users.adapters.author_postgres_repository import AuthorsPostgresRepository
from users.adapters.user_postgres_repository import UsersPostgresRepository
from users.api.schemas.author import PatchAuthorMeRequest
from users.core.dtos.author import AuthorDTO


logger = logging.getLogger(app_settings.APP_LOGGER)


class PatchAuthorUseCase:
    def __init__(self):
        self.author_port = AuthorsPostgresRepository()
        self.user_port = UsersPostgresRepository()

    def patch_author(self, user_email: str, author_fields: PatchAuthorMeRequest) -> AuthorDTO:
        logger.info(f"Patching author with email {user_email}")
        author: AuthorDTO = self.author_port.get_author_by_user_email(user_email)
        if author is None:
            raise Exception(f"Author with email {user_email} not found.")
        new_author = AuthorDTO(id=author.id, **author_fields.dict())
        return self.author_port.patch_author(new_author)
