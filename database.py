from models import SessionLocal, Document, DocumentEmbedding, Curso, Trascricao,Modulo_curso

def save_document(name: str, content: str,modulo_id:int):
    db = SessionLocal()
    doc = Document(name=name, content=content, modulo_id = modulo_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc.id

def save_embedding(document_id: int, vector: list):
    db = SessionLocal()
    embedding = DocumentEmbedding(document_id=document_id, vector=vector)
    db.add(embedding)
    db.commit()

def save_curso(curso_name):
     db = SessionLocal()
     curso = Curso(name = curso_name)
     db.add(curso)
     db.commit()
     return curso.id

def save_Modulo_curso(name,curso_id):
    db = SessionLocal()
    modulo = Modulo_curso(name = name, curso_id = curso_id)
    db.add(modulo)
    db.commit()
    return modulo.id

def get_document_by_id(document_id: int):
    db = SessionLocal()
    return db.query(Document).filter(Document.id == document_id).first()

