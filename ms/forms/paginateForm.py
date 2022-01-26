from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import In, Integer, Nullable


class PaginateForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'q': [Nullable()],
            'order': [Nullable(), In(("asc", "desc"))],
            'order_column': [Nullable(), In(("email", "name", "lastname", "mothername", "phone"))],
            'page': [Nullable(), Integer()],
            'per_page': [Nullable(), Integer()],
        }
