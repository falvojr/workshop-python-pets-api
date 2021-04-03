from typing import Optional
from pydantic import Field

from app.api.v1.response import BaseResponse


class UserResponse(BaseResponse):
    id_: int = Field(None, alias="id")
    username: str = Field(None)
    firstName: Optional[str] = Field(None)
    lastName: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    userStatus: Optional[int] = Field(None)
