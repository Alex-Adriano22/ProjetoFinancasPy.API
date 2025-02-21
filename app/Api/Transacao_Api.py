from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from enum import Enum
from app.Repositorio.Contexto.Data_Base import get_db
from app.Services.Transação_service import (
    criar_transacao_service,
    listar_transacoes_service,
    atualizar_transacao_service,
    deletar_transacao_service,
    reativar_transacao_service
)
from app.Services.Transação_service import transacaoValida


class tipotransacao(str, Enum):
    DESPESA = "despesa"
    RECEITA = "receita"

transacao_router = APIRouter()

@transacao_router.post("/")
def criar_transacao(transacao: transacaoValida, db: Session = Depends(get_db)):
    if transacao.tipo not in tipotransacao.__members__.values():
        return {"error": "Tipo de transação inválido. Use 'despesa' ou 'receita'."}
    return criar_transacao_service(db, transacao)

@transacao_router.get("/listar_transacao")
def listar_transacoes(db: Session = Depends(get_db)):
    return listar_transacoes_service(db)

# @transacao_router.get("/{transacao_id}", )
# def obter_transacao(transacao_id: int, db: Session = Depends(get_db)):
#     return obter_transacao_id_service(db, transacao_id)

@transacao_router.put("/atualizar_transacao/{transacao_id}" )
def atualizar_transacao(transacao_id: int, transacao: transacaoValida, db: Session = Depends(get_db)):
    return atualizar_transacao_service(db, transacao_id, transacao)

@transacao_router.delete("/deletar_transacao/{transacao_id}" )
def deletar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    return deletar_transacao_service(db, transacao_id)

@transacao_router.put("/reativar-transacao/{transacao_id}" )
def reativar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    return reativar_transacao_service(db, transacao_id)
