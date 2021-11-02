from typing import Union
from ms.db import db
from wtforms.validators import ValidationError


class Unique():
    def __init__(self, model: db.Model,
                 column: Union[str, None] = None,
                 message: Union[str, None] = None) -> None:
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field) -> None:
        column = self.column or field.name
        message = self.message or f'The {field.data} has already been taken.'

        exists = self.model.query.filter_by(**{column: field.data}).count()

        if exists:
            raise ValidationError(message)


class CheckPassword():
    def __init__(self, model: db.Model,
                 column: Union[str, None] = None,
                 password_field: Union[str, None] = None,
                 message: Union[str, None] = None) -> None:
        self.model = model
        self.column = column
        self.password_field = password_field or 'password'
        self.message = message

    def __call__(self, form, field) -> None:
        password = form[self.password_field].data
        column = self.column or field.name
        message = self.message or 'These credentials do not match our records.'

        user = self.model.query.filter_by(**{column: field.data}).first()
        print(user, column, field.data, password)
        if user is None or not user.verify_password(password):
            raise ValidationError(message)
