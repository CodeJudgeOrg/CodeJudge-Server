from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.postgresql_server_db import SessionLocal
from database import crud
from schemas.submission_schemas import SubmissionUpload, SubmissionUploadRespone
from schemas.exercise_schemas import ExerciseReceiveRespond

router = APIRouter(prefix="/student", tags=["student"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------------------------------
# Exercises
# ----------------------------------------------------
@router.get("/retrieveExercises", response_model = list[ExerciseReceiveRespond])
def receiveExercises(db: Session = Depends(get_db)):
    return crud.receiveExercises(db)

# ----------------------------------------------------
# Submission
# ----------------------------------------------------
@router.post("/uploadSubmission", response_model=SubmissionUploadRespone)
def uploadExercise(submission: SubmissionUpload, db: Session = Depends(get_db)):
    return crud.insertSubmission(
        db = db,
        exerciseName = submission.exerciseName,
        task = submission.task,
        code = submission.code,
        output = submission.output,
        studentName = submission.studentName
    )
