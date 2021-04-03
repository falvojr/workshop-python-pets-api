from pydantic import BaseModel


class BaseRequest(BaseModel):
    class Config:
        orm_mode = True

    @property
    def model(self):
        return self.Meta.model(**self.dict(exclude_unset=True))
