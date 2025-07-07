
from typing import Optional, List
from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    description: str
    budget: int
    status: str
    client: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True

class JobList(BaseModel):
    jobs: List[JobResponse]
