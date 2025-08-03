from fastapi import HTTPException, Depends
from app.db.deps import db_dependency
from app.models.incidents import Incident
from app.models.users import User
from app.schemas.incident import IncidentCreate, UpdateIncidentStatus


def create_incident(incident: IncidentCreate, reporter_id: int, db:db_dependency):
    new_incident = Incident(
        title  = incident.title,
        description = incident.description,
        severity = incident.severity,
        reported_by_id = reporter_id
    )

    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)

    return new_incident

def get_incident(incident_id: int, db:db_dependency):
    return db.query(Incident).filter(Incident.id==incident_id).first()

def get_all_incidents(db:db_dependency, user_id: int):
    return db.query(Incident).filter(Incident.reported_by_id==user_id)

def update_incident(incident_id:int, payload: UpdateIncidentStatus, db:db_dependency):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    incident.status = payload.status
    db.commit()
    db.refresh(incident)
    return incident