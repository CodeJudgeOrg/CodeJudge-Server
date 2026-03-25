from fastapi import FastAPI
from database.postgresql_server_db import engine, Base
from database.tables.exercise_table import Exercises
from api.teacher_api import router as teacher_router

# Start the server
app = FastAPI()

# End point to test the server
@app.get("/health")
def health():
    return {"status": "ok"}

# Include the routers
app.include_router(teacher_router)

# Generate the tables of the db
Base.metadata.create_all(bind=engine)