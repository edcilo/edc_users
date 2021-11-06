from .Serializer import Serializer


class UserSerializer(Serializer):
    response = {"id": str, "username": str, "email": str, }
