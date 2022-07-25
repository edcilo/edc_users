from flask import jsonify
from flaskFormRequest.decorators import form_validator
from ms.forms import (
    AppListForm,
    AppCreateForm,
    AppUpdateForm)
from ms.repositories import AppRepository
from ms.serializers import AppSerializer
from .controller import Controller


class AppController(Controller):
    def __init__(self):
        self.appRepo = AppRepository()

    @form_validator(AppListForm)
    def list(self, form):
        collection = self.appRepo.all(**{
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = AppSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AppCreateForm)
    def create(self, form):
        app = self.appRepo.add(form.data)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 201

    def detail(self, id):
        app = self.appRepo.find(id)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 200

    @form_validator(AppUpdateForm)
    def update(self, id, form):
        app = self.appRepo.update(id, form.data)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 200

    def delete(self, id):
        self.appRepo.delete(id)
        return jsonify(None), 204
