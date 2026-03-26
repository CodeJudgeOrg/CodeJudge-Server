from sqlalchemy.orm import Session
from .tables import exercise_table, submission_table
from schemas import exercise_schemas

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
def insertSubmission(db: Session, exerciseName: str, task: str, code: str, output: str, studentName: str):
    # Create an object of a submission
    submission = submission_table.SubmissionTable(
        exerciseName = exerciseName,
        task = task,
        code = code,
        output= output,
        studentName = studentName,
    )
    # Insert the object to the db
    db.add(submission)
    db.commit()
    db.refresh(submission)

    # Return the object
    return submission

# Receive all submissions
def receiveSubmissions(db: Session):
    return db.query(submission_table.SubmissionTable).all()
