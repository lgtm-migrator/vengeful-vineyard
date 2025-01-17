"""
Models for group member data structures. Group members only contain fields
from the table 'group_members'.
"""

from app.types import GroupId, OWGroupUserId, UserId
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class BaseGroupMember(BaseModel):
    group_id: GroupId
    user_id: UserId
    ow_group_user_id: OWGroupUserId | None = None
    active: bool = True


class GroupMember(BaseGroupMember):
    pass


class GroupMemberCreate(BaseGroupMember):
    pass


class GroupMemberUpdate(BaseGroupMember):
    pass
