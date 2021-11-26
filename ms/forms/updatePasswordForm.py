from typing import Callable, Type

from flask import Request
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
    Regexp,
)
from ms.helpers.regex import password_regex
from .form import FormRequest


class UpdatePasswordForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        return {
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
