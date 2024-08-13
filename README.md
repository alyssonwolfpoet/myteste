# myteste

uvicorn main:app --reload

Para testar as rotas do seu API com o Postman, você precisará criar requisições HTTP com os seguintes formatos de JSON:

1. Upload de arquivos (/upload/)

    Método: POST
    Tipo de requisição: multipart/form-data
    Corpo da requisição:
        Adicione um ou mais arquivos como "form-data" com a chave files
        Certifique-se de que o tipo de arquivo esteja correto (por exemplo, application/pdf para PDFs)

Exemplo de requisição no Postman:

    Selecione o método POST e a URL http://localhost:8000/upload/
    Clique em "Body" e selecione "form-data"
    Adicione um arquivo (por exemplo, um PDF) com a chave files
    Clique em "Send"

2. Perguntar sobre um documento (/ask/)

    Método: GET
    Parâmetros de consulta:
        document_id: o ID do documento sobre o qual você deseja fazer uma pergunta (por exemplo, 123)
        question: a pergunta que você deseja fazer sobre o documento (por exemplo, "Qual é o título do documento?")

Exemplo de requisição no Postman:

    Selecione o método GET e a URL http://localhost:8000/ask/?document_id=123&question=Qual%20%C3%A9%20o%20t%C3%ADtulo%20do%20documento?
    Clique em "Send"

3. Gerar um quiz (/generate_quiz/)

    Método: GET
    Parâmetros de consulta:
        document_id: o ID do documento para o qual você deseja gerar um quiz (por exemplo, 123)

Exemplo de requisição no Postman:

    Selecione o método GET e a URL http://localhost:8000/generate_quiz/?document_id=123
    Clique em "Send"

Lembre-se de substituir http://localhost:8000 pela URL do seu servidor FastAPI. Além disso, certifique-se de que os endpoints estejam configurados corretamente no seu arquivo main.py (ou outro arquivo que você esteja usando para configurar o FastAPI).