from wtforms import IntegerField, StringField
from wtforms.validators import ValidationError
from .form import Form


class PaginateForm(Form):
    class Meta:
        csrf = False

    q = StringField('q', validators=[])
    order = StringField('order', validators=[])
    page = IntegerField('page', validators=[])
    per_page = IntegerField('per_page', validators=[])

    def validate_order(self, field):
        value = field.data
        if value is not None and value not in ('asc', 'desc'):
            raise ValidationError("Invalid value, must be one of: desc, asc.")
