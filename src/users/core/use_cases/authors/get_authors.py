import logging
from typing import List

from application.config.app_settings import app_settings
from users.adapters.author_postgres_repository import AuthorsPostgresRepository
from users.core.dtos.author import AuthorDTO


logger = logging.getLogger(app_settings.APP_LOGGER)


class GetAuthorsUseCase:
    def __init__(self):
        self.author_port = AuthorsPostgresRepository()

    def get_authors(self) -> List[AuthorDTO]:
        return self.author_port.get_authors()
