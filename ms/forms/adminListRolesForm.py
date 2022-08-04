from flaskFormRequest import FormRequest
from flaskFormRequest.validators import In, Integer, Nullable


class AdminListRolesForm(FormRequest):
    def rules(self):
        return {
            'q': [Nullable()],
            'order': [Nullable(), In(("asc", "desc"))],
            'order_column': [Nullable(), In(("name", "created_at"))],
            'page': [Nullable(), Integer()],
            'per_page': [Nullable(), Integer()],
        }
