#from ollama import Ollama
#from langchain_community.llms import Ollama
import ollama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

#ollama = Ollama(api_key=os.getenv("OLLAMA_API_KEY"))
embedding = FastEmbedEmbeddings()

#ollama = Ollama()



embeddings = OllamaEmbeddings(model="llama3")
def generate_embedding(text: str) -> list:
    response = ollama.embed(input==text,model=embeddings)
    return response['embedding']

def ask_question(question: str, context: str) -> str:
    response = ollama.complete(prompt=f"Context: {context}\n\nQuestion: {question}", model="llama3.1")
    return response['text']