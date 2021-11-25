from wtforms import StringField
from wtforms.validators import (
    DataRequired,
)
from .form import FormRequest


class LoginForm(FormRequest):
    def rules(self, request):
        return {
            'username': StringField('username', validators=[
                DataRequired(),
            ]),
            'password': StringField('password', validators=[
                DataRequired(),
            ])
        }
