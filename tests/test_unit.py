from datetime import datetime
from fixture import client
from ms.helpers import jwt, time


def test_jwt_helper_encode():
    token = jwt.jwtHelper.encode({'foo': 'bar'}, 60)
    assert isinstance(token, str) == True

def test_jwt_helper_decode():
    data = {'foo': 'bar'}
    token = jwt.jwtHelper.encode(data, 60)
    payload = jwt.jwtHelper.decode(token)
    assert isinstance(payload, dict) == True
    assert payload == data

def test_jwt_helper_get_tokens():
    token = jwt.jwtHelper.get_tokens({'foo': 'bar'})
    assert isinstance(token, dict) == True
    assert list(token.keys()) == ['token', 'refresh_token']

def test_jwt_helper_check():
    token = jwt.jwtHelper.encode({'foo': 'bar'}, 60)
    valid = jwt.jwtHelper.check(token)
    assert valid == True

def test_jwt_helper_check_invalid_token():
    valid = jwt.jwtHelper.check('abcde01234.')
    assert valid == False

def test_time_helper_now():
    now = time.now()
    assert isinstance(now, datetime)

def test_time_helper_epoch():
    epoch = time.epoch_now()
    assert isinstance(epoch, int)
