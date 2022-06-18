from typing import List, Union
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    time_created: datetime
    is_active: bool

    class Config:
        orm_mode = True
