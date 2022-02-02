from .serializer import Serializer
from .roleSerializer import RoleSerializer


class UserSerializer(Serializer):
    response = {
        "id": str,
        "phone": str,
        "email": str,
        "name": str,
        "lastname": str,
        "mothername": str,
        'role': RoleSerializer,
    }
