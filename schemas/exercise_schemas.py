from pydantic import BaseModel

# Schemas when creating an exercise
class ExerciseCreate(BaseModel):
    name: str
    description: str
    task: str
    solution: str
    hint: str
    difficulty: int

# Schemas when receiving an exercise
class ExerciseReceiveRespond(BaseModel):
    id: int
    name: str
    description: str
    task: str
    solution: str
    hint: str
    difficulty: int

    class Config:
        orm_mode = True