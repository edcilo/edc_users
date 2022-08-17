from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    AlphaNum,
    Array,
    Between,
    Date,
    Email,
    Float,
    In,
    Integer,
    Json,
    Max,
    Min,
    Nullable,
    Regex,
    Required,
    Size,
    Unique,
)
from ms.helpers import regex
from ms.helpers.dictionaries import (
    activities, department, entities, grades, marital_status)
from ms.models import User, Profile


class ShopperCreateForm(FormRequest):
    def rules(self):
        return {
            'email': [
                Required(),
                Max(255),
                Email(),
                Unique(User),
            ],
            'phone': [
                Required(),
                Size(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
                Unique(User),
            ],
            'password': [
                Required(),
                Max(255),
                Regex(regex.password_regex, message='The password is invalid'),
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
                Nullable(),
                Max(50),
                Regex(regex.personal_name_regex, message='The second lastname is invalid'),
            ],
            'home_phone': [
                Required(),
                Size(10),
                Regex(regex.phone_regex, message='The phone is invalid'),
            ],
            'birthday': [
                Required(),
                Date(format="%Y-%m-%d"),
            ],
            'entity_birth': [
                Required(),
                In([entity.get('id') for entity in entities.mx.entities]),
            ],
            'gender': [
                Required(),
                In(['H', 'M']),
            ],
            'grade': [
                Required(),
                Max(60),
                In(grades.grades)
            ],
            'marital_status': [
                Required(),
                Max(60),
                In(marital_status.marital_status),
            ],
            'deparment': [
                Required(),
                In(department.department),
            ],
            'street': [
                Required(),
                Max(120),
                Regex(regex.text_with_numbers, message='The street is invalid'),
            ],
            'exterior': [
                Required(),
                Max(10),
                Regex(regex.text_with_numbers, message='The exterior number is invalid'),
            ],
            'interior': [
                Nullable(),
                Max(10),
                Regex(regex.text_with_numbers, message='The interior number is invalid'),
            ],
            'neighborhood': [
                Required(),
                Max(120),
                Regex(regex.text_with_numbers, message='The street is invalid'),
            ],
            'zip': [
                Required(),
                Size(5),
                Integer(),
            ],
            'monthly_expenditure': [
                Required(),
                Float(),
                Min(0),
            ],
            'income': [
                Required(),
                Float(),
                Min(0),
            ],
            'income_family': [
                Required(),
                Float(),
                Min(0),
            ],
            'count_home': [
                Required(),
                Size(2),
                Integer(),
            ],
            'company_name': [
                Required(),
                Max(120),
                Regex(regex.text_with_numbers, message='The street is invalid'),
            ],
            'type_activity': [
                Required(),
                Max(120),
                In(activities.activities),
            ],
            'position': [
                Required(),
                Max(120),
                Regex(regex.text_with_numbers, message='The street is invalid'),
            ],
            'time_activity_year': [
                Required(),
                Integer(),
                Between(0, 100),
            ],
            'time_activity_month': [
                Required(),
                Integer(),
                Between(0, 11)
            ],
            'personal_references': [
                Array(rules=[Json(rules={
                    "name": [
                        Required(),
                        Max(120),
                        Regex(regex.personal_name_regex, message='The name is invalid'),
                    ],
                    "phone": [
                        Required(),
                        Size(10),
                        Regex(regex.phone_regex, message='The phone is invalid'),
                    ],
                    "relationship": [
                        Required(),
                        Max(60),
                        Regex(regex.text, message='The name is invalid'),
                    ],
                })]),
                Min(1),
            ],
        }
