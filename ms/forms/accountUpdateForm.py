from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Max,
    Nullable,
    Regex,
)
from ms.helpers import regex

class AccountUpdateForm(FormRequest):
    def rules(self):
        return {
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
