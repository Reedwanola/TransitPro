from sqlalchemy.orm import Session
from app.models.bus import Bus
from app.models.route import Route
from app.schemas.bus import BusCreate
from fastapi import HTTPException

def create_bus(db: Session, bus_data: BusCreate) -> Bus:

    if not db.query(Route).filter(Route.id == bus_data.route_id).first():
        raise HTTPException(status_code=404, detail="Route not found")
    bus = Bus(**bus_data.dict())
    db.add(bus)
    db.commit()
    db.refresh(bus)
    return bus

def get_buses(db: Session):
    return db.query(Bus).all()