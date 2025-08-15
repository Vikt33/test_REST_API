from sqlalchemy.orm import Session
from app.models import Organization, Phone

def get_organizations_by_building(db: Session, building_id: int):
    return db.query(Organization).filter(Organization.building_id == building_id).all()

def get_organizations_by_activity(db: Session, activity_id: int):
    return db.query(Organization).join(Organization.activities).filter_by(id=activity_id).all()

def get_organization(db: Session, organization_id: int):
    return db.query(Organization).filter(Organization.id == organization_id).first()

def search_organizations_by_name(db: Session, name: str):
    return db.query(Organization).filter(Organization.name.ilike(f"%{name}%")).all()