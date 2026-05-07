from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.message import Message
from app.core.logger import logger
from app.core.rate_limiter import limiter
from fastapi import Request

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def process_message(message_id: int):
    db = SessionLocal()

    message = db.query(Message).filter(Message.id == message_id).first()

    if message:
        message.status = "sent"
        db.commit()

    db.close()

@router.post("/send-message")
@limiter.limit("5/minute")
def send_message(
    request: Request,
    content: str,
    phone: str,
    business_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    message = Message(
        content=content,
        phone=phone,
        business_id=business_id,
        status="pending"
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    # async processing
    background_tasks.add_task(process_message, message.id)
    
    logger.info(f"Processing message {message.id}")

    return {"message": "Message queued", "data": message}