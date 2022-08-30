import uuid
from ms.db import db
from ms.models.user import User


class Profile(db.Model):
    __tablename__ = 'profile'

    _fillable = (
        'birthday',
        'gender',
    )

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    birthday = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.String(50), nullable=True)  # M -> Male, F -> Female

    user_id = db.Column(
        db.String(36),
        db.ForeignKey(User.id, ondelete='CASCADE'),
        nullable=False)

    user = db.relationship("User", back_populates="profile")

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<Profile {self.id}>"
