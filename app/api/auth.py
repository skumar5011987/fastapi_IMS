from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.models.users import User
from app.db.deps import db_dependency, oauth2_scheme
from app.schemas.token import AccessToken, RefreshToken
from app.core.security import create_access_token, create_refresh_token, verify_password
from app.core.blacklist import blacklist_token
from app.core.security import SECRET_KEY, ALGORITHM


router = APIRouter()

@router.post("/refresh", response_model=AccessToken)
def refresh_token(payload: RefreshToken):
    try:
        decoded = jwt.decode(payload.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if decoded.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({"sub": decoded.get("sub")})
    new_refresh_token = create_refresh_token({"sub": decoded.get("sub")})

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }

@router.post("/login", response_model=AccessToken)
def login(db:db_dependency, form_data:OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access = create_access_token(data={"sub": user.email})
    refresh = create_refresh_token(data = {"sub": user.email})
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }

@router.post("/logout")
def logout(request: Request, token: str = Depends(oauth2_scheme)):
    blacklist_token(token)
    return {"detail": "Successfully logged out"}