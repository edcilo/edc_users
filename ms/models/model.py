from flask_sqlalchemy import Model as BaseModel


class Model(BaseModel):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
