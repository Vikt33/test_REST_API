from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/organizations", tags=["organizations"])

@router.get("/{organization_id}", response_model=schemas.Organization)
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    organization = crud.get_organization(db, organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization

@router.get("/search/name/", response_model=list[schemas.Organization])
def search_organizations_by_name(name: str, db: Session = Depends(get_db)):
    return crud.search_organizations_by_name(db, name)

@router.get("/building/{building_id}", response_model=list[schemas.Organization])
def get_orgs_by_building(building_id: int, db: Session = Depends(get_db)):
    return crud.get_organizations_by_building(db, building_id)

@router.get("/activity/{activity_id}", response_model=list[schemas.Organization])
def get_orgs_by_activity(activity_id: int, db: Session = Depends(get_db)):
    return crud.get_organizations_by_activity(db, activity_id)

@router.get("/nearby/radius", response_model=list[schemas.Organization])
def get_orgs_in_radius(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    radius: float = Query(..., description="Radius in meters"),
    db: Session = Depends(get_db)
):
    return crud.get_organizations_in_radius(db, lat, lon, radius)