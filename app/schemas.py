from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class PostBase(BaseModel):
    __abstract__ = True

    title: str
    content: str
    published: bool = True


class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: Userout

    class Config:
        orm_mode = True


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # lessthen equal


class PostOut(BaseModel):
    Post: PostResponse
    votes : int
    
