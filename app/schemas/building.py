from pydantic import BaseModel
from typing import Tuple

class BuildingBase(BaseModel):
    address: str

class BuildingCreate(BuildingBase):
    latitude: float
    longitude: float

class Building(BuildingBase):
    id: int
    coordinates: Tuple[float, float]

    class Config:
        from_attributes = True