from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    In, Nullable, Integer)


class AppListForm(FormRequest):
    def rules(self):
        return {
            'q': [Nullable()],
            'order': [
                Nullable(),
                In(("asc", "desc"))
            ],
            'order_column': [
                Nullable(),
                In(("email", "phone", "name", "lastname", "created_at"))
            ],
            'page': [Nullable(), Integer()],
            'per_page': [Nullable(), Integer()], }
