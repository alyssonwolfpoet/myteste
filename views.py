from fastapi import APIRouter, UploadFile, File,status,HTTPException ,Form
from typing import List
from controllers.file_processing import process_files
from controllers.document_queries import ask_about_document
from controllers.quiz_generation import generate_quiz
from pydantic import BaseModel

router = APIRouter()

class Curso(BaseModel): #serialize
    cursoname:str
    modulo:str

    class Config:
        orm_mode = True

@router.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    response = process_files(files)
    return response

@router.get("/ask/")
def ask_about_document_endpoint(document_id: int, question: str):
    answer = ask_about_document(document_id, question)
    return {"answer": answer}

@router.get("/generate_quiz/")
def generate_quiz_endpoint(document_id: int):
    quiz = generate_quiz(document_id)
    return {"quiz": quiz}

@router.post("/curso/",response_model=Curso,status_code=200)
async def test(curso:Curso):
    return curso

class FileUploadData(BaseModel):
    cursoname: str
    modulo: str

async def process_filesteste(files: List[UploadFile], cursoname: str, modulo: str) -> dict:
    results = []
    for file in files:
        content = await file.read()
        results.append({
            "filename": file.filename,
            "content_size": len(content),
            "cursoname": cursoname,
            "modulo": modulo
        })
    return {"processed_files": results}

@router.post("/curso2/")
async def curse2(
    cursoname: str = Form(...),
    modulo: str = Form(...),
    files: List[UploadFile] = File(...)
):
    if not files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado.")
    
    response = await process_filesteste(files, cursoname, modulo)
    return response