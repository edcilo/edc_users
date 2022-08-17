from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Date,
    Email,
    In,
    Max,
    Min,
    Nullable,
    Regex,
    Required,
    Size,
    Unique,
)
from ms.helpers import regex
from ms.models import User, Profile
from ms.repositories import UserRepository


class ShopperUpdateForm(FormRequest):
    def rules(self):
        userRepo = UserRepository()
        user_id = self.request.view_args.get('id')
        user = userRepo.find(user_id)
        profile_id = user.profile.id

        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User, except_id=user_id)
            ],
            'phone': [
                Required(),
                Min(10),
                Max(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user_id)
            ],
            'password': [
                Required(),
                Max(255),
                Regex(regex.password_regex, message='The password is invalid')
            ],
            'name': [
                Required(),
                Max(50),
                Regex(regex.personal_name_regex, message='The name is invalid'),
            ],
            'lastname': [
                Required(),
                Max(50),
                Regex(regex.personal_name_regex, message='The lastname is invalid'),
            ],
            'second_lastname': [
                Required(),
                Max(50),
                Regex(regex.personal_name_regex, message='The second lastname is invalid'),
            ],
            'rfc': [
                Required(),
                Size(13),
                Unique(Profile, except_id=profile_id)
            ],
            'curp': [
                Required(),
                Size(18),
                Unique(Profile, except_id=profile_id)
            ],
            'home_phone': [
                Nullable(),
                Min(9),
                Max(15),
                Regex(regex.phone_regex, message='The phone is invalid'),
            ],
            'birthday': [
                Nullable(),
                Date(format="%Y-%m-%d")
            ],
            'gender': [
                Nullable(),
                In(['M', 'F'])
            ],
        }
