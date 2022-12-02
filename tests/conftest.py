import pytest
from faker import Faker

from application import init_app as create_app
from application.database import db, User

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['en']

@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 4321

@pytest.fixture(scope="function")
def create_300_users(app, faker):
    user_list = []
    number_of_users = 300

    with app.app_context():
        for i in range(number_of_users):
            user = User(faker.email(), faker.password())
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()


@pytest.fixture(scope="function")
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False

    })

    # other setup can go here
    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield app

        db.session.remove()
        # Uncomment To Reset Database After Test
        # db.drop_all()

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="function")
def app_clean_db():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here
    with app.app_context():
        db.session.remove()
        db.drop_all()
        yield app
        db.session.remove()
