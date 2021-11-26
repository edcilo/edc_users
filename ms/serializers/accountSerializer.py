from .serializer import Serializer


class AccountSerializer(Serializer):
    response = {
        'id': str,
        'usernme': str,
        'email': str,
        'phone': str,
        'name': str,
        'lastname': str,
        'is_active': str,
    }
