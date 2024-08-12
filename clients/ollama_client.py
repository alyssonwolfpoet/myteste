#from ollama import Ollama
#from langchain_community.llms import Ollama
import ollama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

#ollama = Ollama(api_key=os.getenv("OLLAMA_API_KEY"))
#embedding = OllamaEmbeddings()

#ollama = Ollama()

embedding = OllamaEmbeddings(model="llama3")

def generate_embedding(text: str) -> list:
    response = embedding.embed_query(text)
    print(response)
    return response

def ask_question(question: str, context: str) -> str:
    response = ollama.complete(prompt=f"Context: {context}\n\nQuestion: {question}", model="llama3.1")
    return response['text']