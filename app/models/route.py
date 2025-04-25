from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Route(Base):
    __tablename__ = "routes"

    id = Column(primary_key=True, index=True,  default=lambda: str(uuid.uuid4()))
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    
