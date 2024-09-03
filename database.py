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

def save_trascricao(curso_id,modelo_id,uuid,content,vector):
    db = SessionLocal()
    trascricao = Trascricao(curso_id=curso_id,modelo_id=modelo_id,uuid=uuid,content=content,vector=vector)
    db.add(trascricao)
    db.commit()
    return trascricao.id

def get_document_by_id(document_id: int):
    db = SessionLocal()
    return db.query(Document).filter(Document.id == document_id).first()

def get_curso_by_name(namecurso):
    db = SessionLocal()
    return db.query(Curso).filter(Curso.name == namecurso).first()

def get_curso_by_id(id_curso):
    db = SessionLocal()
    return db.query(Curso).filter(Curso.id == id_curso).first()

def get_modulo_by_name(curso_id,modulo_id):
    db = SessionLocal()
    return db.query(Modulo_curso).filter(Curso.id == curso_id,Document.modulo_id == modulo_id).first()

def get_trascript_by_uuid(uuid:str):
    db = SessionLocal()
    return db.query(Trascricao).filter(Trascricao.uuid == uuid).first()

def get_document_modulo_by_id(modulo_id:int,doc_id):
    db = SessionLocal()
    return db.query(Document).filter(Document.modulo_id == modulo_id,Document.id == doc_id).first()

def get_trascricao_modulo_Curso_by_id(modulo_id:int,uuid:str):
    db = SessionLocal()
    return db.query(Trascricao).filter(Trascricao.modelo_id == modulo_id,Trascricao.uuid == uuid,).first()

