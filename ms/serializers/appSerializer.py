from ms.helpers import time
from .serializer import Serializer
from .permissionSerializer import PermissionSerializer
from .roleSerializer import RoleSerializer


class AppSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "description": str,
        "created_at": time.datetime_to_epoch,
        "all_permissions": {
            "label": "permissions",
            "type": PermissionSerializer},
        "roles": RoleSerializer
    }
