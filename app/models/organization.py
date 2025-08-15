from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.database import Base

organization_activity = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    building = relationship("Building", back_populates="organizations")
    activities = relationship("Activity", secondary=organization_activity)
    phones = relationship("Phone", back_populates="organization")

class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="phones")