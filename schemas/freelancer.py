
from typing import List, Optional
from pydantic import BaseModel

class FreelancerBase(BaseModel):
    name: str
    skills: List[str]
    hourly_rate: int
    experience: str

class FreelancerCreate(FreelancerBase):
    pass

class FreelancerResponse(FreelancerBase):
    id: int
    hired_jobs: List[int] = []

    class Config:
        from_attributes = True

class FreelancerList(BaseModel):
    freelancers: List[FreelancerResponse]
