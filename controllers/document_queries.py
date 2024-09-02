from database import get_document_by_id,get_document_modulo_by_id,get_modulo_by_name,get_curso_by_id
from clients.ollama_client import ask_question

def ask_about_document(document_id: int, question: str):
    doc = get_document_by_id(document_id)
    if doc:
        answer = ask_question(question, doc.content)
        return answer
    return "Document not found"

def ask_about_document2(curso_id:int,document_id:int,query:str,modulo_id:int):
    doc = get_document_modulo_by_id(modulo_id=modulo_id,doc_id=document_id)
    if doc:
        curso_name = get_curso_by_id(curso_id)
        print(f"\n{curso_name.name}\n")

        modulo_name= get_modulo_by_name(curso_id,modulo_id)
        print(f"\n{modulo_name.name}\n")

        answer = ask_question(query, doc.content)

        return answer,curso_name.name,modulo_name.name
    return "Document not found"
        


def ask_about_trascript(curso_id:int,uuid:int,query:str):
    print("oi")
