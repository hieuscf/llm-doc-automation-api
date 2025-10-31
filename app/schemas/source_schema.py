from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime

class SourceBase(BaseModel):
    source_name: str
    url: HttpUrl | str  
    last_crawled_at: datetime | None = None

class SourceCreate(SourceBase):
    pass

class SourceUpdate(BaseModel):
    source_name: str | None = None
    url: HttpUrl | None = None
    last_crawled_at: datetime | None = None

class SourceResponse(SourceBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True