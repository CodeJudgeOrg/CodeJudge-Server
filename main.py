from fastapi import FastAPI
from database.postgresql_server_db import engine, Base
from database.tables.exercise_table import Exercises
from database.tables.submission_table import SubmissionTable
from api.teacher_api import router as teacher_router
from api.student_api import router as student_router

# Start the server
app = FastAPI()

# End point to test the server
@app.get("/health")
def health():
    return {"status": "ok"}

# Include the routers
app.include_router(teacher_router)
app.include_router(student_router)

# Generate the tables of the db
Base.metadata.create_all(bind = engine)