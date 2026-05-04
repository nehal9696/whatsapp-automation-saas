from app.db.database import Base, engine

# import models so they register
from app.models.user import User
from app.models.business import Business
from app.models.message import Message

def init_db():
    Base.metadata.create_all(bind=engine)