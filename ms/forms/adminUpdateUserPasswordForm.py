from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Confirmed,
    Max,
    Min,
    Regex,
    Required,
)
from ms.helpers import regex


class AdminUpdateUserPasswordForm(FormRequest):
    def rules(self):
        return {
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
