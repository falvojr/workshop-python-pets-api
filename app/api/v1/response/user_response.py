from pydantic import Field

from app.api.v1.response import BaseResponse


class UserResponse(BaseResponse):
    id_: int = Field(None, alias="id")
    name: str = Field(None)
