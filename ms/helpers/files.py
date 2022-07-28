import random
import string
from datetime import datetime
from fileStorage3 import S3
from ms import app


def s3_session():
    return S3({
        "aws_access_key_id": app.config.get("S3").get("ACCESS_KEY"),
        "aws_secret_access_key": app.config.get("S3").get("SECRET_KEY"),
        "region": app.config.get("S3").get("REGION"),
        "bucket": app.config.get("S3").get("BUCKET")
    })


def upload_file(origin, destination):
    s3 = s3_session()
    return s3.put(origin, destination)


def generate_client_filename(client, file):
    letters = string.ascii_lowercase
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    rand = ''.join(random.choice(letters) for i in range(6))
    ext = file.filename.split(".")[-1]
    return f"{client.id}_{now}_{rand}.{ext}"
