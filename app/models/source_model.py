from sqlalchemy import Column, String, DateTime, func
from app.config.database import Base
import uuid

class Source(Base):
    __tablename__ = "sources"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source_name = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    last_crawled_at = Column(DateTime, nullable=True)
