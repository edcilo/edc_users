import os
import pytest
import random
import string
import shutil
import tempfile
from flask_migrate import init, migrate, upgrade
from flask_seeder import cli
from ms import app as msapp


@pytest.fixture
def app():
    ran = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=6))
    migrations_path = os.path.join(tempfile.gettempdir(), f'migrations_{ran}')
    db_fd, db_path = tempfile.mkstemp()

    with msapp.app_context():
        msapp.config.update(TESTING=True)
        msapp.config.update(SECRET_KEY='testingapp')
        msapp.config.update(
            SQLALCHEMY_DATABASE_URI=f'sqlite:///{db_path}')
        init(directory=migrations_path)
        migrate(directory=migrations_path)
        upgrade(directory=migrations_path)
        exec_seeders(msapp, root='./ms/db/seeders')

    yield msapp

    os.close(db_fd)
    os.unlink(db_path)
    shutil.rmtree(migrations_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth(client):
    return AuthActions(client)


def exec_seeders(app, root):
    db = app.extensions["flask_seeder"].db
    for seeder in cli.get_seeders(root):
        seeder.db = db
        try:
            seeder.run()
        except Exception as e:
            print(f"{seeder.name}...\t[ERROR]")
            print(f"\t {e}")
            db.session.rollback()
            continue

    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="admin@example.com", password="secret"):
        return self._client.post(
            "/api/v1/users/login", data={"username": username, "password": password}
        )

    def get_token(self, username="admin@example.com", password="secret"):
        response = self.login(username, password)
        return response.json.get('token')

    def get_refreshtoken(self, username="admin@example.com", password="secret"):
        response = self.login(username, password)
        return response.json.get('refresh_token')
