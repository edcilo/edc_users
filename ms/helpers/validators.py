from wtforms.validators import ValidationError


class Unique():
    def __init__(self, model, column=None, message=None):
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field):
        column = self.column or field.name
        message = self.message or f'The {field.data} has already been taken.'

        exists = self.model.query.filter_by(**{column: field.data}).count()

        if exists:
            raise ValidationError(message)
