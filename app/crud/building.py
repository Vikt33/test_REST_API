from sqlalchemy import func
from geoalchemy2 import WKTElement
from geoalchemy2.functions import ST_DWithin, ST_MakePoint, ST_MakeEnvelope
from app.models import Building

def get_buildings_in_radius(db: Session, lat: float, lon: float, radius: float):
    point = ST_MakePoint(lon, lat)
    return db.query(Building).filter(ST_DWithin(Building.coordinates, point, radius)).all()

def get_buildings_in_rectangle(db: Session, min_lat: float, min_lon: float, max_lat: float, max_lon: float):
    envelope = f'POLYGON(({min_lon} {min_lat}, {min_lon} {max_lat}, {max_lon} {max_lat}, {max_lon} {min_lat}, {min_lon} {min_lat}))'
    return db.query(Building).filter(Building.coordinates.intersects(envelope)).all()