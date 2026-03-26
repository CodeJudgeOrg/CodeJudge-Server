from sqlalchemy.orm import Session
from .tables import exercise_table, submission_table
from schemas import exercise_schemas
from schemas import submission_schemas

# ----------------------------------------------------
# Exercises
# ----------------------------------------------------
# Insert a new exercise
def insertExercises(db: Session, exercises: list[exercise_schemas.ExerciseCreate]):
    created = []

    for exercise in exercises:
        # Extract each exercise
        obj = exercise_table.Exercises(
            name = exercise.name,
            description = exercise.description,
            task = exercise.task,
            solution = exercise.solution,
            hint = exercise.hint,
            difficulty = exercise.difficulty
        )

        # Add the exercise to the db and a list
        db.add(obj)
        created.append(obj)

    # Insert all exercises at once
    db.commit(),

    # Refresh the list and return it
    for obj in created:
        db.refresh(obj)
    return created

# Receive all exercises
def receiveExercises(db: Session):
    return db.query(exercise_table.Exercises).all()

# ----------------------------------------------------
# Submissions
# ----------------------------------------------------
# Insert a new submission
def insertSubmissions(db: Session, submissions = list[submission_schemas.SubmissionUpload]):
    created = []

    for submission in submissions:
        # Extract each submission
        obj = exercise_table.Exercises(
            name = submission.name,
            description = submission.description,
            task = submission.task,
            solution = submission.solution,
            hint = submission.hint,
            difficulty = submission.difficulty
        )

        # Add the submission to the db and a list
        db.add(obj)
        created.append(obj)

    # Insert all exercises at once
    db.commit(),

    # Refresh the list and return it
    for obj in created:
        db.refresh(obj)
    return created

# Receive all submissions
def receiveSubmissions(db: Session):
    return db.query(submission_table.SubmissionTable).all()
