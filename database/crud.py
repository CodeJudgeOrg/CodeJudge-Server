from sqlalchemy.orm import Session
from .tables import exercise_table, submission_table

def createExercise(db: Session, name: str, description: str, exercise: str, solution: str, hint: str, difficulty: int):
    exercise = exercise_table.Exercises(
        name = name,
        description = description,
        task = exercise,
        solution = solution,
        hint = hint,
        difficulty = difficulty,
    )
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

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
