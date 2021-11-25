import functools
from flask import jsonify, request


def form_validator(FormClass, method=None):
    def form_validator_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = request.args.to_dict() if method == 'GET' else request.form
            form = FormClass(data=data, request=request)
            if not form.validate():
                return jsonify({'errors': form.errors}), 400
            kwargs['form'] = form
            return func(*args, **kwargs)
        return wrapper
    return form_validator_decorator
