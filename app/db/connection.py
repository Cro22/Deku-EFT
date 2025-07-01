import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the full database URL, e.g. "postgresql://user:pass@db:5432/dbname"
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
# pool_pre_ping=True helps prevent "stale connections" errors
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create a configured "SessionLocal" class
# autocommit=False, autoflush=False are the recommended defaults
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
