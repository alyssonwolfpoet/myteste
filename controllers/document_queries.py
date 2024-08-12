from database import get_document_by_id
from clients.ollama_client import ask_question

def ask_about_document(document_id: int, question: str):
    doc = get_document_by_id(document_id)
    if doc:
        answer = ask_question(question, doc.content)
        return answer
    return "Document not found"
