import os, time
from datetime import datetime, timezone
from ms import app


utc = timezone.utc
app_tz = app.config.get('APP_TIMEZONE', 'UTC')


os.environ['TZ'] = app_tz
time.tzset()


def now():
    return datetime.now(tz=utc)

def epoch_now():
    return int(time.time())
