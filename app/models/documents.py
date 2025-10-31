from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app.config.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_id = Column(UUID(as_uuid=True), ForeignKey("sources.id"))
    url = Column(String, nullable=False)
    local_path = Column(String, nullable=True)
    file_type = Column(String(10), nullable=True)
    document_type = Column(String(50), default="khac")     # ví dụ: hanh_chinh, phap_luat
    document_subtype = Column(String(50), nullable=True)   # ví dụ: cong_van, thong_bao, nghi_dinh
    title = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    text_excerpt = Column(Text, nullable=True)
    size = Column(Integer, nullable=True)
    analysis = Column(JSON, nullable=True)
    downloaded_at = Column(DateTime, nullable=True)
    analyzed_at = Column(DateTime, nullable=True)