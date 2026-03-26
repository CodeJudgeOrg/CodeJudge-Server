from pydantic import BaseModel

class SubmissionUpload(BaseModel):
    exerciseName: str
    task: str
    code: str
    output: str
    studentName: str

class SubmissionUploadRespone(SubmissionUpload):
    id: int

    class Config:
        orm_mode = True
