# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Teachers can sign in to manage activity registrations
- Students can view activities and registered participants

## Getting Started

1. Install the dependencies from the repository root:

   ```
   pip install -r requirements.txt
   ```

2. Create a teacher account. Passwords are prompted securely and stored as salted PBKDF2 hashes in the local, Git-ignored `teachers.json` file:

   ```
   cd src
   python create_teacher.py
   ```

3. Start the application from the repository root:

   ```
   uvicorn app:app --app-dir src --reload
   ```

4. Open http://localhost:8000. Students can view activities and participants. Only signed-in teachers can register or unregister students.

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/auth/login`                                                      | Validate teacher credentials using HTTP Basic                      |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up a student (teacher authentication required)                 |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister a student (teacher authentication required)              |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
Teacher credentials remain in the local `src/teachers.json` file and should not be committed or shared.
