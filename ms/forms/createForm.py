from typing import Iterable
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
from ms.helpers.regex import phone_regex, password_regex
from ms.models import Role, User


class CreateForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
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
                Regex(phone_regex, message='The phone is invalid'),
                Unique(User)
            ],
            'password': [
                Required(),
                Max(255),
                Regex(password_regex, message='The password is invalid')
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
                Exists(Role, 'id')
            ],
        }
