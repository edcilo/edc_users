from ms.models.user import User
from ms.helpers.validators import Unique
from .form import Form
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Regexp
)


class CreateForm(Form):
    class Meta:
        csrf = False

    phone = StringField('phone', validators=[
        DataRequired(),
        Length(min=9, max=15),
        Regexp('^\\+?1?\\d{9,15}$'),
        Unique(User)])
    password = StringField('password', validators=[
        DataRequired(),
        Length(min=6, max=120)])
    email = StringField('email', validators=[
        DataRequired(),
        Email(),
        Length(max=255),
        Unique(User)])
    name = StringField('name', validators=[Length(max=50), ])
    lastname = StringField('lastname', validators=[Length(max=50), ])
    mothername = StringField('mothername', validators=[Length(max=50), ])
