
from sqlalchemy.orm import Session
from config.database import get_db, create_tables
from database.freelancer_db import FreelancerDB
from database.job_db import JobDB

class DataService:
    @staticmethod
    def initialize_database():
        create_tables()
        db = next(get_db())
        try:
            FreelancerDB.insert_sample_data(db)
            JobDB.insert_sample_data(db)
        except Exception as e:
            db.rollback()
            print(f"Error inserting sample data: {e}")
        finally:
            db.close()
