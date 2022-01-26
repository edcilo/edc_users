from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Required


class LoginForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'username': [Required()],
            'password': [Required()]
        }
