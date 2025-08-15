# app/schemas/organizations.py
from pydantic import BaseModel
from typing import List
from .activity import Activity
from .building import Building

class PhoneBase(BaseModel):
    number: str

class OrganizationBase(BaseModel):
    name: str
    building_id: int

class OrganizationCreate(OrganizationBase):
    activities: List[int] = []
    phones: List[str] = []

class Organization(OrganizationBase):
    id: int
    activities: List[Activity] = []
    phones: List[PhoneBase] = []
    building: Building

    class Config:
        from_attributes = True