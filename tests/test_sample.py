"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User, SampleCalc


def test_sample_calc_model(app, create_5_users):
    with app.app_context():
        assert SampleCalc.record_count() == 0
        sample_calc = SampleCalc(z_score=2.58, margin_error=.05, std=.5, population_size=425)
        assert sample_calc.calc_sample_size == 259.39
        user = User.get_random_record()
        user.sample_calcs.append(sample_calc)
        user.save()
        assert SampleCalc.record_count() == 1


def test_sample_calc_route(app, client, login):
    with app.app_context():
        assert SampleCalc.record_count() == 0

    with client:
        response = client.post("/sample_size", data={
            "z_score": "2.58",
            "margin_error": ".05",
            "std": ".5",
            "population_size": "425"
        }, follow_redirects=True)
        with app.app_context():
            assert SampleCalc.record_count() == 1

        assert response.status_code == 200
        assert response.request.path == url_for('sample_size.my_sample_calcs')
        assert b"259.39" in response.data


def test_sample_size_login_redirect_route(client):
    response = client.post("/registration", data={
        "email": "steve@steve.com",
        "password": "testtest",
        "confirm": "testtest",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('authentication.login')
    response = client.get("/sample_size", follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('authentication.login')
    response = client.get(
        "/login?next=%2Fsample_size",
        follow_redirects=True
    )
    response = client.post(
        "/login?next=%2Fsample_size",
        data=dict(email='steve@steve.com', password='testtest'),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert response.request.path == url_for('sample_size.sample_size_page')


def test_menu_calculate_sample_unauthenticated(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculate Sample" in response.data


def test_main_menu_authenticated(client, login):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Calculate Sample" in response.data
    assert b"My Sample Sizes" in response.data
    assert b"Logout" in response.data
    assert b"My Profile" in response.data
