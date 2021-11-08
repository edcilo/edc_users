import functools
from flask import jsonify, request


def form_validator(formClass, method=None):
    def form_validator_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = request.args.to_dict() if method == 'GET' else request.form
            form = formClass(data=data)
            if not form.validate():
                return jsonify({'errors': form.errors}), 400
            kwargs['form'] = form
            return func(*args, **kwargs)
        return wrapper
    return form_validator_decorator
