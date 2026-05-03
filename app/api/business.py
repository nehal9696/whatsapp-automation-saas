print("Business router file loaded")
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.business import Business

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/business")
def create_business(name: str, db: Session = Depends(get_db)):
    business = Business(name=name, owner_id=1)  # later replace with logged-in user
    db.add(business)
    db.commit()
    db.refresh(business)
    return business