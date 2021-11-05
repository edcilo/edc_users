from flask_wtf import FlaskForm


class Repository():
    model = None

    def __init__(self, model) -> None:
        self.model = model

    def form_to_dict(self, form: FlaskForm, cols: tuple) -> dict:
        return {c: getattr(form, c).data for c in cols}
