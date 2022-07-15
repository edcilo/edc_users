from random import randint
from faker import Faker
from flask_seeder import Seeder
from ms.models import Role, User


class UsersSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 20

    def run(self):
        faker = Faker()

        adminRole = Role.query.filter_by(name="root").first()
        clientRole = Role.query.filter_by(name="client").first()
        merchantAdminRole = Role.query.filter_by(name="merchant_admin").first()
        merchantRole = Role.query.filter_by(name="merchant").first()

        users = (
            {
                "name": "root",
                "email": "root@example.com",
                "phone": "0000000000",
                "role": adminRole,
            },
            {
                "name": "merchant_admin",
                "email": "merchant_admin@example.com",
                "phone": "0000000001",
                "role": merchantAdminRole
            },
            {
                "name": "merchant_single",
                "email": "merchant_single@example.com",
                "phone": "0000000002",
                "role": merchantRole,
            },
            {
                "name": "client",
                "email": "client@example.com",
                "phone": "9999999999",
                "role": clientRole,
            }
        )

        for user in users:
            exists = User.query.filter_by(email=user.get("email")).count()
            if not exists:
                model = User(user)
                model.is_active = True
                model.set_password('secret')
                model.roles.append(user.get("role"))
                self.db.session.add(model)

        for _ in range(5):
            client = User({
                "phone": faker.unique.msisdn(),
                "email": faker.unique.email(),
                "name": faker.first_name(),
                "lastname": faker.last_name(),
                "mothername": faker.last_name(),
            })
            client.is_active = True if randint(0, 1) else False
            client.set_password("secret")
            client.roles.append(clientRole)
            self.db.session.add(client)
