from sqlalchemy import or_

from .extensions import bcrypt, db

# User Model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(255))
    weight = db.Column(db.Float)
    feet = db.Column(db.Integer)
    inches = db.Column(db.Integer)
    goals = db.Column(db.String(255))
    days_per_week = db.Column(db.Integer)
    dietary_restrictions = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Password Hashing
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def get_user_id_by_username_or_email(cls, username, email):
        user = db.session.query(cls).filter(or_(cls.username == username, cls.email == email)).first()
        return user.id if user else None

# Saved Fitness Plan Model
class SavedFitnessPlan(db.Model):
    __tablename__ = "saved_fitness_plans"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    workout_routine = db.Column(db.Text, nullable=True)
    workout_summary = db.Column(db.Text, nullable=True)
    plan_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship with User model
    user = db.relationship("User", backref=db.backref("saved_fitness_plans", lazy=True, cascade="all, delete-orphan"))

# Saved Diet Plan Model
class SavedDietPlan(db.Model):
    __tablename__ = "saved_diet_plans"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    diet_plan = db.Column(db.Text, nullable=True)
    diet_summary = db.Column(db.Text, nullable=True)
    plan_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship with User model
    user = db.relationship("User", backref=db.backref("saved_diet_plans", lazy=True, cascade="all, delete-orphan"))
