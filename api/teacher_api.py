from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgresql_server_db import SessionLocal
from database import crud
from schemas.exercise_schemas import ExerciseCreate, ExerciseCreateRespone
from schemas.submission_schemas import SubmissionReceiveResponse

router = APIRouter(prefix="/teacher", tags=["teacher"])

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------------------------------
# Exercises
# ----------------------------------------------------
@router.post("/uploadExercises", response_model=list[ExerciseCreateRespone])
def uploadExercise(exercises: list[ExerciseCreate], db: Session = Depends(getDB)):
    return crud.insertExercises(db, exercises)

# ----------------------------------------------------
# Submission
# ----------------------------------------------------
@router.get("/receiveSubmissions", response_model = list[SubmissionReceiveResponse])
def receiveSubmissions(db: Session = Depends(getDB)):
    return crud.receiveSubmissions(db)

# TODO: Teacher should be able to edit an exercise, to delete exercises, to quit the session, etc.