Claro! Vou fornecer um exemplo completo de como configurar um projeto usando FastAPI, Ollama e LangChain com o modelo Llama 3.1. Esse exemplo incluirá um arquivo `docker-compose.yml` e alguns arquivos de configuração para o FastAPI.

### Estrutura do Projeto

```
my_project/
│
├── docker-compose.yml
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── clients/
│       └── ollama_client.py
```

### 1. Arquivo `docker-compose.yml`

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/app/data

  fastapi:
    build:
      context: ./app
    ports:
      - "8000:8000"
    depends_on:
      - ollama
    volumes:
      - ./app:/app

volumes:
  ollama_data:
```

### 2. Arquivo `requirements.txt` (dentro de `app/`)

```plaintext
fastapi
uvicorn
httpx
langchain
```

### 3. Arquivo `main.py` (dentro de `app/`)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from clients.ollama_client import OllamaClient

app = FastAPI()
ollama_client = OllamaClient(base_url="http://ollama:11434")

class Query(BaseModel):
    text: str

@app.post("/embed/")
async def create_embedding(query: Query):
    embedding = await ollama_client.generate_embedding(query.text)
    return {"embedding": embedding}

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

### 4. Arquivo `ollama_client.py` (dentro de `app/clients/`)

```python
import httpx

class OllamaClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def generate_embedding(self, text: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/embed", json={"text": text})
            response.raise_for_status()
            return response.json()["embedding"]
```

### 5. Instruções para Executar

1. **Navegue até o diretório do projeto**:
   ```bash
   cd my_project
   ```

2. **Construa e inicie os serviços**:
   ```bash
   docker-compose up --build
   ```

3. **Teste a API**:
   Após os serviços estarem rodando, você pode enviar uma requisição para criar um embedding. Por exemplo, usando `curl`:

   ```bash
   curl -X POST "http://localhost:8000/embed/" -H "Content-Type: application/json" -d '{"text": "Hello, world!"}'
   ```

### Considerações Finais

- **Modelos**: Certifique-se de que o Ollama está configurado para usar o modelo Llama 3.1. Você pode precisar baixar ou configurar isso diretamente no Ollama.
- **Dependências**: Certifique-se de que todas as dependências estão instaladas corretamente no container do FastAPI.
- **Logs**: Sempre verifique os logs dos containers (`docker-compose logs`) se algo não funcionar como esperado.

Se precisar de mais alguma coisa ou tiver dúvidas, é só avisar!