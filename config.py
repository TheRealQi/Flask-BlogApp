import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
class Config:
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
    CREATE_DB_IF_NOT_FOUND = os.getenv("CREATE_DB_IF_NOT_FOUND", True)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///sql.db")
    SECRET_KEY = os.getenv("SECRET_KEY")