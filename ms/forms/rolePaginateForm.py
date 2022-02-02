from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import In, Integer, Nullable


class RolePaginateForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'q': [Nullable()],
            'order': [Nullable(), In(("asc", "desc"))],
            'page': [Nullable(), Integer()],
            'per_page': [Nullable(), Integer()],
        }
