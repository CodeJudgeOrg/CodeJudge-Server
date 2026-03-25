from sqlalchemy.orm import Session
from .tables import exercise_table

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