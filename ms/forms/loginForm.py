from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from ms.helpers.validators import CheckPassword
from ms.models import User


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    password = StringField('password', validators=[DataRequired(), ])
    username = StringField('username', validators=[
        DataRequired(),
        CheckPassword(User)])
