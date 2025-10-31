from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from pydantic import BaseModel
from typing import Optional, Dict
from app.config.database import get_db
from app.controller.documents_controller import DocumentController

router = APIRouter(prefix="/documents", tags=["Documents"])

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

def get_controller(db: Session = Depends(get_db)):
    return DocumentController(db)

@router.get("/")
def list_documents(skip: int = 0, limit: int = 100, controller: DocumentController = Depends(get_controller)):
    return controller.list(skip, limit)

@router.get("/{doc_id}")
def get_document(doc_id: UUID, controller: DocumentController = Depends(get_controller)):
    return controller.get(doc_id)

@router.post("/")
def create_document_endpoint(payload: DocumentCreate, controller: DocumentController = Depends(get_controller)):
    return controller.create(**payload.dict())

@router.put("/{doc_id}")
def update_document_endpoint(doc_id: UUID, payload: DocumentUpdate, controller: DocumentController = Depends(get_controller)):
    return controller.update(doc_id, **payload.dict(exclude_unset=True))

@router.delete("/{doc_id}")
def delete_document_endpoint(doc_id: UUID, controller: DocumentController = Depends(get_controller)):
    return controller.delete(doc_id)

documents_route = router