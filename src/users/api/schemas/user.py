from pydantic import BaseModel, EmailStr
from users.core.dtos.user import Role


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: Role


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class UserSignupRequest(UserBase):
    password: str


class UserSignupResponse(UserBase):
    is_active: bool


class UserTokenRefreshRequest(BaseModel):
    refresh_token: str


class UserMeResponse(UserBase):
    id: int
    is_active: bool
