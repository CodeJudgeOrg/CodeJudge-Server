from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.postgresql_server_db import Base

class Exercises(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    task = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)
    hint = Column(Text, nullable=False)
    difficulty = Column(Integer, nullable=False)
