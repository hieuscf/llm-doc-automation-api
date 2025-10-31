from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.config import settings

# Kết nối PostgreSQL qua SQLAlchemy
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency cho FastAPI để dùng session DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
