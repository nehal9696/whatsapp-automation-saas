from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.business import Business
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/business")
def create_business(
    name: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    business = Business(
        name=name,
        owner_id=current_user.id
    )

    db.add(business)
    db.commit()
    db.refresh(business)

    return business