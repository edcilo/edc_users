import datetime
import os
import requests
from ms import app
from ms.helpers import faker


class CURP:
    def __init__(self) -> None:
        self.api_url = os.getenv('CURP_API_URL')
        self.api_token = os.getenv('CURP_API_TOKEN')

    @property
    def headers(self):
        return {
            "Authorization": f"Token {self.api_token}",
        }

    def parse_response(self, response):
        if response.status_code == 200:
            response = response.json()
            return response.get('curp')
        else:
            raise Exception('Error generating CURP')
            return None

    def generate(self, name, lastname, second_lastname, birthday, entity_birth, gender):
        data = {
            "name": name,
            "last_name": lastname,
            "mother_name": second_lastname,
            "birthday": birthday,
            "entity_birth": entity_birth,
            "gender": gender,
        }

        res = requests.request(
            'POST',
            self.api_url,
            headers=self.headers,
            data=data
        )

        return self.parse_response(res)

def generate(data):
    curp = CURP()
    name = data.get('name', None)
    lastname = data.get('lastname', None)
    second_lastname = data.get('second_lastname', None)
    birthday = data.get('birthday', None)
    entity_birth = data.get('entity_birth', None)
    gender = data.get('gender', None) # M mujer, H hombre

    birthday = birthday.strftime("%Y-%m-%d") if isinstance(birthday, datetime.datetime) else birthday

    if app.config.get('ENV') == 'development':
        return faker.curp(name, lastname, second_lastname, birthday, entity_birth, gender)

    return curp.generate(name, lastname, second_lastname, birthday, entity_birth, gender)
