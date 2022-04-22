from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Boolean, Max, Required, Unique
from ms.models import Permission


class AdminCreatePermissionForm(FormRequest):
    def rules(self):
        return {
            'name': [
                Required(),
                Max(120),
                Unique(
                    Permission,
                    message="The permission name has already been taken.")],
            'fixed': [
                Required(),
                Boolean()]}
