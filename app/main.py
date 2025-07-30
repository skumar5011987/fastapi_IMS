from fastapi import FastAPI
from app.db.session import Base, engine
from app.api import incident, user, auth


app = FastAPI()

# Initialize tables on first run (for now; later use Alembic)
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["Register"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(incident.router, prefix="/incidents", tags=["Incidents"])



