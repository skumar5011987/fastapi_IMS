from fastapi import Depends
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

async def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Error in dependency: {e}")
        raise  # must re-raise!
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]