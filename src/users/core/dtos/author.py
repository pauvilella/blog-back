from typing import Optional

from pydantic import BaseModel


class AuthorDTO(BaseModel):
    id: Optional[int]
    abstract: Optional[str]
    job_title: Optional[str]
    linkedin_profile_link: Optional[str]
    github_profile_link: Optional[int]
