from faker import Faker

from application.database import User, db


def test_address_field(client, create_300_users):

    response = client.get("/users/1")
    assert response.status_code == 200
    assert b"Address" in response.data
    assert b"9335 Gloria Street Suite" in response.data