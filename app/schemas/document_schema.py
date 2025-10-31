from pydantic import BaseModel, UUID4, HttpUrl
from typing import Optional, Any , Dict
from datetime import datetime


# --- Base ---
class DocumentBase(BaseModel):
    url: HttpUrl
    local_path: Optional[str] = None
    file_type: Optional[str] = None
    document_type: Optional[str] = "khac"  
    document_subtype: Optional[str] = None  
    title: Optional[str] = None
    content: Optional[str] = None
    text_excerpt: Optional[str] = None
    size: Optional[int] = None
    analysis: Optional[Any] = None  # JSON field


# --- Create ---
class DocumentCreate(BaseModel):
    source_id: UUID
    url: str
    local_path: Optional[str] = None
    file_type: Optional[str] = None
    document_type: Optional[str] = "khac"
    document_subtype: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    text_excerpt: Optional[str] = None
    size: Optional[int] = None
    analysis: Optional[Dict] = None

class DocumentUpdate(BaseModel):
    url: Optional[str]
    local_path: Optional[str]
    file_type: Optional[str]
    document_type: Optional[str]
    document_subtype: Optional[str]
    title: Optional[str]
    content: Optional[str]
    text_excerpt: Optional[str]
    size: Optional[int]
    analysis: Optional[Dict]


# --- Response ---
class DocumentResponse(DocumentBase):
    id: UUID4
    source_id: UUID4
    downloaded_at: Optional[datetime] = None
    analyzed_at: Optional[datetime] = None

    class Config:
        from_attributes = True  
