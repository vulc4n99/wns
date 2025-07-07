
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from models.freelancer import Freelancer

class FreelancerDB:
    @staticmethod
    def get_all(db: Session) -> List[Freelancer]:
        return db.query(Freelancer).all()
    
    @staticmethod
    def get_by_id(db: Session, freelancer_id: int) -> Freelancer:
        return db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()
    
    @staticmethod
    def create(db: Session, name: str, skills: List[str], hourly_rate: int, experience: str) -> Freelancer:
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
        return freelancer
    
    @staticmethod
    def insert_sample_data(db: Session):
        freelancer_count = db.query(Freelancer).count()
        
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
