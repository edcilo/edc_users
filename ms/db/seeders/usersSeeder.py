from random import randint
from faker import Faker
from flask_seeder import Seeder
from ms.models import Role, User


class UsersSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 30

    def run(self):
        faker = Faker()

        adminRole = Role.query.filter_by(name="root").first()
        userRole = Role.query.filter_by(name="user").first()

        users = (
            {
                "id": "accd5294-aab2-4b61-96b5-fd7f39ee6de1",
                "name": "root",
                "email": "root@example.com",
                "phone": "0000000000",
                "role": adminRole,
            },
            {
                "id": "4bd7a357-0670-4aa9-a261-6234b774f7fe",
                "name": "user",
                "email": "user@example.com",
                "phone": "9999999999",
                "role": userRole,
            },
        )

        for user in users:
            exists = User.query.filter_by(email=user.get("email")).count()
            if not exists:
                model = User(user)
                model.id = user.get("id")
                model.is_active = True
                model.set_password('secret')
                model.roles.append(user.get("role"))
                self.db.session.add(model)

        for _ in range(50):
            user = User({
                "phone": faker.unique.msisdn(),
                "email": faker.unique.email(),
                "name": faker.first_name(),
                "lastname": faker.last_name(),
                "second_lastname": faker.last_name(),
            })
            user.is_active = True if randint(0, 1) else False
            user.set_password("secret")
            user.roles.append(userRole)
            self.db.session.add(user)
