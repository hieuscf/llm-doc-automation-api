import uuid
from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base

class Setting(Base):   # 👉 nên đổi tên class khớp với bảng
    __tablename__ = "setting"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    max_depth = Column(Integer, default=2)
    link_limit = Column(Integer, default=1000) 
    allowed_domains = Column(String, nullable=True)
    time_reload = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    last_crawled_at = Column(DateTime, nullable=True)