import abc
from typing import Type
from flask_sqlalchemy import Model
from flaskFormRequest import FormRequest
from ms.db import db


class Repository(abc.ABC):
    def __init__(self) -> None:
        self._model = self.get_model()

    @abc.abstractmethod
    def get_model(self) -> Model:
        pass

    def form_to_dict(self, form: Type[FormRequest], cols: tuple) -> dict:
        return {c: form.get(c, None) for c in cols}

    def db_save(self, model: Model) -> None:
        db.session.add(model)
        db.session.commit()

    def db_delete(self, model: Model) -> None:
        db.session.delete(model)
        db.session.commit()
