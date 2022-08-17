from flask import jsonify
from flaskFormRequest.decorators import form_validator
from ms.repositories import ShopperRepository
from ms.serializers import UserProfileSerializer
from ms.services import rfc, curp
from ms.forms import (
    ShopperCreateForm,
    ShopperUpdateForm,
    ShopperUpdloaFilesForm)
from .controller import Controller


class ShopperController(Controller):
    def __init__(self) -> None:
        self.shopperRepo = ShopperRepository()

    @form_validator(ShopperCreateForm)
    def create(self, form):
        data = form.data
        data['rfc'] = rfc.generate(data)
        data['curp'] = curp.generate(data)
        user = self.shopperRepo.add(data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 201

    @form_validator(ShopperUpdateForm)
    def update(self, id, form):
        user = self.shopperRepo.update(id, form.data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(ShopperUpdloaFilesForm)
    def upload_id_files(self, id, form):
        self.shopperRepo.upload_files(id, form.data)
        return jsonify(None), 204
