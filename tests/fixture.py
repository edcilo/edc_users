import os
import pytest
import random
import string
import shutil
import tempfile
from flask_migrate import init, migrate, upgrade
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
        yield client

    db_file.close()
    shutil.rmtree(db_path)
