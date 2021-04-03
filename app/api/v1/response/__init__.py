from pydantic import BaseModel


class BaseResponse(BaseModel):
    class Config:
        orm_mode = True
