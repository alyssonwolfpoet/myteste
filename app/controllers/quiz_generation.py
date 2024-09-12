from database import get_document_by_id

def generate_quiz(document_id: int):
    doc = get_document_by_id(document_id)
    if doc:
        # Implementar a lógica para gerar um quiz com base no conteúdo do documento
        return "Generated quiz based on document"
    return "Document not found"