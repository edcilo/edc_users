import functools
from flask import abort, jsonify


def form_validator(formClass):
    def form_validator_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            form = formClass()
            if not form.validate_on_submit():
                return jsonify({'errors': form.errors}), 400
            kwargs['form'] = form
            return func(*args, **kwargs)
        return wrapper
    return form_validator_decorator
