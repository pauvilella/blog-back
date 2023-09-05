from typing import Optional

from pydantic import BaseModel
from users.api.schemas.user import UserBase


class AuthorBase(BaseModel):
    user: UserBase
    abstract: Optional[str]
    abstract: Optional[str]
    job_title: Optional[str]
    linkedin_profile_link: Optional[str]
    github_profile_link: Optional[str]


class AuthorsGetResponse(AuthorBase):
    ...
