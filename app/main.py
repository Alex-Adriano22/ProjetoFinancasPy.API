from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Api.Usuario_Api import usuario_router
from app.Api.Transacao_Api import transacao_router
from app.Repositorio.Contexto.Data_Base import criar_tabelas

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

criar_tabelas()

app.include_router(usuario_router)
app.include_router(transacao_router)