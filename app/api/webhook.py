from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.message import Message

router = APIRouter(prefix="/webhook")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/message-status")
def update_message_status(
    message_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    message = db.query(Message).filter(
        Message.id == message_id
    ).first()

    if not message:
        return {"error": "Message not found"}

    message.status = status

    db.commit()

    return {
        "message": "Status updated",
        "status": status
    }