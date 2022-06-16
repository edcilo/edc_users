from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Required


class AuthLoginForm(FormRequest):
    def rules(self):
        return {
            'username': [Required()],
            'password': [Required()]
        }
