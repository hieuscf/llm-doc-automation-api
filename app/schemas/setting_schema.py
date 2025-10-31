from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID as UUIDType
from pydantic import BaseModel, UUID4



class SettingBase(BaseModel):
    max_depth: Optional[int] = 2
    link_limit: Optional[int] = 100
    allowed_domains: Optional[str] = None
    time_reload: Optional[datetime] = None
    last_crawled_at: Optional[datetime] = None



class SettingCreate(SettingBase):
    pass


class SettingUpdate(SettingBase):
    pass


class SettingResponse(SettingBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True
