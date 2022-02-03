from datetime import datetime
from fixture import app
from ms.helpers import time
from ms.helpers.jwt import JwtHelper


def test_jwt_helper_encode(app):
    with app.app_context():
        jwt = JwtHelper()
        token = jwt.encode({'foo': 'bar'}, 60)
        assert isinstance(token, str) == True


def test_jwt_helper_decode(app):
    with app.app_context():
        jwt = JwtHelper()
        data = {'foo': 'bar'}
        token = jwt.encode(data, 60)
        payload = jwt.decode(token)
        assert isinstance(payload, dict) == True
        assert payload == data


def test_jwt_helper_get_tokens(app):
    with app.app_context():
        jwt = JwtHelper()
        token = jwt.get_tokens({'foo': 'bar'})
        assert isinstance(token, dict) == True
        assert list(token.keys()) == ['token', 'refresh_token']


def test_jwt_helper_check(app):
    with app.app_context():
        jwt = JwtHelper()
        token = jwt.encode({'foo': 'bar'}, 60)
        valid = jwt.check(token)
        assert valid == True


def test_jwt_helper_check_invalid_token(app):
    with app.app_context():
        jwt = JwtHelper()
        valid = jwt.check('abcde01234.')
        assert valid == False


def test_time_helper_now(app):
    with app.app_context():
        now = time.now()
        assert isinstance(now, datetime)


def test_time_helper_epoch(app):
    with app.app_context():
        epoch = time.epoch_now()
        assert isinstance(epoch, int)
