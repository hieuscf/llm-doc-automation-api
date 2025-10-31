from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from app.models.documents import Document

def get_all_documents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Document).offset(skip).limit(limit).all()

def get_document_by_id(db: Session, doc_id: UUID):
    return db.query(Document).filter(Document.id == doc_id).first()

def create_document(db: Session, source_id: UUID, url: str, local_path: str = None,
                    file_type: str = None, document_type: str = "khac",
                    document_subtype: str = None, title: str = None,
                    content: str = None, text_excerpt: str = None,
                    size: int = None, analysis: dict = None):
    new_doc = Document(
        source_id=source_id,
        url=url,
        local_path=local_path,
        file_type=file_type,
        document_type=document_type,
        document_subtype=document_subtype,
        title=title,
        content=content,
        text_excerpt=text_excerpt,
        size=size,
        analysis=analysis,
        downloaded_at=datetime.utcnow() if local_path else None
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def update_document(db: Session, doc_id: UUID, **kwargs):
    doc = get_document_by_id(db, doc_id)
    if not doc:
        return None
    for key, value in kwargs.items():
        if hasattr(doc, key):
            setattr(doc, key, value)
    db.commit()
    db.refresh(doc)
    return doc

def delete_document(db: Session, doc_id: UUID):
    doc = get_document_by_id(db, doc_id)
    if not doc:
        return None
    db.delete(doc)
    db.commit()
    return doc
