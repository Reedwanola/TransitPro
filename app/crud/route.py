from sqlalchemy.orm import Session
from app.models.route import Route
from app.schemas.route import RouteCreate


def create_route(db: Session, route_data: RouteCreate) -> Route:
    route = Route(**route_data.dict())
    db.add(route)
    db.commit()
    db.refresh(route)
    return route


def get_routes(db: Session):
    return db.query(Route).all()
