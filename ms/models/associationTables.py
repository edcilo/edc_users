from ms.db import db


permission_role_table = db.Table(
    "role_has_permissions", db.Model.metadata, db.Column(
        'role_id', db.ForeignKey('role.id')), db.Column(
            'permission_id', db.ForeignKey('permission.id')), )


user_permission_table = db.Table(
    "user_has_permissions", db.Model.metadata, db.Column(
        'user_id', db.ForeignKey('user.id', ondelete='CASCADE')), db.Column(
            'permission_id', db.ForeignKey('permission.id')), )


user_role_table = db.Table(
    "user_has_roles", db.Model.metadata, db.Column(
        'user_id', db.ForeignKey(
            'user.id', ondelete='CASCADE')), db.Column(
                'role_id', db.ForeignKey('role.id')), )


app_permission_table = db.Table(
    "app_has_permissions", db.Model.metadata, db.Column(
        'app_id', db.ForeignKey('app.id', ondelete='CASCADE')), db.Column(
            'permission_id', db.ForeignKey('permission.id')), )


app_role_table = db.Table(
    "app_has_roles", db.Model.metadata, db.Column(
        'app_id', db.ForeignKey(
            'app.id', ondelete='CASCADE')), db.Column(
                'role_id', db.ForeignKey('role.id')), )
