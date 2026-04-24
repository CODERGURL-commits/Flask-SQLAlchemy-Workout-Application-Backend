# Workout Tracker API

A professional backend API built with Flask, SQLAlchemy, and Marshmallow. 
This application allows personal trainers to manage workouts and reusable exercises. It demonstrates advanced database relationships, multi-layer data validation, and automated serialization.

# Features
## Relational Database: 
Many-to-Many relationship between Workouts and Exercises using a WorkoutExercise association table.

## Triple-Layer Validation:Table Constraints:
nullable=False, unique=True, and CheckConstraints.

## Model Validations: 
Using SQLAlchemy @validates for business logic.

## Schema Validations:
Using Marshmallow validate for request integrity.

## RESTful Endpoints:
Clean API design for creating, viewing, and linking resources.

Seeded Data: Pre-populated database for immediate testing.

# Step-by-Step Installation 

Follow these instructions exactly to set up your development environment from scratch.

# 1. Prerequisites
 Ensure you have Python 3.8.13+ installed.
 You will also need Pipenv.
 To check Python version: ```python --version``` To install Pipenv: ```run pipenv install```
# 2. Clone the Repository 
Open your terminal and clone your project:```Bash git clone <your-github-repo-url>
cd workout-tracker-backend```

 # Install Dependencies
 Install all required packages (Flask, SQLAlchemy, Marshmallow, etc.) as specified in the Pipfile: ```Bash pipenv install <list of all dependencies required>```
 *  Activate the Virtual Environment:
```Bash pipenv shell``` for MacOS/linux
```venv\Scripts\activate```on windows

 # Initialize the Database
 Set up your SQLite database and generate the tables using Flask-Migrate: ```Bash# Initialize the migration folder
flask db init```

# Create the initial migration script
```flask db migrate -m "Initial migration"```

# Apply the migration to create 'instance/app.db'
```flask db upgrade```
# Seed the Database
 Populate the database with sample data (trainers, exercises, and workouts) so the API isn't empty: ```Bash python seed.py```
 
# Launch the API
   Start the Flask development server: ```Bash flask run```
The API will now be running at http://127.0.0.1:5000.

# API Endpoints 

Method,Endpoint,Description
GET,/workouts,Retrieve all workouts with associated exercises.
GET,/workouts/<id>,Retrieve a specific workout by ID.
POST,/workouts,"Create a new workout (requires title, trainer_id)."
DELETE,/workouts/<id>,Remove a workout.

# Workout Endpoints

Method,Endpoint,Description
GET,/exercises,List all available reusable exercises.
POST,/exercises,Create a new exercise (requires name).
DELETE,/exercises/<id>,Delete an exercise.

# Validation & Constraints
This project implements three levels of protection to ensure data integrity:

``Table Constraints``: Database-level checks like unique=True for exercise names and CheckConstraint to ensure reps/sets are greater than 0.

``Model Validations``: Using @validates in SQLAlchemy to enforce business rules (e.g., workout titles must be at least 3 characters).

``Schema Validations``: Marshmallow schemas validate incoming JSON data types and required fields before they even touch the database.

# Project Structure
``app.py``: Application entry point and API routes.

``models.py``: SQLAlchemy models and relationship definitions.

``schemas.py``: Marshmallow schemas for serialization and validation.

``seed.py``: Script to populate the database with initial data.

``Pipfile``: List of dependencies and Python version requirements.

#  Testing the API
You can test the endpoints using:

``Postman or Insomnia (Recommended for POST/DELETE).``

``cURL via the terminal.``

``SQLite Viewer (VS Code extension) to see the data inside app.db.``

## License

Apache 2.0
