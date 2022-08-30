from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Boolean, Max, Regex, Required, Unique
from ms.helpers import regex
from ms.models import Permission


class AdminCreatePermissionForm(FormRequest):
    def rules(self):
        return {
            'name': [
                Required(),
                Max(120),
                Regex(regex.personal_name_regex, message='The name is invalid'),
                Unique(
                    Permission,
                    message="The permission name has already been taken.")],
            'fixed': [
                Required(),
                Boolean()]}
