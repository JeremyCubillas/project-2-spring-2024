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

        records = user.sample_calcs
        for record in records:
            record.z_score = 1
            record.save()
        for record in records:
            assert record.z_score == 1


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
