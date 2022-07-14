from flask import jsonify
from flaskFormRequest.decorators import form_validator
from ms.repositories import ClientRepository
from ms.serializers import UserProfileSerializer
from ms.forms import ClientCreateForm, ClientUpdateForm
from .controller import Controller


class ClientController(Controller):
    def __init__(self) -> None:
        self.clientRepo = ClientRepository()

    @form_validator(ClientCreateForm)
    def create(self, form):
        user = self.clientRepo.add(form.data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 201

    @form_validator(ClientUpdateForm)
    def update(self, id, form):
        user = self.clientRepo.update(id, form.data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200
