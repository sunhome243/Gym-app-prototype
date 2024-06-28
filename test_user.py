import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.user_service.database import Base, get_db
from backend.user_service import main, crud, models
import os

# Override database URL for testing
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine and a SessionLocal class with a temporary database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for overriding the session
@pytest.fixture(scope="function")
def testing_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    # Clean up existing data
    cleanup_existing_data(session)

    yield session

    # Rollback transaction to clear data after test
    session.close()
    transaction.rollback()
    connection.close()

# Function to clean up existing data
def cleanup_existing_data(session):
    # Perform cleanup tasks here based on your application's requirements
    # For example, delete all users before running tests
    session.query(models.User).delete()
    session.commit()

# Define the client fixture
@pytest.fixture(scope="function")
def client(testing_session):
    def override_get_db():
        try:
            yield testing_session
        finally:
            testing_session.close()

    main.app.dependency_overrides[get_db] = override_get_db
    with TestClient(main.app) as c:
        yield c
    main.app.dependency_overrides = {}

# Test CRUD operations
def test_create_user(client: TestClient, testing_session: Session):
    user_data = {
        "email": "test@example.com",
        "password": "password",
        "usertype": "MEM"
    }
    response = client.post("/users/", json=user_data)

    assert response.status_code == 200

    created_user = response.json()

    assert created_user["email"] == user_data["email"]
    assert "user_id" in created_user

    
    #Create Error for purpose
    user_data3 = {
        "email": "test@example.com",
        "password": "password",
        "usertype": "TRN"
    }
    response3 = client.post("/users/", json=user_data3)
    assert response3.status_code == 400
    
    user_data4 = {
        "email": "test2@example.com",
        "password": "password",
        "usertype": "TRM"
    }
    response4 = client.post("/users/", json=user_data4)
    assert response4.status_code == 422
    
    
def test_get_user(client: TestClient, testing_session: Session):
    # Create user first
    user_data = {
        "email": "test@example.com",
        "password": "password",
        "height": 190.1,
        "usertype": "MEM"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    created_user = response.json()

    # Test get_user
    user = crud.get_user(testing_session, user_id=created_user["user_id"])
    assert user
    assert user.email == user_data["email"]

def test_get_users(client: TestClient, testing_session: Session):
    # Create users
    user_data1 = {
        "email": "test1@example.com",
        "password": "password1",
        "usertype": "MEM"
    }
    user_data2 = {
        "email": "test2@example.com",
        "password": "password2",
        "usertype": "TRN"
    }
    client.post("/users/", json=user_data1)
    client.post("/users/", json=user_data2)

    # Test get_users
    users = crud.get_users(testing_session, skip=0, limit=10)
    assert len(users) == 2
    assert users[0].email in {user_data1["email"], user_data2["email"]}
    assert users[1].email in {user_data1["email"], user_data2["email"]}
    
def test_update_user(client: TestClient, testing_session: Session):
    # Create a user to update (initial creation)
    user_data = {
        "email": "test@example.com",
        "password": "password",
        "usertype": "MEM",
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    created_user = response.json()
    
    # Define update data
    user_update_data = {
        "email": "test@example.com",
        "password": "newpassword",
        "age": 25,
        "height": 170.0,
        "weight": 65.0,
        "exercise_level": 7,
    }
    
    # Perform update operation
    update_response = client.put(f"/users/{created_user['user_id']}", json=user_update_data)
    assert update_response.status_code == 200
    
    # Check updated user in database
    updated_user_id = created_user['user_id']
    db_user = testing_session.query(models.User).filter(models.User.user_id == updated_user_id).first()
    assert db_user.age == user_update_data['age']
    assert db_user.height == user_update_data['height']
    assert db_user.weight == user_update_data['weight']
    assert db_user.exercise_level == user_update_data['exercise_level']
    
    