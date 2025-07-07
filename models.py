
from sqlalchemy import create_engine, Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

Base = declarative_base()

class Freelancer(Base):
    __tablename__ = "freelancers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    skills = Column(JSON, nullable=False)
    hourly_rate = Column(Integer, nullable=False)
    experience = Column(String(50), nullable=False)
    hired_jobs = Column(JSON, default=list)

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    budget = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    client = Column(String(100), nullable=False)

# Database configuration
DATABASE_URL = "sqlite:///./freelancer_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
