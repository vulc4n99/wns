from fastapi import FastAPI
from routers.main_router import router
from services.data_service import DataService

app = FastAPI()

# Initialize database and sample data
DataService.initialize_database()

# Include all routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)