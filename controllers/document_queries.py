from database import get_document_by_id,get_document_modulo_by_id,get_modulo_by_name,get_curso_by_id,get_trascricao_modulo_Curso_by_id
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
        curso = get_curso_by_id(curso_id)
        print(f"\n{curso.name}\n")

        modulo= get_modulo_by_name(curso_id,modulo_id)
        print(f"\n{modulo.name}\n")

        answer = ask_question(query, doc.content)

        return {"curso_nome": curso.name, "modulo": modulo.name, "answer": answer}
    return "Document not found"
        

def ask_about_trascript(model_id:int,uuid:str,question:str):
    doc = get_trascricao_modulo_Curso_by_id(model_id,uuid)
    if doc:
        answer = ask_question(question, doc.content)
        return answer
    return "Document not found"
