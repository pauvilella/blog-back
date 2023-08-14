from typing import Optional

from pydantic import BaseModel
from users.core.dtos.user import UserDTO


class AuthorDTO(BaseModel):
    id: Optional[int]
    user: Optional[UserDTO]
    abstract: Optional[str]
    job_title: Optional[str]
    linkedin_profile_link: Optional[str]
    github_profile_link: Optional[int]

    def __repr__(self):
        return f"""AuthorDTO (id={self.id}, job_title={self.email},
                user_id={self.user.id}"""
