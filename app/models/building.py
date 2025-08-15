from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    coordinates = Column(Geometry(geometry_type='POINT', srid=4326))
    organizations = relationship("Organization", back_populates="building")