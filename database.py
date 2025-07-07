
from sqlalchemy.orm import Session
from models import Freelancer, Job, create_tables, SessionLocal
from typing import List, Dict, Any

class DatabaseManager:
    def __init__(self):
        create_tables()
        self.insert_sample_data()
    
    def get_db_session(self):
        return SessionLocal()
    
    def insert_sample_data(self):
        db = self.get_db_session()
        try:
            # Check if data already exists
            job_count = db.query(Job).count()
            freelancer_count = db.query(Freelancer).count()
            
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
            
            if freelancer_count == 0:
                sample_freelancers = [
                    Freelancer(
                        name="Sarah Johnson",
                        skills=["Python", "Django", "Flask"],
                        hourly_rate=45,
                        experience="5 years",
                        hired_jobs=[]
                    ),
                    Freelancer(
                        name="Mike Chen",
                        skills=["JavaScript", "React", "Node.js"],
                        hourly_rate=60,
                        experience="7 years",
                        hired_jobs=[]
                    ),
                    Freelancer(
                        name="Lisa Wong",
                        skills=["UI/UX Design", "Figma", "Adobe XD"],
                        hourly_rate=50,
                        experience="4 years",
                        hired_jobs=[]
                    )
                ]
                for freelancer in sample_freelancers:
                    db.add(freelancer)
            
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error inserting sample data: {e}")
        finally:
            db.close()
    
    def get_all_jobs(self) -> List[Dict[str, Any]]:
        db = self.get_db_session()
        try:
            jobs = db.query(Job).all()
            return [
                {
                    "id": job.id,
                    "title": job.title,
                    "description": job.description,
                    "budget": job.budget,
                    "status": job.status,
                    "client": job.client
                }
                for job in jobs
            ]
        finally:
            db.close()
    
    def get_job_by_id(self, job_id: int) -> Dict[str, Any] | None:
        db = self.get_db_session()
        try:
            job = db.query(Job).filter(Job.id == job_id).first()
            if job:
                return {
                    "id": job.id,
                    "title": job.title,
                    "description": job.description,
                    "budget": job.budget,
                    "status": job.status,
                    "client": job.client
                }
            return None
        finally:
            db.close()
    
    def add_job(self, title: str, description: str, budget: int, status: str, client: str) -> int:
        db = self.get_db_session()
        try:
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
            return job.id
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    def get_all_freelancers(self) -> List[Dict[str, Any]]:
        db = self.get_db_session()
        try:
            freelancers = db.query(Freelancer).all()
            return [
                {
                    "id": freelancer.id,
                    "name": freelancer.name,
                    "skills": freelancer.skills,
                    "hourly_rate": freelancer.hourly_rate,
                    "experience": freelancer.experience,
                    "hired_jobs": freelancer.hired_jobs
                }
                for freelancer in freelancers
            ]
        finally:
            db.close()
    
    def get_freelancer_by_id(self, freelancer_id: int) -> Dict[str, Any] | None:
        db = self.get_db_session()
        try:
            freelancer = db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()
            if freelancer:
                return {
                    "id": freelancer.id,
                    "name": freelancer.name,
                    "skills": freelancer.skills,
                    "hourly_rate": freelancer.hourly_rate,
                    "experience": freelancer.experience,
                    "hired_jobs": freelancer.hired_jobs
                }
            return None
        finally:
            db.close()
    
    def add_freelancer(self, name: str, skills: List[str], hourly_rate: int, experience: str) -> int:
        db = self.get_db_session()
        try:
            freelancer = Freelancer(
                name=name,
                skills=skills,
                hourly_rate=hourly_rate,
                experience=experience,
                hired_jobs=[]
            )
            db.add(freelancer)
            db.commit()
            db.refresh(freelancer)
            return freelancer.id
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
