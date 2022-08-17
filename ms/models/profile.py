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
        'entity_birth',
        'gender',
        'grade',
        'marital_status',
        'department',
        'street',
        'exterior',
        'interior',
        'neighborhood',
        'zip',
        'monthly_expenditure',
        'income',
        'income_family',
        'count_home',
        'company_name',
        'type_activity',
        'position',
        'time_activity_year',
        'time_activity_month',
        'personal_references',
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
    entity_birth = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(50), nullable=True) # H -> Hombre, M -> Mujer
    grade = db.Column(db.String(60), nullable=True)
    marital_status = db.Column(db.String(60), nullable=True)
    department = db.Column(db.String(60), nullable=True)
    street = db.Column(db.String(255), nullable=True)
    exterior = db.Column(db.String(6), nullable=True)
    interior = db.Column(db.String(6), nullable=True)
    neighborhood = db.Column(db.String(255), nullable=True)
    zip = db.Column(db.String(5), nullable=True)
    monthly_expenditure = db.Column(db.Float, nullable=True)
    income = db.Column(db.Float, nullable=True)
    income_family = db.Column(db.Float, nullable=True)
    count_home = db.Column(db.Integer, nullable=True)
    company_name = db.Column(db.String(255), nullable=True)
    type_activity = db.Column(db.String(255), nullable=True)
    position = db.Column(db.String(255), nullable=True)
    time_activity_year = db.Column(db.Integer, nullable=True)
    time_activity_month = db.Column(db.Integer, nullable=True)
    personal_references = db.Column(db.JSON, nullable=True)

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
