from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name : str
    password: str


class ResponseUser(BaseModel):

    id: int
    name: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True