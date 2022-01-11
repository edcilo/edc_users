import os
from dotenv import load_dotenv
from ms import app


load_dotenv()


DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


config = {
    'app': {
        'APP_NAME': os.getenv('APP_NAME', 'app'),
        'APP_VERSION': os.getenv('APP_VERSION', '1.0.0'),
        'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
        'TIMEZONE': os.getenv('APP_TIMEZONE', 'UTC'),
        'URL_PREFIX': '/api/v1/users',
    },
    'db': {
        'SQLALCHEMY_DATABASE_URI': f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    },
}


app.config.update(**config.get('app'))
app.config.update(**config.get('db'))
