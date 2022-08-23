import pytz
from datetime import (
    date as datetime_instance,
    datetime)
from ms import app


app_tz: str = app.config.get('TIMEZONE')


def now(tz: str = app_tz) -> datetime:
    return datetime.now(tz=pytz.timezone(tz))


def datetime_to_epoch(date: datetime) -> int:
    return int(date.timestamp())


def epoch_now() -> int:
    return datetime_to_epoch(now())
