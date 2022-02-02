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
from ms.helpers.regex import phone_regex
from ms.models import Role, User



class UpdateForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        user_id = self.request.view_args.get('id')

        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User, except_id=user_id),
            ],
            'phone': [
                Required(),
                Min(9),
                Max(15),
                Regex(phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user_id),
            ],
            'name': [
                Nullable(),
                Max(50),
            ],
            'lastname': [
                Nullable(),
                Max(50),
            ],
            'mothername': [
                Nullable(),
                Max(50),
            ],
            'role_id': [
                Required(),
                Exists(Role, 'id'),
            ],
        }
