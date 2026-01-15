from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'testuser1'
    assert response.json()['email'] == 'testuser1@example.com'
    assert response.json()['first_name'] == 'Test'
    assert response.json()['last_name'] == 'User'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'



def test_change_password_success(test_user):
    response = client.put("/users/password", json={
        "password": "password123",
        "new_password": "newpassword456"
    })
    assert response.status_code == status.HTTP_200_OK

def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/password", json={
        "password": "wrongpassword",
        "new_password": "newpassword456"
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}


def test_change_phone_number_success(test_user):
    response = client.put("/users/phonenumber/0987654321")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    








