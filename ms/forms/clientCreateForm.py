from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Date,
    Email,
    In,
    Max,
    Min,
    Nullable,
    Regex,
    Required,
    Size,
    Unique,
)
from ms.helpers import regex
from ms.models import User, Profile


class ClientCreateForm(FormRequest):
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
                Required(),
                Max(50)
            ],
            'lastname': [
                Required(),
                Max(50)
            ],
            'mothername': [
                Required(),
                Nullable(),
                Max(50)
            ],
            'rfc': [
                Required(),
                Size(13),
                Unique(Profile)
            ],
            'curp': [
                Required(),
                Size(18),
                Unique(Profile)
            ],
            'home_phone': [
                Nullable(),
                Min(9),
                Max(15),
                Regex(regex.phone_regex, message='The phone is invalid'),
            ],
            'birthday': [
                Nullable(),
                Date(format="%Y-%m-%d")
            ],
            'gender': [
                Nullable(),
                In(['M', 'F'])
            ],
        }
