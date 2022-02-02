from .serializer import Serializer
from .roleSerializer import RoleSerializer


class AccountSerializer(Serializer):
    response = {
        'id': str,
        'usernme': str,
        'email': str,
        'phone': str,
        'name': str,
        'lastname': str,
        'is_active': str,
        'role': RoleSerializer,
    }
