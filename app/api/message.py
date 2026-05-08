from fastapi import APIRouter, Depends, BackgroundTasks, Request
from sqlalchemy.orm import Session

from app.models.message import Message
from app.db.dependencies import get_db
from app.models.user import User

from app.schemas.message import (
    MessageCreate,
    MessageResponse
)

from app.core.dependencies import get_current_user
from app.core.rate_limiter import limiter
from app.core.logger import logger

router = APIRouter(prefix="/api")

def process_message(message_id: int):
    logger.info(f"Processing message {message_id}")

@router.post(
    "/send-message",
    response_model=MessageResponse
)
@limiter.limit("5/minute")
def send_message(
    request: Request,
    message_data: MessageCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    message = Message(
        content=message_data.content,
        phone=message_data.phone,
        business_id=message_data.business_id,
        status="pending"
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    background_tasks.add_task(
        process_message,
        message.id
    )

    logger.info(
        f"Message queued by user {current_user.id}"
    )

    return message