from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Confirmed,
    Email,
    Max,
    Min,
    Regex,
    Required,
    Unique,
)
from ms.helpers.regex import phone_regex, password_regex
from ms.models import User


class RegisterForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User),
            ],
            'phone': [
                Required(),
                Min(9),
                Max(15),
                Regex(phone_regex, message='The phone is invalid'),
                Unique(User),
            ],
            'password': [
                Required(),
                Min(6),
                Max(255),
                Regex(password_regex, message='The password is invalid'),
                Confirmed(),
            ],
            'password_confirmation': [Required()],
        }
