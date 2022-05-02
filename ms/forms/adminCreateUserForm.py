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
                Min(9),
                Max(15),
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
                Max(50)
            ],
            'lastname': [
                Nullable(),
                Max(50)
            ],
            'mothername': [
                Nullable(),
                Max(50)
            ],
            'role_id': [
                Required(),
                Exists(Role, 'id', message="The role does not exist")
            ]
        }