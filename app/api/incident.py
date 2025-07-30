from fastapi import APIRouter
from typing import List
from app.db.deps import db_dependency
from app.schemas.incident import IncidentCreate, ResponseIncident
from app.crud.incidents import (
    create_incident, 
    get_all_incidents,
    get_incident
)


router = APIRouter()

@router.post("/", response_model=ResponseIncident)
def create_new_incident(incident:IncidentCreate, db:db_dependency):
    
    reporter_id = incident.reporter_id
    return create_incident(incident, reporter_id, db)

@router.get("/", response_model=List[ResponseIncident])
def list_all_incidents(db:db_dependency):
    return get_all_incidents(db)

@router.get("/{incident_id}", response_model=List[ResponseIncident])
def get_incident_by_id(incident_id: int, db:db_dependency):
    return get_incident(incident_id, db)