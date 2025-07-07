
from fastapi import APIRouter
from api.freelancer_api import router as freelancer_router
from api.job_api import router as job_router

router = APIRouter()

router.include_router(freelancer_router)
router.include_router(job_router)

@router.get("/")
def home():
    return {"message": "Hello welcome to Freelancer app"}
