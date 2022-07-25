from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Max, Nullable, Required, Unique)
from ms.models import App


class AppCreateForm(FormRequest):
    def rules(self):
        return {
            'name': [
                Required(),
                Max(255),
                Unique(App)],
            'description': [
                Nullable(),
                Max(512)],}
