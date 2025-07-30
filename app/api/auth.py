from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.users import User
from app.db.deps import db_dependency
from app.schemas.token import Token
from app.core.security import create_access_token, verify_password


router = APIRouter()

@router.post("/login", response_model=Token)
def login(db:db_dependency, form_data:OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

