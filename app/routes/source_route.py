from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.config.database import SessionLocal
from app.controller.source_controller import SourceController
from app.schemas.source_schema import SourceCreate, SourceResponse, SourceUpdate

router = APIRouter(prefix="/sources", tags=["Sources"])
controller = SourceController()

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[SourceResponse])
def get_sources(db: Session = Depends(get_db)):
    return controller.get_all_sources(db)

@router.get("/{source_id}", response_model=SourceResponse)
def get_source(source_id: UUID, db: Session = Depends(get_db)):
    return controller.get_source_by_id(db, source_id)

@router.post("/", response_model=SourceResponse)
def create_source(payload: SourceCreate, db: Session = Depends(get_db)):
    return controller.create_source(db, payload)

@router.put("/{source_id}", response_model=SourceResponse)
def update_source(source_id: UUID, payload: SourceUpdate, db: Session = Depends(get_db)):
    return controller.update_source(db, source_id, payload)

@router.delete("/{source_id}")
def delete_source(source_id: UUID, db: Session = Depends(get_db)):
    return controller.delete_source(db, source_id)

source_route = router
