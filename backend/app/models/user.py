"""
Models for user data structures
"""

from app.types import OWUserId, UserId
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class UserBase(BaseModel):
    ow_user_id: OWUserId
    first_name: str
    last_name: str
    email: str | None


class CreatedUserBase(UserBase):
    user_id: UserId


class User(CreatedUserBase):
    pass


class UserCreate(UserBase):
    pass


class UserUpdate(CreatedUserBase):
    pass
