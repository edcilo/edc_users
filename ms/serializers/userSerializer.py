from ms.helpers import time
from .serializer import Serializer
from .permissionSerializer import PermissionSerializer
from .roleSerializer import RoleSerializer


class UserSerializer(Serializer):
    response = {
        "id": str,
        "email": str,
        "phone": str,
        "name": str,
        "lastname": str,
        "mothername": str,
        "is_active": bool,
        "created_at": time.datetime_to_epoch,
        "deleted_at": lambda date: time.datetime_to_epoch(date) if date is not None else None,
    }


class UserPermissionsSerializer(Serializer):
    response = {
        "id": str,
        "email": str,
        "phone": str,
        "name": str,
        "lastname": str,
        "mothername": str,
        "is_active": bool,
        "created_at": time.datetime_to_epoch,
        "deleted_at": lambda date: time.datetime_to_epoch(date) if date is not None else None,
        "all_permissions": {
            "label": "permissions",
            "type": PermissionSerializer},
        "roles": RoleSerializer}
