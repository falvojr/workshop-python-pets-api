from pydantic import Field

from app.api.v1.request import BaseRequest
from app.model import UserModel


class UserRequest(BaseRequest):
    name: str = Field(...)

    class Meta:
        model = UserModel
