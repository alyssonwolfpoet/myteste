from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
    content = Column(String)

class DocumentEmbedding(Base):
    __tablename__ = "document_embeddings"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer)
    vector = Column(String)

Base.metadata.create_all(bind=engine)