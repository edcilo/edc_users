from ms.helpers import time
from .serializer import Serializer
from .permissionSerializer import PermissionSerializer
from .roleSerializer import RoleSerializer


class PersonalReferenceSerializer(Serializer):
    response = {
        "name": str,
        "phone": str,
        "relationship": str,
    }


class ProfileSerializer(Serializer):
    response = {
        "rfc": str,
        "curp": str,
        "home_phone": str,
        "birthday": lambda date: date.strftime("%Y-%m-%d") if date else None,
        "entity_birth": str,
        "gender": str,
        "grade": str,
        "marital_status": str,
        "department": str,
        "street": str,
        "exterior": str,
        "interior": str,
        "neighborhood": str,
        "zip": str,
        "monthly_expenditure": float,
        "income": float,
        "income_family": float,
        "count_home": int,
        "company_name": str,
        "type_activity": str,
        "position": str,
        "time_activity_year": int,
        "time_activity_month": int,
        "personal_references": PersonalReferenceSerializer,
    }


class UserProfileSerializer(Serializer):
    response = {
        "id": str,
        "email": str,
        "phone": str,
        "name": str,
        "lastname": str,
        "second_lastname": str,
        "is_active": bool,
        "created_at": time.datetime_to_epoch,
        "deleted_at": lambda date: time.datetime_to_epoch(date) if date else None,
        "profile": {
            "type": ProfileSerializer},
        "all_permissions": {
            "label": "permissions",
            "type": PermissionSerializer},
        "roles": RoleSerializer}
