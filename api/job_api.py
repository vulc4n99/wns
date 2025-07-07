
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.job import JobCreate, JobResponse, JobList
from database.job_db import JobDB

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/", response_model=JobList)
def get_jobs(db: Session = Depends(get_db)):
    jobs = JobDB.get_all(db)
    return {"jobs": jobs}

@router.get("/{job_id}", response_model=JobResponse)
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):
    job = JobDB.get_by_id(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/post", response_model=JobResponse)
def post_job(job: JobCreate, db: Session = Depends(get_db)):
    created_job = JobDB.create(
        db=db,
        title=job.title,
        description=job.description,
        budget=job.budget,
        status=job.status,
        client=job.client
    )
    return created_job
