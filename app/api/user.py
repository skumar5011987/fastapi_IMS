from fastapi import APIRouter, HTTPException
from app.schemas.users import UserCreate, ResponseUser
from app.db.deps import db_dependency
from app.crud.users import create_user, get_user_by_email

router = APIRouter()

@router.post("/register", response_model=ResponseUser)
def create_new_user(user:UserCreate, db:db_dependency):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(user, db)
