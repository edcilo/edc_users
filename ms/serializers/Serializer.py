from ms.models import User


class Serializer():
    response: tuple[str] = list()

    def __init__(self, user: User) -> None:
        self.model = user
        self.serialize()

    def serialize(self) -> None:
        data = {}
        for attr in self.response:
            data[attr] = getattr(self.model, attr, None)

        self.data = data
