from fixture import client
from ms.serializers import UserSerializer
from ms.models import User
import uuid

def test_user_serializer():
    user = User({
        'phone': '1231231231',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
        'role_id': str(uuid.uuid4()),
    })
    serializer = UserSerializer(user)
    assert tuple(serializer.get_data().keys()) == ('id', 'phone', 'email', 'name', 'lastname', 'mothername', 'role')


def test_user_collection_serializer():
    user = User({
        'phone': '1231231231',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
        'role_id': str(uuid.uuid4()),
    })
    serializer = UserSerializer([user], collection=True)
    assert len(serializer.get_data()) == 1
    assert type(serializer.get_data()) == list
