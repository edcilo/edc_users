import os


app_config = {
    'APP_NAME': os.getenv('APP_NAME', 'app'),
    'APP_VERSION': os.getenv('APP_VERSION', '1.0.0'),
    'ENV': os.getenv('APP_ENV', 'development'),
    'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
}
