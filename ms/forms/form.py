import abc
from flask_wtf import FlaskForm
from flask import Request


def strip_filter(value):
    if value is not None and hasattr(value, 'strip'):
        return value.strip()
    return value


class BaseForm(FlaskForm):
    class Meta:
        def bind_field(self, form, unbound_field, options):
            filters = unbound_field.kwargs.get('filters', [])
            filters.append(strip_filter)
            return unbound_field.bind(form=form, filters=filters, **options)


class FormRequest():
    def __init__(self, data: dict, request: Request) -> None:
        self.request_data = data
        self.request = request
        self.attrs = list()
        self.form = self.initialize()

    @property
    def errors(self):
        return None if self.form is None else self.form.errors

    @property
    def data(self):
        data = dict()
        for attr in self.attrs:
            data[attr] = getattr(self.form, attr).data
        return data

    def initialize(self):
        class Form(BaseForm):
            pass

        rules = self.rules(self.request)

        for attr, rule in rules.items():
            setattr(Form, attr, rule)
            self.attrs.append(attr)

        return Form(data=self.request_data, meta={'csrf': False})

    def validate(self):
        return self.form.validate()

    @abc.abstractmethod
    def rules(self, request) -> dict:
        pass
