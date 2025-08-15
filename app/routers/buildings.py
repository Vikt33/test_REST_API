# app/routers/buildings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.get("/{building_id}", response_model=schemas.Building)
def read_building(building_id: int, db: Session = Depends(get_db)):
    building = crud.get_building(db, building_id)
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building

@router.get("/nearby/radius", response_model=list[schemas.Building])
def get_buildings_in_radius(
    lat: float,
    lon: float,
    radius: float,
    db: Session = Depends(get_db)
):
    return crud.get_buildings_in_radius(db, lat, lon, radius)