
from sqlalchemy.orm import Session
from typing import List
from models.job import Job

class JobDB:
    @staticmethod
    def get_all(db: Session) -> List[Job]:
        return db.query(Job).all()
    
    @staticmethod
    def get_by_id(db: Session, job_id: int) -> Job:
        return db.query(Job).filter(Job.id == job_id).first()
    
    @staticmethod
    def create(db: Session, title: str, description: str, budget: int, status: str, client: str) -> Job:
        job = Job(
            title=title,
            description=description,
            budget=budget,
            status=status,
            client=client
        )
        db.add(job)
        db.commit()
        db.refresh(job)
        return job
    
    @staticmethod
    def insert_sample_data(db: Session):
        job_count = db.query(Job).count()
        
        if job_count == 0:
            sample_jobs = [
                Job(
                    title="Website Development",
                    description="Build a company website with React and Node.js",
                    budget=1500,
                    status="open",
                    client="Acme Corp"
                ),
                Job(
                    title="Mobile App Design",
                    description="UI/UX design for a food delivery app",
                    budget=800,
                    status="open",
                    client="Foodie Inc"
                ),
                Job(
                    title="Python Scripting",
                    description="Automate data processing tasks",
                    budget=300,
                    status="open",
                    client="DataWorks"
                )
            ]
            for job in sample_jobs:
                db.add(job)
            db.commit()
