
from sqlalchemy import Column, Integer, String, JSON
from config.database import Base

class Freelancer(Base):
    __tablename__ = "freelancers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    skills = Column(JSON, nullable=False)
    hourly_rate = Column(Integer, nullable=False)
    experience = Column(String(50), nullable=False)
    hired_jobs = Column(JSON, default=list)
