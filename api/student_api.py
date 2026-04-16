from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgresql_server_db import SessionLocal
from database import crud
from schemas.submission_schemas import SubmissionUpload
from schemas.exercise_schemas import ExerciseReceiveRespond

router = APIRouter(prefix="/student", tags=["student"])

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------------------------------
# Exercises
# ----------------------------------------------------
@router.get("/retrieveExercises", response_model = list[ExerciseReceiveRespond])
def receiveExercises(db: Session = Depends(getDB)):
    return crud.receiveExercises(db)

# ----------------------------------------------------
# Submission
# ----------------------------------------------------
@router.post("/uploadSubmissions")
def uploadExercise(submissions: list[SubmissionUpload], db: Session = Depends(getDB)):
    return crud.insertSubmissions(db, submissions)

