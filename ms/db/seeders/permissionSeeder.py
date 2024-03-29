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
            Permission({"name": "Shopper - create", "fixed": True}),
            Permission({"name": "Shopper - update", "fixed": True}),
            Permission({"name": "Shopper - upload files", "fixed": True}),
            Permission({"name": "App - create", "fixed": True}),
            Permission({"name": "App - list", "fixed": True}),
            Permission({"name": "App - detail", "fixed": True}),
            Permission({"name": "App - generate token", "fixed": True}),
            Permission({"name": "App - update", "fixed": True}),
            Permission({"name": "App - permissions", "fixed": True}),
            Permission({"name": "App - roles", "fixed": True}),
            Permission({"name": "App - delete", "fixed": True}),

            # Feature flags
            Permission({"name": "Feature Flags - service - create", "fixed": True}),
            Permission({"name": "Feature Flags - service - list", "fixed": True}),
            Permission({"name": "Feature Flags - service - detail", "fixed": True}),
            Permission({"name": "Feature Flags - service - update", "fixed": True}),
            Permission({"name": "Feature Flags - service - delete", "fixed": True}),
            Permission({"name": "Feature Flags - feature - create", "fixed": True}),
            Permission({"name": "Feature Flags - feature - list", "fixed": True}),
            Permission({"name": "Feature Flags - feature - detail", "fixed": True}),
            Permission({"name": "Feature Flags - feature - update", "fixed": True}),
            Permission({"name": "Feature Flags - feature - update status", "fixed": True}),
            Permission({"name": "Feature Flags - feature - delete", "fixed": True}),

            # Analytics
            Permission({"name": "Analytics - event - create", "fixed": True}),
            Permission({"name": "Analytics - counters - list", "fixed": True}),
        )

        for _ in permissions:
            permission = Permission.query.filter_by(name=_.name).first()
            if permission is None:
                self.db.session.add(_)
