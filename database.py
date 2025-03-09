from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL (modify if needed)
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:ArshithBabuSD@localhost/video_recommendation"

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base for models
Base = declarative_base()
