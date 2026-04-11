# Flask-SQLAlchemy-Workout-Application-Backend
## Overview

A backend REST API for a workout application built with Flask and SQLAlchemy. This project provides endpoints for managing users, workouts, exercises, and training progress.

## Features

- User authentication and management
- Workout planning and tracking
- Exercise database with detailed information
- Progress monitoring and statistics
- SQLAlchemy ORM for database operations

## Tech Stack

- **Framework**: Flask
- **Database ORM**: SQLAlchemy
- **Database**: SQLite/PostgreSQL
- **Language**: Python

## Installation

```bash
git clone <repository-url>
cd Flask-SQLAlchemy-Workout-Application-Backend
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## API Endpoints

- `GET /api/users` - Retrieve all users
- `POST /api/users` - Create a new user
- `GET /api/workouts` - Retrieve workouts
- `POST /api/workouts` - Create a new workout
- `GET /api/exercises` - Retrieve exercises

## License

Apache 2.0
