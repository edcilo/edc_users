from datetime import datetime
from fixture import app, client, db
from helpers import createJhonDoe
from ms.models import User
from ms.repositories import userRepo
from ms.serializers import UserSerializer
from ms.helpers import ( jwt, time )



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


def test_user_repo_add(client):
    data = {
        'username': 'jhon.doe',
        'password': 'secret',
        'email': 'jhon.doe@example.com',
    }
    user = userRepo.add(data)
    assert isinstance(user, User)
    assert user.username == data['username']

def test_user_repo_find(client):
    data = {
        'username': 'jhon.doe',
        'password': 'secret',
        'email': 'jhon.doe@example.com',
    }
    userRepo.add(data)
    user = userRepo.find(1)
    assert isinstance(user, User)
    assert user.id == 1

def test_user_repo_find_by_attr(client):
    data = {
        'username': 'jhon.doe',
        'password': 'secret',
        'email': 'jhon.doe@example.com',
    }
    userRepo.add(data)
    user = userRepo.find_by_attr('email', data['email'])
    assert isinstance(user, User)
    assert user.email == data['email']


def test_user_serializer(client):
    user = createJhonDoe()
    serializer = UserSerializer(user)
    assert isinstance(serializer.data, dict)
    assert list(serializer.data.keys()) == ['id', 'username', 'email']
