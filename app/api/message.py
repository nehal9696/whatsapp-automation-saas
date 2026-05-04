from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.message import Message

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send-message")
def send_message(content: str, phone: str, business_id: int, db: Session = Depends(get_db)):
    message = Message(
        content=content,
        phone=phone,
        business_id=business_id,
        status="pending"
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    return {"message": "Message queued", "data": message}