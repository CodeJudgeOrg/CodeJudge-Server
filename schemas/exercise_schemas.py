from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    description: str
    task: str
    solution: str
    hint: str
    difficulty: int

class ExerciseRespone(ExerciseCreate):
    id: int

    class Config:
        orm_mode = True