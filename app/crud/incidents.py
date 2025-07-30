from app.db.deps import db_dependency
from app.models.incidents import Incident
from app.schemas.incident import IncidentCreate


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
    return db.query(Incident).filter(Incident.id==incident_id)

def get_all_incidents(db:db_dependency):
    return db.query(Incident).all()
