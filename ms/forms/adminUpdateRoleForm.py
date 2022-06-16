from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Boolean, Max, Required, Unique
from ms.models import Role


class AdminUpdateRoleForm(FormRequest):
    def rules(self):
        role_id = self.request.view_args.get('id')

        return {
            'name': [
                Required(),
                Max(120),
                Unique(
                    Role,
                    except_id=role_id,
                    message="The role name has already been taken.")],
            'fixed': [
                Required(),
                Boolean()]}
