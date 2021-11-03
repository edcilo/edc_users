from typing import Union
import jwt
from ms import app
from ms.helpers import time


class JwtHelper():
    def __init__(self, algorithms: Union[str, None] = None,
                 token_lifetime: Union[int, None] = None,
                 refresh_token_lifetime: Union[int, None] = None,
                 token_type: Union[str, None] = None) -> None:
        self.key = app.config.get('SECRET_KEY')
        self.algorithms = algorithms or 'HS256'
        self.token_type = token_type or 'Bearer'
        self.token_lifetime = token_lifetime or 43200
        self.refresh_token_lifetime = refresh_token_lifetime or 86400

    def encode(self, payload: dict, lifetime: int) -> str:
        payload['exp'] = time.epoch_now() + lifetime
        encoded = jwt.encode(payload, self.key, algorithm=self.algorithms)
        return encoded

    def decode(self, token: str) -> dict:
        token = token.replace(self.token_type, '').strip()
        payload = jwt.decode(token, self.key, algorithms=self.algorithms)
        return payload

    def get_tokens(self, payload: dict) -> dict[str, str]:
        token = self.encode(payload, self.token_lifetime)
        refresh_token = self.encode(payload, self.refresh_token_lifetime)
        return {
            'token': token,
            'refresh_token': refresh_token,
        }

    def check(self, token: str) -> bool:
        try:
            payload = self.decode(token)
            return time.epoch_now() <= payload['exp']
        except (jwt.InvalidSignatureError,
                jwt.DecodeError,
                jwt.ExpiredSignatureError,
                KeyError):
            return False


jwtHelper = JwtHelper()
