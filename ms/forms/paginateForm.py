from wtforms import IntegerField, StringField
from wtforms.validators import AnyOf
from .form import FormRequest


class PaginateForm(FormRequest):
    def rules(self, request):
        return {
            'q': StringField('q', validators=[]),
            'order': StringField('order', validators=[AnyOf(('asc', 'desc'))]),
            'page': IntegerField('page', validators=[]),
            'per_page': IntegerField('per_page', validators=[])
        }
