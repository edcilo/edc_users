from .serializer import Serializer


class RoleSerializer(Serializer):
    response = {
        'id': str,
        'name': str,
    }


class UserRoleSerializer(Serializer):
    response = {
        'name': str,
    }
