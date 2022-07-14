from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Date,
    In,
    Max,
    Min,
    Nullable,
    Regex,
    Size,
    Required,
    Unique,
)
from ms.helpers import regex
from ms.models import Profile


class AccountUpdateProfileForm(FormRequest):
    def rules(self):
        user = self.request.auth.get('user')
        return {
            'rfc': [
                Required(),
                Size(13),
                Unique(Profile, except_id=user.profile.id)
            ],
            'curp': [
                Required(),
                Size(18),
                Unique(Profile, except_id=user.profile.id)
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
