from ms.helpers import time
from .serializer import Serializer
from .permissionSerializer import PermissionSerializer
from .roleSerializer import RoleSerializer


class ProfileSerializer(Serializer):
    response = {
        "rfc": str,
        "curp": str,
        "home_phone": str,
        "birthday": lambda date: date.strftime("%Y-%m-%d") if date else None,
        "gender": str
    }


class UserProfileSerializer(Serializer):
    response = {
        "id": str,
        "email": str,
        "phone": str,
        "name": str,
        "lastname": str,
        "mothername": str,
        "is_active": bool,
        "created_at": time.datetime_to_epoch,
        "deleted_at": lambda date: time.datetime_to_epoch(date) if date else None,
        "profile": {
            "type": ProfileSerializer}}
