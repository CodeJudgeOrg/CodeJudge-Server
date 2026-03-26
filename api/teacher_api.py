from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgresql_server_db import SessionLocal
from database import crud
from schemas.exercise_schemas import ExerciseCreate, ExerciseCreateRespone

router = APIRouter(prefix="/teacher", tags=["teacher"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/uploadExercises", response_model=list[ExerciseCreateRespone])
def uploadExercise(exercises: list[ExerciseCreate], db: Session = Depends(get_db)):
    return crud.insertExercises(db, exercises)
