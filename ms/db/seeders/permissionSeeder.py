from faker import Faker
from flask_seeder import Seeder, generator
from ms.models import Permission


class PermissionSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        faker = Faker()

        permissions = (
            Permission({"name": "Role - list", "fixed": True}),
            Permission({"name": "Role - detail", "fixed": True}),
            Permission({"name": "Permission - list", "fixed": True}),
            Permission({"name": "Permission - detail", "fixed": True}),
            Permission({"name": "User - create", "fixed": True}),
            Permission({"name": "User - list", "fixed": True}),
            Permission({"name": "User - detail", "fixed": True}),
            Permission({"name": "User - update", "fixed": True}),
            Permission({"name": "User - update password", "fixed": True}),
            Permission({"name": "User - permissions", "fixed": True}),
            Permission({"name": "User - roles", "fixed": True}),
            Permission({"name": "User - activate", "fixed": True}),
            Permission({"name": "User - soft delete", "fixed": True}),
            Permission({"name": "User - restore", "fixed": True}),
            Permission({"name": "User - delete", "fixed": True}),
            Permission({"name": "App - create", "fixed": True}),
            Permission({"name": "App - list", "fixed": True}),
            Permission({"name": "App - detail", "fixed": True}),
            Permission({"name": "App - generate token", "fixed": True}),
            Permission({"name": "App - update", "fixed": True}),
            Permission({"name": "App - permissions", "fixed": True}),
            Permission({"name": "App - roles", "fixed": True}),
            Permission({"name": "App - delete", "fixed": True}),
        )

        for _ in permissions:
            permission = Permission.query.filter_by(name=_.name).first()
            if permission is None:
                self.db.session.add(_)
