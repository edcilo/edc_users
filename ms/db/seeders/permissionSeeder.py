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
            Permission({"name": "Client - create", "fixed": True}),
            Permission({"name": "Client - update", "fixed": True}),
        )

        for _ in permissions:
            permission = Permission.query.filter_by(name=_.name).first()
            if permission is None:
                self.db.session.add(_)
