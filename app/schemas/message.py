from pydantic import BaseModel

class MessageCreate(BaseModel):
    content: str
    phone: str
    business_id: int

class MessageResponse(BaseModel):
    id: int
    content: str
    phone: str
    status: str
    business_id: int

    class Config:
        from_attributes = True