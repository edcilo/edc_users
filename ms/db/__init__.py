from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from ms import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)
