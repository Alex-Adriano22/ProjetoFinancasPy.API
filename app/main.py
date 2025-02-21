from fastapi import FastAPI
from app.Api.Usuario_Api import usuario_router
from app.Api.Transacao_Api import transacao_router
from app.Repositorio.Contexto.Data_Base import criar_tabelas

app = FastAPI()

criar_tabelas()

app.include_router(usuario_router)
app.include_router(transacao_router)