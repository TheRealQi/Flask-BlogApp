import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
class Config:
    DEBUG = os.getenv("DEBUG", True)
    DATABASE = os.getenv("DATABASE", "SQL")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    MONGO_URI = os.getenv("MONGO_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=int(os.getenv("PERMANENT_SESSION_LIFETIME", 3600)))
