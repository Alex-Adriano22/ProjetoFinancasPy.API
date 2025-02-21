from app.Repositorio.Configuracoes.Models_Transacao import Transacoes
from pydantic import BaseModel
from enum import Enum
from sqlalchemy.orm import Session


class transacaoValida(BaseModel):
    tipo: str
    valor: float
    descricao: str
    

def criar_transacao_service(db: Session,  transaocao: transacaoValida):
    nova_transacao = Transacoes(
        tipo = transaocao.tipo,
        valor = transaocao.valor,
        descricao = transaocao.descricao
    )
    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)

    return {"message": "Transação criada com sucesso"}
def listar_transacoes_service(db: Session):
    transacoes = db.query(Transacoes).filter(Transacoes.ativo == True).all()
    return [{"id": t.id, "tipo": t.tipo, "valor": t.valor, "descricao": t.descricao, "data": t.data} for t in transacoes]

def atualizar_transacao_service(db: Session, transacao_id: int, transacao: transacaoValida):
    transacao_db = db.query(Transacoes).filter(Transacoes.id == transacao_id).first()
    if not transacao_db:
        return {"error": "Transação não encontrada"}
    
    transacao_db.tipo = transacao.tipo
    transacao_db.valor = transacao.valor
    transacao_db.descricao = transacao.descricao
    transacao_db.data = transacao.data
    
    db.commit()
    db.refresh(transacao_db)
    return {"message": "Transação atualizada com sucesso"}

def deletar_transacao_service(db: Session, transacao_id: int):
    transacao = db.query(Transacoes).filter(Transacoes.id == transacao_id).first()
    if not transacao:
        return {"error": "Transação não encontrada"}
    
    transacao.ativo = False
    db.commit()
    return {"message": "Transação desativada com sucesso"}

def reativar_transacao_service(db: Session, transacao_id: int):
    transacao = db.query(Transacoes).filter(Transacoes.id == transacao_id).first()
    if not transacao:
        return {"error": "Transação não encontrada"}
    
    transacao.ativo = True
    db.commit()
    return {"message": "Transação reativada com sucesso"}
