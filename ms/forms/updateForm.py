from ms.models.user import User
from ms.helpers.validators import Unique
from flask_wtf import FlaskForm
from .form import Form
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Regexp
)


class UpdateForm(Form):
    class Meta:
        csrf = False

    username = StringField('username', validators=[
        DataRequired(),
        Length(min=3, max=120),
        Regexp(
            '^\\w+$',
            message="Username must contain only letters numbers or underscore"),
        ])
    email = StringField('email', validators=[
        DataRequired(),
        Email(),
        Length(max=255),
        ])
