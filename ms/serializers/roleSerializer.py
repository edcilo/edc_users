from ms.helpers import time
from .serializer import Serializer
from .permissionSerializer import PermissionSerializer


class RoleSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "fixed": bool,
        "created_at": time.datetime_to_epoch
    }


class RolePermissionsSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "fixed": bool,
        "created_at": time.datetime_to_epoch,
        "permissions": PermissionSerializer
    }
