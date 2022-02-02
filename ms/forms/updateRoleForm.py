from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    AlphaDash,
    Max,
    Required,
    Unique,
)
from ms.models import Role


class UpdateRoleForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        role_id = self.request.view_args.get('id')

        return {
            'name': [
                Required(),
                Max(60),
                AlphaDash(),
                Unique(Role, except_id=role_id),
            ],
        }
