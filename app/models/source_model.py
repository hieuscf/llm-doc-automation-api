import uuid
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base
from sqlalchemy.orm import relationship

class Source(Base):
    __tablename__ = "sources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_name = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    last_crawled_at = Column(DateTime, nullable=True)

    # Liên kết 1-n
    document_links = relationship("DocumentLink", back_populates="source", cascade="all, delete-orphan")