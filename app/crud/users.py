
from app.db.deps import db_dependency
from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate
from passlib.hash import bcrypt


def create_user(user:UserCreate, db:db_dependency):
    hashed_pw = bcrypt.hash(user.password)
    new_user = User(
        email = user.email,
        name = user.name,
        hashed_password = hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(email:str, db:db_dependency):
    return db.query(User).filter(User.email==email).first()
