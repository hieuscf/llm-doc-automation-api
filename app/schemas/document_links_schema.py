from pydantic import BaseModel, HttpUrl, UUID4
from datetime import datetime
from typing import Optional

# --- Base ---
class DocumentLinkBase(BaseModel):
    url: HttpUrl
    file_type: Optional[str] = None
    level: Optional[int] = 1
    status: Optional[str] = "pending"
    retries: Optional[int] = 0


# --- Create ---
class DocumentLinkCreate(DocumentLinkBase):
    source_id: UUID4


# --- Update ---
class DocumentLinkUpdate(BaseModel):
    status: Optional[str] = None
    retries: Optional[int] = None


# --- Response ---
class DocumentLinkResponse(DocumentLinkBase):
    id: UUID4
    source_id: UUID4
    discovered_at: datetime

    class Config:
        from_attributes = True  
