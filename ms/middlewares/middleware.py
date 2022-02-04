from flask import request
from abc import ABC, abstractmethod
from functools import wraps


class MiddlewareBase(ABC):
    @abstractmethod
    def handler(self, request) -> None:
        pass


def middleware(middleware):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            middleware.handler(request)

            return f(*args, **kwargs)
        return wrapper
    return decorator
