from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.services.documents_service import (
    get_all_documents,
    get_document_by_id,
    create_document,
    update_document,
    delete_document
)

class DocumentController:
    def __init__(self, db: Session):
        self.db = db

    def list(self, skip: int = 0, limit: int = 100):
        return get_all_documents(self.db, skip, limit)

    def get(self, doc_id: UUID):
        doc = get_document_by_id(self.db, doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    def create(self, **kwargs):
        return create_document(self.db, **kwargs)

    def update(self, doc_id: UUID, **kwargs):
        doc = update_document(self.db, doc_id, **kwargs)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    def delete(self, doc_id: UUID):
        doc = delete_document(self.db, doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return {"detail": "Document deleted successfully"}
