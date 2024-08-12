from database import save_document, save_embedding
from clients.ollama_client import generate_embedding
from utils.file_readers import read_pdf, read_csv, read_odt

def process_files(files):
    for file in files:
        contents = file.file.read()
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(contents)
        
        if file.filename.endswith(".pdf"):
            content = read_pdf(file_path)
        elif file.filename.endswith(".csv"):
            content = read_csv(file_path)
        elif file.filename.endswith(".odt"):
            content = read_odt(file_path)
        else:
            return {"error": "Unsupported file type"}
        
        doc_id = save_document(file.filename, content)
        vector = generate_embedding(content)
        save_embedding(doc_id, vector)
    
    return {"status": "Files uploaded and processed successfully"}