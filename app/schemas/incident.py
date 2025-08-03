from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime


class IncidentStatus(str, Enum):
    open = "Open"
    in_progress = "In Progress"
    resolved = "Resolved"
    closed = "Closed"


class IncidentCreate(BaseModel):

    title: str
    description: Optional[str] = None
    severity: Optional[str] = "Low"


class ResponseIncident(BaseModel):
    id : int
    title : str
    description : Optional[str]
    status : IncidentStatus
    severity : str
    created_at: datetime
    reported_by_id : int

    model_config = ConfigDict(from_attributes=True)

class UpdateIncidentStatus(BaseModel):
    status: IncidentStatus