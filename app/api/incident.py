from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.db.deps import db_dependency, get_current_user
from app.models.users import User
from app.schemas.incident import IncidentCreate, ResponseIncident
from app.crud.incidents import (
    create_incident, 
    get_all_incidents,
    get_incident
)


router = APIRouter()

@router.post("/", response_model=ResponseIncident)
def create_new_incident(incident:IncidentCreate, db:db_dependency, current_user: User = Depends(get_current_user)):
    print(f"Current user:{current_user.email}")
    return create_incident(incident, current_user.id, db)

@router.get("/", response_model=List[ResponseIncident])
def list_all_incidents(db:db_dependency, current_user: User = Depends(get_current_user)):
    return get_all_incidents(db)

@router.get("/{incident_id}", response_model=List[ResponseIncident])
def get_incident_by_id(incident_id: int, db:db_dependency, current_user: User = Depends(get_current_user)):
    return get_incident(incident_id, db)