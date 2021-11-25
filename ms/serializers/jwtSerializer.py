from .serializer import Serializer


class JwtSerializer(Serializer):
    response = {
        'id': str
    }
