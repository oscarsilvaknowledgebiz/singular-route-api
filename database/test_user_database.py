import pytest
from database import user_database
from core.schemes import user_schemes


user = user_schemes.UserPost()
user.name = "Oscar"
user.email = "teste@email.pt"
user.receives_notification = False
user.notification_email = "test.notifications@email.pt"
user.password = "test.password1234"
user.picture = "image.png"
user.phone = "999999999"
user.birth_date = "01-01-2000"
user.gmail_access_token = ""
user.exponent_push_token = ""
user.address.city = "city"
user.address.street = "street"
user.address.country = "country"
user.address.postal_code = "2222-222"
user.address.door_number = "1J"


def test_user_database():
    response = user_database.add_user(user)
    assert response is True
