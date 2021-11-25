from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Regexp
)
from ms.models import User
from ms.helpers.regex import phone_regex
from ms.forms.validators.unique import Unique
from .form import FormRequest


class UpdateForm(FormRequest):
    def rules(self, request) -> dict:
        user_id = request.view_args.get('id')

        return {
            'email': StringField('email', validators=[
                DataRequired(),
                Email(),
                Length(max=255),
                Unique(User, except_id=user_id),
            ]),
            'phone': StringField('phone', validators=[
                DataRequired(),
                Length(min=9, max=15),
                Regexp(phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user_id),
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
