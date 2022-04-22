from .serializer import Serializer


class JwtSerializer(Serializer):
    response = {
        "id": str,
        "roles_list": {
            "label": "roles",
            "type": list
        }
    }
