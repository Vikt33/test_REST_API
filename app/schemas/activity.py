from pydantic import BaseModel
from typing import List, Optional

class ActivityBase(BaseModel):
    name: str

class ActivityCreate(ActivityBase):
    parent_id: Optional[int] = None

class Activity(ActivityBase):
    id: int
    parent_id: Optional[int] = None
    children: List["Activity"] = []

    class Config:
        from_attributes = True

Activity.model_rebuild()