from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.message import Message
from app.db.dependencies import get_db

from app.schemas.webhook import WebhookUpdate

router = APIRouter(prefix="/webhook")

@router.post("/message-status")
def update_message_status(
    webhook_data: WebhookUpdate,
    db: Session = Depends(get_db)
):

    message = db.query(Message).filter(
        Message.id == webhook_data.message_id
    ).first()

    if not message:
        return {"error": "Message not found"}

    message.status = webhook_data.status

    db.commit()

    return {
        "message": "Status updated",
        "status": webhook_data.status
    }