from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Confirmed,
    CurrentPassword,
    Max,
    Min,
    Regex,
    Required,
)
from ms.helpers import regex
from ms.models import User


class AccountUpdatePassword(FormRequest):
    def rules(self):
        user = self.request.auth.get('user')
        return {
            'current_password': [
                Required(),
                CurrentPassword(user),
            ],
            'password': [
                Required(),
                Min(6),
                Max(255),
                Regex(regex.password_regex, message='The password is invalid'),
                Confirmed(),
            ],
            'password_confirmation': [
                Required(),
            ]
        }
