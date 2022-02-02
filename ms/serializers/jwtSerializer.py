from urllib import response
from .serializer import Serializer
from .roleSerializer import UserRoleSerializer


class JwtSerializer(Serializer):
    response = {
        'id': str,
        'role': UserRoleSerializer,
    }
