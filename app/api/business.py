from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.business import Business
from app.models.user import User

from app.schemas.business import (
    BusinessCreate,
    BusinessResponse
)

from app.core.dependencies import get_current_user
from app.core.logger import logger

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/business",
    response_model=BusinessResponse
)
def create_business(
    business_data: BusinessCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    logger.info(
        f"Creating business for user {current_user.id}"
    )

    business = Business(
        name=business_data.name,
        owner_id=current_user.id
    )

    db.add(business)
    db.commit()
    db.refresh(business)

    return business