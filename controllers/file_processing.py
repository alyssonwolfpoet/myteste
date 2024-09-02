from database import save_document, save_embedding , save_curso , save_Modulo_curso,save_trascricao
from clients.ollama_client import generate_embedding
from utils.file_readers import read_pdf, read_csv, read_odt, read_csv2

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


def process_files2(files,modulo_id,curso_id):
    for file in files:
        contents = file.file.read()
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(contents)
        
        if file.filename.endswith(".pdf"):
            content = read_pdf(file_path)

            doc_id = save_document(file.filename, content,modulo_id=modulo_id)
            vector = generate_embedding(content)
            save_embedding(doc_id, vector)
        elif file.filename.endswith(".csv"):
            print("\n\n")
            content = read_csv2(file_path)
            transcribed_data = content[['transcript', 'uuid']]
            print(transcribed_data)
            print("\n\n")

            for index, row in content.iterrows():
                transcript = row['transcript']
                uuid = row['uuid']
    
                # Fazer algo com o transcript e uuid
                print(f'Transcript: {transcript}, UUID: {uuid}')
                vector = generate_embedding(transcript)
                save_trascricao(curso_id=curso_id,modelo_id=modulo_id,uuid=uuid,content=transcript,vector=vector)

            content = curso_id
        elif file.filename.endswith(".odt"):
            content = read_odt(file_path)

            doc_id = save_document(file.filename, content,modulo_id=modulo_id)
            vector = generate_embedding(content)
            save_embedding(doc_id, vector)
        else:
            return {"error": "Unsupported file type"}
        
    
    return {"status": "Files uploaded and processed successfully"}

def curso_modulo_up(files, cursoname, modulo):
    curso_id = save_curso(curso_name= cursoname)
    modulo_id = save_Modulo_curso(name= modulo,curso_id=curso_id)
    a = process_files2(files,modulo_id=modulo_id,curso_id=curso_id)
    return a