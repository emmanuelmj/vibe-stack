from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Initialize the SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create a sessionmaker bundle
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """ Dependency for getting the database session in FastAPI routes """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
