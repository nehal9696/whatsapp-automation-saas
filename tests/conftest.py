import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

from app.main import app
from app.db.database import Base
from app.db.dependencies import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create tables once
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# SINGLE SHARED SESSION
db = TestingSessionLocal()

def override_get_db():
    try:
        yield db
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)