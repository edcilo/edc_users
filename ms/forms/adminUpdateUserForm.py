from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Email,
    Max,
    Min,
    Nullable,
    Regex,
    Required,
    Unique,
)
from ms.helpers import regex
from ms.models import User


class AdminUpdateUserForm(FormRequest):
    def rules(self):
        user_id = self.request.view_args.get('id')

        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User, except_id=user_id)
            ],
            'phone': [
                Required(),
                Min(10),
                Max(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user_id)
            ],
            'name': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The name is invalid'),
            ],
            'lastname': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The lastname is invalid'),
            ],
            'mothername': [
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The mothername is invalid'),
            ],
        }
