from faker import Faker
from flask_seeder import Seeder, generator
from ms.models import Role


class RoleSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 20

    def run(self):
        faker = Faker()

        roles = (
            Role({"name": "root", "fixed": True}),
            Role({"name": "client", "fixed": True}),
            Role({"name": "user", "fixed": True}),
            Role({"name": "merchant", "fixed": True}),
        )

        for _ in roles:
            role = Role.query.filter_by(name=_.name).first()
            if role is None:
                self.db.session.add(_)
