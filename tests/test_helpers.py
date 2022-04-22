import datetime
from fixture import app
from ms.helpers import jwt, regex, time, utils


def test_jwt_helper_encode(app):
    jwt_ = jwt.JwtHelper()
    token = jwt_.encode({'foo': 'bar'}, 60)
    assert isinstance(token, str) == True


def test_jwt_helper_decode(app):
    jwt_ = jwt.JwtHelper()
    data = {'foo': 'bar'}
    token = jwt_.encode(data, 60)
    payload = jwt_.decode(token)
    assert isinstance(payload, dict) == True
    assert payload == data


def test_jwt_helper_get_tokens(app):
    jwt_ = jwt.JwtHelper()
    token = jwt_.get_tokens({'foo': 'bar'})
    assert isinstance(token, dict) == True
    assert list(token.keys()) == ['token', 'refresh_token']


def test_jwt_helper_check(app):
    jwt_ = jwt.JwtHelper()
    token = jwt_.encode({'foo': 'bar'}, 60)
    valid = jwt_.check(token)
    assert valid == True


def test_jwt_helper_check_invalid_token(app):
    jwt_ = jwt.JwtHelper()
    valid = jwt_.check('abcde01234.')
    assert valid == False


def test_time_now():
    now = time.now()
    assert isinstance(now, datetime.datetime)


def test_time_datetime_to_epoch():
    now = time.now()
    epoch = time.datetime_to_epoch(now)
    assert isinstance(epoch, int)


def test_time_epoch_now():
    now = time.epoch_now()
    assert isinstance(now, int)


def test_utils_random_string():
    randstr1 = utils.random_string(6)
    randstr2 = utils.random_string(6)
    assert len(randstr1) == len(randstr2)
    assert randstr1 != randstr2
