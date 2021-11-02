from .Serializer import Serializer


class UserSerializer(Serializer):
    response = ("id", "username", "email",)
