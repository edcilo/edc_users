from ms.db import db


class Serializer():
    original: None
    data = None
    pagination = None
    response: tuple[str] = list()
    is_collection: bool = False
    is_paginated: bool = False

    def __init__(self, model: db.Model, collection: bool = False,
                 paginate: bool = False) -> None:
        self.original = model
        self.model = model.items if paginate else model
        self.is_paginated = paginate
        self.is_collection = collection or paginate

    def get_data(self):
        self.handler()
        return self.data

    def handler(self) -> None:
        data = self.handler_collection(self.model) \
            if self.is_collection else self.serialize(self.model)
        if self.is_paginated:
            pagination_data = {
                'page': self.original.page,
                'pages': self.original.pages,
                'per_page': self.original.per_page,
                'prev': self.original.prev_num,
                'next': self.original.next_num,
                'total': self.original.total,
            }
            data = {'data': data, 'pagination': pagination_data}
        self.data = data

    def handler_collection(self, collection) -> None:
        res = list()
        for model in collection:
            data = self.serialize(model)
            res.append(data)
        return res

    def serialize(self, model) -> None:
        data = {}
        for attr in self.response:
            data[attr] = getattr(model, attr, None)
        return data
