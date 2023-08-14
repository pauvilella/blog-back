import logging

from application.config.app_settings import app_settings
from infra.databases.postgres import Base, get_db
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import backref, relationship
from users.adapters.user_postgres_repository import User
from users.core.dtos.author import AuthorDTO
from users.core.ports.author import AuthorPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class Author(Base):
    """Models an author table"""

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", backref=backref('author', uselist=False, cascade='all, delete-orphan'))
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
            user=self.user.to_dto(),
            abstract=self.abstract,
            job_title=self.job_title,
            linkedin_profile_link=self.linkedin_profile_link,
            github_profile_link=self.github_profile_link,
        )

    def update_from_dto(self, author: AuthorDTO):
        if author.id:
            self.id = author.id
        if author.user:
            self.user = author.user
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
            user=User.from_dto(author.user),
            abstract=author.abstract,
            job_title=author.job_title,
            linkedin_profile_link=author.linkedin_profile_link,
            github_profile_link=author.github_profile_link,
        )


class AuthorsPostgresRepository(AuthorPort):
    def __init__(self):
        ...

    def create_author(self, author: AuthorDTO) -> AuthorDTO:
        try:
            logger.info("Creating author in PostgreSQL")
            db_author = Author.from_dto(author)
            with get_db() as session:
                user_from_db: User = session.query(User).filter(User.id == author.user.id).one()
                db_author.user = user_from_db
                session.add(db_author)
                session.commit()
                session.refresh(db_author)
                logger.debug(db_author)
                logger.info("Author created successfully!")
                return db_author.to_dto()
        except Exception:
            logger.exception("Error creating author in PostgreSQL")
