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
from ms.helpers import regex
from ms.models import User


class AuthRegisterForm(FormRequest):
    def rules(self):
        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User),
            ],
            'phone': [
                Required(),
                Min(10),
                Max(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User),
            ],
            'password': [
                Required(),
                Min(6),
                Max(255),
                Regex(regex.password_regex, message='The password is invalid'),
                Confirmed(),
            ],
            'password_confirmation': [Required()],
        }
