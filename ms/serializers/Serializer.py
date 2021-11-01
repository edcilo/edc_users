class Serializer():
    response = list()

    def __init__(self, user):
        self.model = user
        self.serialize()

    def serialize(self):
        data = {}
        for attr in self.response:
            data[attr] = getattr(self.model, attr, None)

        self.data = data
