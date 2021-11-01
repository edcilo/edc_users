import os
from ms import app


config = {
    'app': {
        'APP_NAME': os.getenv('APP_NAME', 'app'),
        'APP_VERSION': os.getenv('APP_VERSION', '0.0.0'),
        'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
        'TIMEZONE': os.getenv('APP_TIMEZONE', 'UTC'),
    }
}


app.config.update(**config['app'])
