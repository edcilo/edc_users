from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Email,
    Max,
    Min,
    Regex,
    Required,
    Unique,
)
from ms.helpers import regex
from ms.models import User


class AccountUpdateAuthForm(FormRequest):
    def rules(self):
        user = self.request.auth.get('user')
        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User, except_id=user.id),
            ],
            'phone': [
                Required(),
                Min(10),
                Max(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user.id),
            ],
        }
