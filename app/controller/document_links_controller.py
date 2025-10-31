from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.services.document_links_service import (
    get_all_document_links,
    get_document_link_by_id,
    create_document_link,
    update_document_link,
    delete_document_link
)

class DocumentLinkController:
    def __init__(self, db: Session):
        self.db = db

    def list(self, skip: int = 0, limit: int = 100):
        return get_all_document_links(self.db, skip, limit)

    def get(self, link_id: UUID):
        link = get_document_link_by_id(self.db, link_id)
        if not link:
            raise HTTPException(status_code=404, detail="DocumentLink not found")
        return link

    def create(self, source_id: UUID, url: str, file_type: str = None, level: int = 1):
        return create_document_link(self.db, source_id, url, file_type, level)

    def update(self, link_id: UUID, **kwargs):
        link = update_document_link(self.db, link_id, **kwargs)
        if not link:
            raise HTTPException(status_code=404, detail="DocumentLink not found")
        return link

    def delete(self, link_id: UUID):
        link = delete_document_link(self.db, link_id)
        if not link:
            raise HTTPException(status_code=404, detail="DocumentLink not found")
        return {"detail": "DocumentLink deleted successfully"}
