from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from ms import app
from ms.models import Model


db = SQLAlchemy(app, model_class=Model)
migrate = Migrate(app, db)

seeder = FlaskSeeder()
seeder.init_app(app, db)
