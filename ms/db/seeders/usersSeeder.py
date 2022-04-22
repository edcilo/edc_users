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

        root = User({
            "phone": "0000000000",
            "email": "root@example.com",
        })
        client = User({
            "phone": "1111111111",
            "email": "client@example.com",
        })

        user = User.query.filter_by(email=root.email).first()
        if user is None:
            root.set_password('secret')
            root.roles.append(adminRole)
            self.db.session.add(root)

        user = User.query.filter_by(email=client.email).first()
        if user is None:
            client.set_password('secret')
            client.roles.append(clientRole)
            self.db.session.add(client)

        for _ in range(5):
            client = User({
                "phone": faker.msisdn(),
                "email": faker.email(),
            })
            client.set_password("secret")
            client.roles.append(clientRole)
            self.db.session.add(client)
