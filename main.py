from fastapi import FastAPI
from views import router as views_router
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do arquivo .env

app = FastAPI()

# Incluindo as rotas definidas em views
app.include_router(views_router)