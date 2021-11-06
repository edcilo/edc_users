from .Serializer import Serializer


class UserSerializer(Serializer):
    response = {"id": str, "phone": str, "email": str, }
