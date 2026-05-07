from pydantic import BaseModel

class BusinessCreate(BaseModel):
    name: str

class BusinessResponse(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True