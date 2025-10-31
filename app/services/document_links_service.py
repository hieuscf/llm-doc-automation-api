from sqlalchemy.orm import Session
from uuid import UUID
from app.models.document_links_model import DocumentLink
from app.models.source_model import Source

def get_all_document_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DocumentLink).offset(skip).limit(limit).all()

def get_document_link_by_id(db: Session, link_id: UUID):
    return db.query(DocumentLink).filter(DocumentLink.id == link_id).first()

def create_document_link(db: Session, source_id: UUID, url: str, file_type: str = None, level: int = 1):
    new_link = DocumentLink(
        source_id=source_id,
        url=url,
        file_type=file_type,
        level=level
    )
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

def update_document_link(db: Session, link_id: UUID, **kwargs):
    link = get_document_link_by_id(db, link_id)
    if not link:
        return None
    for key, value in kwargs.items():
        if hasattr(link, key):
            setattr(link, key, value)
    db.commit()
    db.refresh(link)
    return link

def delete_document_link(db: Session, link_id: UUID):
    link = get_document_link_by_id(db, link_id)
    if not link:
        return None
    db.delete(link)
    db.commit()
    return link
