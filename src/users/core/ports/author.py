from abc import ABC, abstractclassmethod

from users.core.dtos.author import AuthorDTO


class AuthorPort(ABC):
    @abstractclassmethod
    def create_author(self, author: AuthorDTO) -> AuthorDTO:
        ...
