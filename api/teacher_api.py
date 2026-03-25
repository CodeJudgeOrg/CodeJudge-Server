from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgresql_server_db import SessionLocal
from database import crud
from schemas.exercise_schemas import ExerciseCreate, ExerciseRespone

router = APIRouter(prefix="/teacher", tags=["teacher"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/uploadExercise", response_model=ExerciseRespone)
def uploadExercise(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    return crud.createExercise(
        db = db,
        name = exercise.name,
        description = exercise.description,
        exercise = exercise.task,
        solution = exercise.solution,
        hint = exercise.hint,
        difficulty = exercise.difficulty,
    )
