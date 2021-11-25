from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
)
from ms.models import User
from ms.helpers.regex import phone_regex, password_regex
from ms.forms.validators.unique import Unique
from .form import FormRequest


class RegisterForm(FormRequest):
    def rules(self, request):
        return {
            'email': StringField('emai', validators=[
                DataRequired(),
                Email(),
                Length(max=255),
                Unique(User),
            ]),
            'phone': StringField('phone', validators=[
                DataRequired(),
                Length(min=9, max=15),
                Regexp(phone_regex, message='The phone is invalid'),
                Unique(User),
            ]),
            'password': StringField('password', validators=[
                DataRequired(),
                Length(min=6, max=255),
                Regexp(password_regex, message='The password is invalid'),
                EqualTo('password_confirmation')
            ]),
            'password_confirmation': StringField('password_confirmation',
                                                 validators=[
                                                     DataRequired(),
                                                 ])
        }
