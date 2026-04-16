from pydantic import BaseModel

# Schemas when uploading exercises
class SubmissionUpload(BaseModel):
    exerciseName: str
    task: str
    code: str
    output: str
    studentName: str

# Schemas when receiving exercises
class SubmissionReceiveResponse(BaseModel):
    id: int
    exerciseName: str
    task: str
    code: str
    output: str
    studentName: str

    class Config:
        orm_mode: True