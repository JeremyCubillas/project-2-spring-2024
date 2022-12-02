"""Testing Registration Routes"""



def test_user_registration(client):
    response = client.post("/users", data={
        "email": "steve@steve.com",
        "fname": "Steve",
        "lname": "Stevens",
    })
    assert response.status_code == 200