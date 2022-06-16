from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Boolean, Max, Required, Unique
from ms.models import Role


class AdminCreateRoleForm(FormRequest):
    def rules(self):
        return {
            'name': [
                Required(),
                Max(120),
                Unique(Role, message="The role name has already been taken.")
            ],
            'fixed': [
                Required(),
                Boolean()
            ]
        }
