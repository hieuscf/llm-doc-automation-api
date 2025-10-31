from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.services.source_service import SourceService
from app.schemas.source_schema import SourceCreate, SourceUpdate

class SourceController:
    def __init__(self):
        self.service = SourceService()

    def get_all_sources(self, db: Session):
        return self.service.get_all(db)

    def get_source_by_id(self, db: Session, source_id: UUID):
        source = self.service.get_by_id(db, source_id)
        if not source:
            raise HTTPException(status_code=404, detail="Source không tồn tại")
        return source

    def create_source(self, db: Session, payload: SourceCreate):
        return self.service.create(db, payload)

    def update_source(self, db: Session, source_id: UUID, payload: SourceUpdate):
        updated = self.service.update(db, source_id, payload)
        if not updated:
            raise HTTPException(status_code=404, detail="Source không tồn tại")
        return updated

    def delete_source(self, db: Session, source_id: UUID):
        deleted = self.service.delete(db, source_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Source không tồn tại")
        return {"message": "Source đã được xóa thành công"}
