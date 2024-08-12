from models import SessionLocal, Document, DocumentEmbedding

def save_document(name: str, content: str):
    db = SessionLocal()
    doc = Document(name=name, content=content)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc.id

def save_embedding(document_id: int, vector: list):
    db = SessionLocal()
    embedding = DocumentEmbedding(document_id=document_id, vector=vector)
    db.add(embedding)
    db.commit()

def get_document_by_id(document_id: int):
    db = SessionLocal()
    return db.query(Document).filter(Document.id == document_id).first()