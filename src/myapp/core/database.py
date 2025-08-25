from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Correctly encoded password (ashi@8600 → ashi%408600)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:{password}@localhost:5432/python_project"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()