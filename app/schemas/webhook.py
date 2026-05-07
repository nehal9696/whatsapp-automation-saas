from pydantic import BaseModel

class WebhookUpdate(BaseModel):
    message_id: int
    status: str