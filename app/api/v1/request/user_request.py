from typing import Optional
from pydantic import Field

from app.api.v1.request import BaseRequest
from app.model import UserModel


class UserRequest(BaseRequest):
    username: str = Field(...)
    firstName: Optional[str] = Field(...)
    lastName: Optional[str] = Field(...)
    email: Optional[str] = Field(...)
    password: Optional[str] = Field(...)
    phone: Optional[str] = Field(...)
    userStatus: Optional[int] = Field(...)

    class Meta:
        model = UserModel
