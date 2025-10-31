from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.config.database import get_db
from app.controller.document_links_controller import DocumentLinkController
from app.schemas.document_links_schema import DocumentLinkCreate , DocumentLinkUpdate

router = APIRouter(prefix="/document-links", tags=["DocumentLinks"])


def get_controller(db: Session = Depends(get_db)):
    return DocumentLinkController(db)

@router.get("/")
def list_document_links(skip: int = 0, limit: int = 100, controller: DocumentLinkController = Depends(get_controller)):
    return controller.list(skip, limit)

@router.get("/{link_id}")
def get_document_link(link_id: UUID, controller: DocumentLinkController = Depends(get_controller)):
    return controller.get(link_id)

@router.post("/")
def create_document_link_endpoint(payload: DocumentLinkCreate, controller: DocumentLinkController = Depends(get_controller)):
    return controller.create(**payload.dict())

@router.put("/{link_id}")
def update_document_link_endpoint(link_id: UUID, payload: DocumentLinkUpdate, controller: DocumentLinkController = Depends(get_controller)):
    return controller.update(link_id, **payload.dict(exclude_unset=True))

@router.delete("/{link_id}")
def delete_document_link_endpoint(link_id: UUID, controller: DocumentLinkController = Depends(get_controller)):
    return controller.delete(link_id)

document_links_route = router