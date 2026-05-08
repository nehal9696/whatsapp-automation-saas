from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.db.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    status = Column(String, default="pending")
    business_id = Column(Integer, ForeignKey("businesses.id"))
    created_at = Column(DateTime, default=datetime.utcnow)