from typing import Type, Union
from wtforms.validators import ValidationError
from flask_sqlalchemy import Model


class PasswordConfirmation():
    def __init__(self, user: Type[Model],
                 column: Union[str, None] = None,
                 message: Union[str, None] = None) -> None:
        self.user = user
        self.column = column
        self.message = message

    def __call__(self, form, field) -> None:
        password = field.data
        message = self.message or f'The password is incorrect.'
        if not self.user.verify_password(password):
            raise ValidationError(message)
