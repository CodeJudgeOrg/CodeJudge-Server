from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.postgresql_server_db import Base

class SubmissionTable(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    exerciseName = Column(String, nullable = False)
    task = Column(Text, nullable = False)
    code = Column(Text, nullable = False)
    output = Column(String, nullable = False)
    studentName = Column(String, nullable = False)