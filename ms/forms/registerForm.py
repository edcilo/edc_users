from ms.models.user import User
from ms.helpers.validators import Unique
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
)


class RegisterForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('username', validators=[DataRequired(), Length(min=3, max=120), Unique(User)])
    password = StringField('password', validators=[DataRequired(), Length(min=6, max=120)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=255), Unique(User)])
