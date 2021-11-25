from typing import Type, Any
from ms.db import db


class Serializer:
    response: dict[str, Type] = dict()

    def __init__(self, model: db.Model, collection: bool = False,
                 paginate: bool = False) -> None:
        self.__data = None
        self.__original = model
        self.__model = model.items if paginate else model
        self.__is_paginated = paginate
        self.__is_collection = collection or paginate

    def get_data(self):
        self.handler()
        return self.__data

    def handler(self) -> None:
        data = self.handler_collection(self.__model) \
            if self.__is_collection else self.serialize(self.__model)
        if self.__is_paginated:
            pagination_data = {
                'page': self.__original.page,
                'pages': self.__original.pages,
                'per_page': self.__original.per_page,
                'prev': self.__original.prev_num,
                'next': self.__original.next_num,
                'total': self.__original.total,
            }
            data = {'data': data, 'pagination': pagination_data}
        self.__data = data

    def handler_collection(self, collection) -> list[dict]:
        res = list()
        for model in collection:
            data = self.serialize(model)
            res.append(data)
        return res

    def serialize(self, model) -> dict[str, Any]:
        data = {}
        for attr, type in self.response.items():
            data[attr] = type(getattr(model, attr, None))
        return data
