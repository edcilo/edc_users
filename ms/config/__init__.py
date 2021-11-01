import os
from ms import app


DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


config = {
    'app': {
        'APP_NAME': os.getenv('APP_NAME', 'app'),
        'APP_VERSION': os.getenv('APP_VERSION', '0.0.0'),
        'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
        'TIMEZONE': os.getenv('APP_TIMEZONE', 'UTC'),
    },
    'db': {
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    },
}


app.config.update(**config['app'])
app.config.update(**config['db'])
