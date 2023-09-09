from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import IntEnum


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None


class VoteValue(IntEnum):
    positive_vote: 1
    negative_vote: -1


class Vote(BaseModel):
    post_id: int
    user_id: int
    vote_value: VoteValue = VoteValue(1)
    created_at: datetime
