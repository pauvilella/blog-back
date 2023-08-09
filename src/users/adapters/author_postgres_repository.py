import logging

from application.config.app_settings import app_settings
from infra.databases.postgres import Base
from sqlalchemy import Column, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from users.core.dtos.author import AuthorDTO
from users.core.ports.author import AuthorPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class Author(Base):
    """Models an author table"""

    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    user: Mapped["User"] = relationship(back_populates="author")
    abstract = Column(Text, nullable=True, unique=False)
    job_title = Column(String(225), nullable=True)
    linkedin_profile_link = Column(String(225), nullable=True)
    github_profile_link = Column(String(225), nullable=True)

    PrimaryKeyConstraint("id", name="pk_author_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<Author {id!r}>".format(id=self.id)

    def to_dto(self) -> AuthorDTO:
        return AuthorDTO(
            id=self.id,
            abstract=self.abstract,
            job_title=self.job_title,
            linkedin_profile_link=self.linkedin_profile_link,
            github_profile_link=self.github_profile_link,
        )

    def update_from_dto(self, author: AuthorDTO):
        if author.id:
            self.id = author.id
        if author.abstract:
            self.abstract = author.abstract
        if author.job_title:
            self.job_title = author.job_title
        if author.linkedin_profile_link:
            self.linkedin_profile_link = author.linkedin_profile_link
        if author.github_profile_link:
            self.github_profile_link = author.github_profile_link

    @staticmethod
    def from_dto(author: AuthorDTO):
        return Author(
            id=author.id,
            abstract=author.abstract,
            job_title=author.job_title,
            linkedin_profile_link=author.linkedin_profile_link,
            github_profile_link=author.github_profile_link,
        )


class AuthorsPostgresRepository(AuthorPort):
    def __init__(self):
        ...
