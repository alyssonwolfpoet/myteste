from fastapi import APIRouter, UploadFile, File
from typing import List
from controllers.file_processing import process_files
from controllers.document_queries import ask_about_document
from controllers.quiz_generation import generate_quiz

router = APIRouter()

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
