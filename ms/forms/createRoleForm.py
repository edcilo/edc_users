from typing import Iterable
from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    AlphaDash,
    Max,
    Required,
    Unique,
)
from ms.models import Role


class CreateRoleForm(FormRequest):
    def rules(self) -> dict[str, Iterable]:
        return {
            'name': [
                Required(),
                Max(60),
                AlphaDash(),
                Unique(Role),
            ],
        }
