import datetime
import os
import requests
from slugify import slugify
from ms import app
from ms.helpers import faker


class RFC:
    def __init__(self) -> None:
        self.api_url = os.getenv('RFC_API_URL')
        self.api_host = os.getenv('RFC_API_HOST')
        self.api_key = os.getenv('RFC_API_KEY')
        self.homoclave = 0

    @property
    def headers(self):
        return {
            "x-rapidapi-host": self.api_host,
            "x-rapidapi-key": self.api_key,
            "User-Agent": 'graviti-request/1.0.0'
        }

    def parse_response(self, rsponse):
        if rsponse.status_code == 200:
            response = rsponse.json()
            return response['response']['data']['rfc']
        else:
            raise Exception('Error generating RFC')
            return None

    def generate(self, name, lastname, second_lastname, birthday):
        data = {
            'solo_homoclave': self.homoclave,
            'nombre': slugify(name),
            'apellido_paterno': slugify(lastname),
            'apellido_materno': slugify(second_lastname),
            'fecha': birthday,
        }

        res = requests.request(
            'GET',
            self.api_url,
            headers=self.headers,
            params=data
        )

        return self.parse_response(res)


def generate(data):
    rfc = RFC()
    name = data.get('name', None)
    lastname = data.get('lastname', None)
    second_lastname = data.get('second_lastname', None)
    birthday = data.get('birthday', None)

    birthday = birthday.strftime("%Y-%m-%d") if isinstance(birthday, datetime.datetime) else birthday

    if app.config.get('ENV') == 'development':
        return faker.rfc(name, lastname, second_lastname, birthday)

    return rfc.generate(name, lastname, second_lastname, birthday)
