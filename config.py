import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
class Config:
    DEBUG = os.getenv("DEBUG", True)
    CREATE_DB_IF_NOT_FOUND = os.getenv("CREATE_DB_IF_NOT_FOUND", True)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    SECRET_KEY = os.getenv("SECRET_KEY")