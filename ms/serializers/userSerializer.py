from ms.serializers.Serializer import Serializer


class UserSerializer(Serializer):
    response = ("id", "username", "email",)
