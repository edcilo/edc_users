from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Regexp
)
from ms.models import User
from ms.helpers.regex import phone_regex, password_regex
from ms.forms.validators.unique import Unique
from .form import FormRequest


class CreateForm(FormRequest):
    def rules(self, request):
        return {
            'email': StringField('email', validators=[
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
                Length(max=255),
                Regexp(password_regex, message='The password is invalid'),
            ]),
            'name': StringField('name', validators=[
                Length(max=50),
            ]),
            'lastname': StringField('lastname', validators=[
                Length(max=50),
            ]),
            'mothername': StringField('lastname', validators=[
                Length(max=50),
            ]),
        }
