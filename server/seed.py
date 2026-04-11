#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():
    print("Deleting existing data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()
    
    print("Seeding exercises...")
    exercise1 = Exercise(name="Push-ups", category="Chest", equipment_needed=False)
    exercise2 = Exercise(name="Squats", category="Legs", equipment_needed=False)
    exercise3 = Exercise(name="Bicep Curls", category="Arms", equipment_needed=True)
    db.session.add_all([exercise1, exercise2, exercise3])
    db.session.commit()
    
    print("Seeding workouts...")
    workout1 = Workout(date=date(2026, 4, 11), duration_minutes=45, notes="Uper body day")
    workout2 = Workout(date=date(2026, 4, 12), duration_minutes=30, notes="Lower body day")
    db.session.add_all([workout1, workout2])
    db.session.commit()
    
    print("Seeding workout exercises...")
    we1 = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise1.id, reps=15, sets=3)
    we2 = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise3.id, reps=12, sets=3)
    we3 = WorkoutExercise(workout_id=workout2.id, exercise_id=exercise2.id, reps=20, sets=4)
    db.session.add_all([we1,we2, we3])
    db.session.commit()
    
    print("Seeding complete!")