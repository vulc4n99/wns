
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.freelancer import FreelancerCreate, FreelancerResponse, FreelancerList
from database.freelancer_db import FreelancerDB

router = APIRouter(prefix="/freelancers", tags=["freelancers"])

@router.get("/", response_model=FreelancerList)
def get_freelancers(db: Session = Depends(get_db)):
    freelancers = FreelancerDB.get_all(db)
    return {"freelancers": freelancers}

@router.get("/{freelancer_id}", response_model=FreelancerResponse)
def get_freelancer_by_id(freelancer_id: int, db: Session = Depends(get_db)):
    freelancer = FreelancerDB.get_by_id(db, freelancer_id)
    if not freelancer:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return freelancer

@router.post("/register", response_model=dict)
def register_freelancer(freelancer: FreelancerCreate, db: Session = Depends(get_db)):
    created_freelancer = FreelancerDB.create(
        db=db,
        name=freelancer.name,
        skills=freelancer.skills,
        hourly_rate=freelancer.hourly_rate,
        experience=freelancer.experience
    )
    return {
        "message": "Freelancer registered successfully",
        "freelancer": created_freelancer
    }
