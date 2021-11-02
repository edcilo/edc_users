import pytest, os, shutil, random, re, string
from pathlib import Path
from flask_migrate import downgrade, init, migrate, stamp, upgrade
from ms import app as ms_app



class DB():
    def set_migrations_paths(self):
        chars = 6
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = chars))
        return ran
    def start(self, app):
        with app.app_context():
            suffix = self.set_migrations_paths()
            migrations_path = f'/tmp/migrations_{suffix}'
            app.config.update(**{
                'SQLALCHEMY_DATABASE_URI': f'sqlite:////tmp/test_{suffix}.db'
            })
            init(directory=migrations_path)
            migrate(directory=migrations_path)
            upgrade(directory=migrations_path)
    def cleanup(self, app):
        for dir in os.listdir('/tmp'):
            if (re.search('migrations_*', dir)):
                shutil.rmtree(f'/tmp/{dir}')

        for p in Path('/tmp').glob('test_*.db'):
            p.unlink()


@pytest.fixture
def app():
    with ms_app.app_context():
        pass

    yield ms_app

@pytest.fixture
def db():
    return DB()

@pytest.fixture
def client(app, db):
    db.start(app)
    with app.test_client() as client:
        yield client
    db.cleanup(app)
