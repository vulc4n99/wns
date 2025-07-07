
from sqlalchemy import Column, Integer, String, Text
from config.database import Base

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    budget = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    client = Column(String(100), nullable=False)
