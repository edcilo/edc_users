from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Boolean, Max, Required, Unique
from ms.models import Permission


class AdminUpdatePermissionForm(FormRequest):
    def rules(self):
        permission_id = self.request.view_args.get('id')

        return {
            'name': [
                Required(),
                Max(120),
                Unique(
                    Permission,
                    except_id=permission_id,
                    message="The permission name has already been taken.")],
            'fixed': [
                Required(),
                Boolean()]}
