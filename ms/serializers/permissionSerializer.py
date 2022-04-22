from ms.helpers import time
from .serializer import Serializer


class PermissionSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "fixed": bool,
        "created_at": time.datetime_to_epoch
    }
