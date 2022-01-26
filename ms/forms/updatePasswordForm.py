from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Confirmed,
    Max,
    Min,
    Regex,
    Required,
)
from ms.helpers.regex import password_regex


class UpdatePasswordForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'password': [
                Required(),
                Min(6),
                Max(255),
                Regex(password_regex, message='The password is invalid'),
                Confirmed(),
            ],
            'password_confirmation': [
                Required(),
            ]
        }
