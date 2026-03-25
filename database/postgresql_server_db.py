from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://codejudge:1Q?GNVXGsWJ@localhost:5432/codejudge_server_db"

# Connect to the db
engine = create_engine(DATABASE_URL)

# Start a session for db operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Use table modells
Base = declarative_base()
