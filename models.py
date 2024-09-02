from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    modulo_id = mapped_column(ForeignKey("modulo_curso.id"))
    content = Column(String)

class DocumentEmbedding(Base):
    __tablename__ = "document_embeddings"
    id = Column(Integer, primary_key=True, index=True)
    document_id = mapped_column(ForeignKey("documents.id"))
    vector = Column(String)

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Modulo_curso(Base):
    __tablename__ = "modulo_curso"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    curso_id = mapped_column(ForeignKey("cursos.id"))

class Trascricao(Base):
    __tablename__ = "trascricao"
    id = Column(Integer, primary_key=True, index=True)
    curso_id = mapped_column(ForeignKey("cursos.id"))
    modelo_id = mapped_column(ForeignKey("modulo_curso.id"))
    uuid = Column(String)
    content = Column(String)
    vector = Column(String)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
