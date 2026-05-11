from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.core.dependencies import get_current_user

from app.models.business import Business
from app.models.user import User

from app.schemas.business import (
    BusinessCreate,
    BusinessResponse
)

router = APIRouter(prefix="/api")

@router.get("/businesses")
def get_businesses(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    businesses = db.query(Business).filter(
        Business.owner_id == current_user.id
    ).all()

    return businesses

@router.post(
    "/business",
    response_model=BusinessResponse
)
def create_business(
    business_data: BusinessCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    print("CURRENT USER:", current_user)

    business = Business(
        name=business_data.name,
        owner_id=current_user.id
    )

    db.add(business)
    db.commit()
    db.refresh(business)

    return business