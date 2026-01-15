from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from ..database import Base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from ..main import app
from ..models import Todos, Users
import pytest
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread" : False},
    poolclass = StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username": "testuser1", "id": 1, 'user_role': 'admin'}


client = TestClient(app)

@pytest.fixture
def test_todo():
    todo=Todos(
        title='Learn to code',
        description='Learn FastAPI framework',
        priority=5,
        complete=False,
        owner_id=1
    )
    db=TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user=Users(
        username='testuser1',
        email='testuser1@example.com',
        first_name='Test',
        last_name='User',
        role='admin',
        hashed_password=bcrypt_context.hash('password123'),
        is_active=True,
        phone_number='1234567890'
    )
    db=TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()



