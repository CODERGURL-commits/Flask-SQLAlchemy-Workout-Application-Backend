from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship(
        'WorkoutExercise', backref='exercise', cascade="all, delete-orphan")

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name is required")
        return value


class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    __table_args__ = (CheckConstraint('duration_minutes > 0',
                      name='check_duration_positive'),)

    workout_exercises = db.relationship(
        'WorkoutExercise', backref='workout', cascade="all, delete-orphan")


class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey(
        'workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey(
        'exercises.id'), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    @validates('reps', 'sets')
    def validate_metrics(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be positive")
        return value
