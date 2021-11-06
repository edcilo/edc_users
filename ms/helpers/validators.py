from sqlalchemy import or_
from typing import Union
from wtforms.validators import ValidationError
from ms.db import db


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
                 column: Union[str, list, tuple, None] = None,
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

        filters = [getattr(self.model, column) == field.data] \
            if isinstance(column, str) \
            else [getattr(self.model, key) == field.data for key in column]

        user = self.model.query.filter(or_(*filters)).first()
        if user is None or not user.verify_password(password):
            raise ValidationError(message)
