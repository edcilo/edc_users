from .form import Form
from ms.helpers.validators import Unique
from ms.models.user import User
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

    phone = StringField('phone', validators=[
        DataRequired(),
        Length(min=9, max=15),
        Regexp('^\\+?1?\\d{9,15}$'),
        Unique(User)])
    email = StringField('email', validators=[
        DataRequired(),
        Email(),
        Length(max=255),
    ])
