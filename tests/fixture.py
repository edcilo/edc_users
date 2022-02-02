import os
import pytest
import random
import string
import shutil
import tempfile
from flask_migrate import init, migrate, upgrade
from flask_seeder import cli
from ms import app


@pytest.fixture
def client():
    ran = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=6))
    db_path = os.path.join(tempfile.gettempdir(), f'migrations_{ran}')
    db_file = tempfile.NamedTemporaryFile()

    with app.test_client() as client:
        with app.app_context():
            app.config.update(
                SQLALCHEMY_DATABASE_URI=f'sqlite:///{db_file.name}')
            init(directory=db_path)
            migrate(directory=db_path)
            upgrade(directory=db_path)
            exec_seeders(app, root='./ms/db/seeders')
        yield client

    db_file.close()
    shutil.rmtree(db_path)


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
