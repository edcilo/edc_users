from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Email,
    Exists,
    Max,
    Min,
    Nullable,
    Regex,
    Required,
    Unique,
)
from ms.helpers import regex
from ms.models import User, Role


class AdminCreateUserForm(FormRequest):
    def rules(self):
        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User)
            ],
            'phone': [
                Required(),
                Min(10),
                Max(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User)
            ],
            'password': [
                Required(),
                Max(255),
                Regex(regex.password_regex, message='The password is invalid')
            ],
            'name': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The name is invalid'),
            ],
            'lastname': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The lastname is invalid'),
            ],
            'mothername': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The mothername is invalid'),
            ],
            'role_id': [
                Required(),
                Exists(Role, 'id', message="The role does not exist")
            ]
        }
