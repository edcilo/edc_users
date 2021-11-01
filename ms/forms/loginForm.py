from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    password = StringField('password', validators=[DataRequired(),])
    username = StringField('username', validators=[DataRequired(),])
