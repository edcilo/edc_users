import time
import datetime


def now():
    utc = datetime.timezone.utc
    return datetime.datetime.now(tz=utc)


def datetime_to_epoch(date):
    if isinstance(date, datetime.date):
        date = datetime.datetime.combine(
            date, datetime.datetime.min.time())
    return int(date.timestamp())


def epoch_now():
    return int(time.time())
