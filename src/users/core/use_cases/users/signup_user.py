import logging

from application.config.app_settings import app_settings
from users.adapters.author_postgres_repository import AuthorsPostgresRepository
from users.adapters.user_postgres_repository import UsersPostgresRepository
from users.core.dtos.author import AuthorDTO
from users.core.dtos.user import UserDTO


logger = logging.getLogger(app_settings.APP_LOGGER)


class SignupUserUseCase:
    def __init__(self):
        self.user_port = UsersPostgresRepository()
        self.author_port = AuthorsPostgresRepository()

    def signup_user(self, user_dto: UserDTO, is_author: bool) -> UserDTO:
        created_user = self.user_port.create_user(user_dto)
        if is_author:
            logger.info(f"New signed up user: {created_user.email} wants to be an author!")
            self.author_port.create_author(AuthorDTO(user=created_user))
        return created_user
