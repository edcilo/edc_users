import os


storage_config = {
    'S3': {
        'ACCESS_KEY': os.getenv('S3_ACCESS_KEY', None),
        'SECRET_KEY': os.getenv('S3_SECRET_KEY', None),
        'REGION': os.getenv('S3_REGION', None),
        'BUCKET': os.getenv('S3_BUCKET', None),
    }
}
