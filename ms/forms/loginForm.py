from wtforms import StringField
from wtforms.validators import DataRequired
from .form import Form
from ms.helpers.validators import CheckPassword
from ms.models import User


class LoginForm(Form):
    class Meta:
        csrf = False

    password = StringField('password', validators=[DataRequired(), ])
    username = StringField('username', validators=[
        DataRequired(),
        CheckPassword(User, column=('email', 'phone'))])
