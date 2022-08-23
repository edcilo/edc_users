from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Max, Nullable, Required, Unique)
from ms.models import App


class AppUpdateForm(FormRequest):
    def rules(self):
        app_id = self.request.view_args.get('id')

        return {
            'name': [
                Required(),
                Max(255),
                Unique(App, except_id=app_id)],
            'description': [
                Nullable(),
                Max(512)], }
