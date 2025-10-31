from uuid import UUID
from sqlalchemy.orm import Session
from app.models.source_model import Source
from app.schemas.source_schema import SourceCreate, SourceUpdate

class SourceService:
    def get_all(self, db: Session):
        return db.query(Source).all()

    def get_by_id(self, db: Session, source_id: UUID):
        return db.query(Source).filter(Source.id == source_id).first()

    def create(self, db: Session, source_data: SourceCreate):
        new_source = Source(**source_data.model_dump())
        db.add(new_source)
        db.commit()
        db.refresh(new_source)
        return new_source

    def update(self, db: Session, source_id: UUID, source_data: SourceUpdate):
        source = db.query(Source).filter(Source.id == source_id).first()
        if not source:
            return None
        for key, value in source_data.model_dump(exclude_unset=True).items():
            setattr(source, key, value)
        db.commit()
        db.refresh(source)
        return source

    def delete(self, db: Session, source_id: UUID):
        source = db.query(Source).filter(Source.id == source_id).first()
        if not source:
            return None
        db.delete(source)
        db.commit()
        return source
