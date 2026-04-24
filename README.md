# Flask-SQLAlchemy-Workout-Application-Backend
# Project Description #


A robust REST API backend for a workout tracking application used by personal trainers. 
This API allows trainers to create and manage workouts and exercises, with the ability to add multiple exercises to each workout (including sets, reps, or duration). 
The system features reusable exercises that can be added to various workouts, comprehensive data validation at multiple levels, and full CRUD operations for core resources.

Built with:
Flask, 
SQLAlchemy,
and Marshmallow, 
this application demonstrates professional backend architecture including model relationships, database constraints, validation layers, and RESTful endpoint design.

# Technologies Used #

Python 3.8.13+
Flask 2.2.2

Flask-SQLAlchemy 3.0.3

Flask-Migrate 3.1.0

Marshmallow 3.20.1

SQLite (development) / PostgreSQL (production)

Pipenv for dependency management

 # Features
 
Create, view, and delete workouts

Create, view, and delete exercises

Add exercises to workouts (many-to-many relationship)

Three layers of validation:

Database table constraints (UNIQUE, CHECK constraints)

SQLAlchemy model validations

Marshmallow schema validations

RESTful API endpoints following conventions

Seed data for testing and demonstration

Proper serialization/deserialization with Marshmallow

# Installation Instructions

Prerequisites
Python 3.8.13 or higher

Pipenv (install with pip install pipenv)

Git

Step 1: Clone the Repository
`` bash ``
git clone <your-repository-url>
cd Flask-SQLAlchemy-Workout-Application-Backend

Step 2: Install Dependencies
Using Pipenv (recommended):

`` bash``
pipenv install
pipenv shell


Or using pip with requirements.txt:

`` bash``
pip install -r requirements.txt



Step 3: Initialize the Database
`` bash``

# Initialize migrations folder (first time only)
flask db init

# Create migration script
flask db migrate -m "Initial migration"

# Apply migrations to database
flask db upgrade

Step 4: Seed the Database with Sample Data
``bash``
python seed.py
This will populate your database with sample workouts, exercises, and relationships for testing.

# Run Instructions
Development Server
`` bash ``
flask run
The server will start at http://127.0.0.1:5000

Alternative Method
`` bash ``
python app.py
Production (using gunicorn)

`` bash ``
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
API Endpoints
The API base URL is /api

# Workout Endpoints
Method	Endpoint	Description	Request Body Example
GET	/workouts	Retrieve all workouts	-
GET	/workouts/<id>	Retrieve a specific workout by ID	-
POST	/workouts	Create a new workout	{"name": "Morning Routine", "duration_minutes": 45, "difficulty": "Intermediate"}
DELETE	/workouts/<id>	Delete a workout	-
POST	/workouts/<workout_id>/exercises/<exercise_id>	Add an exercise to a workout (with sets/reps/duration)	{"sets": 3, "reps": 12} or {"duration_seconds": 60}
Exercise Endpoints
Method	Endpoint	Description	Request Body Example
GET	/exercises	Retrieve all exercises	-
GET	/exercises/<id>	Retrieve a specific exercise by ID	-
POST	/exercises	Create a new exercise	{"name": "Push Up", "muscle_group": "Chest", "calories_per_minute": 7.5}
DELETE	/exercises/<id>	Delete an exercise	-
Sample API Responses
GET /api/workouts - Returns all workouts with their associated exercises:

json
{
  "workouts": [
    {
      "id": 1,
      "name": "Upper Body Strength",
      "duration_minutes": 45,
      "difficulty": "Intermediate",
      "created_at": "2024-01-15T10:30:00",
      "exercises": [
        {
          "id": 1,
          "name": "Push Up",
          "muscle_group": "Chest",
          "sets": 3,
          "reps": 12
        }
      ]
    }
  ]
}
POST /api/workouts - Create a new workout:

json
// Request
{
  "name": "Leg Day",
  "duration_minutes": 60,
  "difficulty": "Advanced"
}

// Response (201 Created)
{
  "id": 4,
  "name": "Leg Day",
  "duration_minutes": 60,
  "difficulty": "Advanced",
  "created_at": "2024-01-20T14:15:00"
}

# Validation Rules
The API enforces the following validations:

Database Constraints
Workout names must be unique

Exercise names must be unique

Difficulty levels limited to: Beginner, Intermediate, Advanced

Duration must be positive (CHECK constraint)

Model Validations
Workout name cannot be empty or contain only whitespace

Duration minutes must be between 1 and 300

Exercise name must be at least 3 characters

Calories per minute must be positive

Schema Validations
Required fields validation (name, duration, etc.)

Data type validation

Custom validators for difficulty levels and muscle groups

Testing
Run the test suite (if implemented):

``bash``
pytest tests/

Or test individual endpoints using the Flask shell:

``bash``
flask shell
>>> from app.models import Workout, Exercise
>>> Workout.query.all()
>>> Exercise.query.filter_by(muscle_group="Chest").all()
Troubleshooting
Common Issues
Issue: ModuleNotFoundError: No module named 'flask'

Solution: Run pipenv install or pip install -r requirements.txt

Issue: Database not found or tables missing

Solution: Run flask db upgrade followed by python seed.py

Issue: Port 5000 already in use

Solution: Use a different port: flask run --port=5001

Issue: Validation errors when creating/updating data

Solution: Check the error response for specific validation messages

# Development Notes
This application uses a many-to-many relationship between workouts and exercises

No update endpoints are implemented per project requirements

Exercises can be reused across multiple workouts

Each workout-exercise association can include custom sets, reps, or duration

# Future Enhancements
User authentication and authorization

Workout completion tracking

Progress statistics and analytics

Exercise video/image uploads

Mobile app integration


# Contributors #
SANDRA NAFULA

# Acknowledgments
Flask and SQLAlchemy documentation

Course instructors and curriculum designers

Repository Structure:

Flask-SQLAlchemy-Workout-Application-Backend/
├── server/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
├── migrations/
├── seed.py
├── config.py
├── app.py
├── requirements.txt
├── Pipfile
└── README.md

## API Endpoints

- `GET /api/users` - Retrieve all users
- `POST /api/users` - Create a new user
- `GET /api/workouts` - Retrieve workouts
- `POST /api/workouts` - Create a new workout
- `GET /api/exercises` - Retrieve exercises

## License

Apache 2.0
