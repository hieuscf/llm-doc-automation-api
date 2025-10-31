import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base

class DocumentLink(Base):
    __tablename__ = "document_links"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_id = Column(UUID(as_uuid=True), ForeignKey("sources.id", ondelete="CASCADE"))
    url = Column(Text, nullable=False)
    file_type = Column(String(10))
    level = Column(Integer, default=1)
    discovered_at = Column(DateTime, server_default=func.now())
    status = Column(String(20), default="pending")  # pending / downloaded / failed
    retries = Column(Integer, default=0)

    # Quan hệ ngược đến Source
    source = relationship("Source", back_populates="document_links")