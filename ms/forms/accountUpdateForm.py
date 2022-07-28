from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Max,
    Nullable,
)


class AccountUpdateForm(FormRequest):
    def rules(self):
        return {
            'name': [
                Nullable(),
                Max(50)
            ],
            'lastname': [
                Nullable(),
                Max(50)
            ],
            'mothername': [
                Nullable(),
                Max(50)
            ],
        }
