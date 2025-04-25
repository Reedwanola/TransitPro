from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
import uuid

class Bus(Base):
    __tablename__ = "buses"

    id = Column(String, primary_key=True, index=True)
    capacity = Column(Integer, nullable=False)
    plate_number = Column(String, unique=True, nullable=False)
    route_id = Column(String, ForeignKey("routes.id"), nullable=False)


