import os
import pytest
import shutil
import tempfile
from flask_migrate import init, migrate, upgrade
from flask_seeder import cli
from ms import app as app_
from ms.helpers.utils import random_string
from ms.repositories import RoleRepository, UserRepository
from helpers import RedisWrapper


@pytest.fixture
def app():
    ran = random_string(6)
    migrations_path = os.path.join(tempfile.gettempdir(), f'migrations_{ran}')
    db_fd, db_path = tempfile.mkstemp()

    with app_.app_context():
        app_.config.update(TESTING=True)
        app_.config.update(SECRET_KEY='testingapp')
        app_.config.update(SQLALCHEMY_DATABASE_URI=f'sqlite:///{db_path}')
        app_.cache.conn = RedisWrapper()
        init(directory=migrations_path)
        migrate(directory=migrations_path)
        upgrade(directory=migrations_path)
        exec_seeders(app_, root='./ms/db/seeders')

    yield app_

    os.close(db_fd)
    os.unlink(db_path)
    shutil.rmtree(migrations_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth(client):
    return AuthActions(client)


@pytest.fixture
def runner(app):
    return app.test_cli_runner()



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

    def superuser(self):
        ur = UserRepository()
        rr = RoleRepository()
        root_role = rr.find_by_attr('name', 'root')
        user = ur.add({
            "email": "root@example.com",
            "phone": "0000000000",
            "password": "secret",
            "role_id": root_role.id
        })
        return user

    def register(self, email="admin@example.com", phone="1231231231", password="secret"):
        return self._client.post(
            "/api/v1/users/register", data={
                "phone": phone,
                "email": email,
                "password": password,
                "password_confirmation": password
            }
        )

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
