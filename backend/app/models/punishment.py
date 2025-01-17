"""
Models for punishment data structures
"""

from datetime import datetime

from app.types import GroupId, PunishmentId, PunishmentTypeId, UserId
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class PunishmentBase(BaseModel):
    punishment_type_id: PunishmentTypeId
    reason: str
    amount: int


class PunishmentCreate(PunishmentBase):
    pass


class PunishmentOut(PunishmentCreate):
    punishment_id: PunishmentId
    created_time: datetime
    created_by: UserId
    verified_time: datetime | None
    verified_by: UserId | None


class PunishmentRead(PunishmentOut):
    group_id: GroupId
    user_id: UserId
