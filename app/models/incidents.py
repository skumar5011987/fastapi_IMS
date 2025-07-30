from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.session import Base
from .users import User


class IncidentStatus(str, enum.Enum):
    open = "Open"
    in_progress = "In Progress"
    resolved = "Resolved"
    closed = "Closed"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.open)
    severity = Column(String, default="Low")
    created_at = Column(DateTime, default=datetime.utcnow)

    reported_by_id = Column(Integer, ForeignKey("users.id"))
    reported_by = relationship("User", backref='incidents')