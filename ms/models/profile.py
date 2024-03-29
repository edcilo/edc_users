import uuid
from ms.db import db
from ms.models.user import User


class Profile(db.Model):
    __tablename__ = 'profile'

    _fillable = (
        'rfc',
        'curp',
        'home_phone',
        'birthday',
        'gender',
        'legal_id_front',
        'legal_id_back',
        'proof_of_address',
    )

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    rfc = db.Column(db.String(13), unique=True, nullable=True)
    curp = db.Column(db.String(18), unique=True, nullable=True)
    home_phone = db.Column(db.String(15), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.String(50), nullable=True)

    legal_id_front = db.Column(db.String(255), nullable=True)
    legal_id_back = db.Column(db.String(255), nullable=True)
    proof_of_address = db.Column(db.String(255), nullable=True)

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
