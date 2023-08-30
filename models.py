# models.py
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    feet = db.Column(db.Integer)
    inches = db.Column(db.Integer)
    goals = db.Column(db.String(255))
    days_per_week = db.Column(db.Integer)
    dietary_restrictions = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Methods to handle hashtagging
    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

# Saved Plans Model
# models.py

class SavedPlan(db.Model):
    __tablename__ = "saved_plans"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    plan = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship with User model
    user = db.relationship("User", backref=db.backref("saved_plans", lazy=True))
