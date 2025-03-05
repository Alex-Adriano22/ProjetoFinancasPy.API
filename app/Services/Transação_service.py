from app.Repositorio.Configuracoes.Models_Transacao import Transacoes
from app.Repositorio.Configuracoes.Models_Usuario import Usuario
from pydantic import BaseModel
from fastapi import  HTTPException
from enum import Enum
from sqlalchemy.orm import Session


class transacaoValida(BaseModel):
    tipo: str
    valor: float
    descricao: str
    
 
    

def criar_transacao_service(usuario_id: int, db: Session, transacao: transacaoValida):
    # Busca o usuário pelo ID
    usuario = db.query(Usuario).filter(Usuario.UsuarioId == usuario_id).first()

    # Verifica se o usuário existe
    if not usuario:
        raise HTTPException( detail="Usuário não encontrado")


    nova_transacao = Transacoes(
        tipo=transacao.tipo,
        valor=transacao.valor,
        descricao=transacao.descricao,
        usuario_id=usuario_id
    )

   
    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)

    
    return nova_transacao


def listar_transacoes_service(db: Session):
    transacoes = db.query(Transacoes).filter(Transacoes.ativo == True).all()
    return transacoes


def atualizar_transacao_service(transacao_id: int, db: Session, transacao: transacaoValida):
   
    transacaoAtualizada = db.query(Transacoes).filter(Transacoes.TransacoesId == transacao_id).first()  # Verifique o nome do atributo (id ou TransacoesId)
    

    if not transacaoAtualizada:
        raise HTTPException( detail="Transação não encontrada")

  
    if transacao.tipo not in ["despesa", "receita"]:
        raise HTTPException( detail="Tipo de transação inválido. Use 'despesa' ou 'receita'.")

  
    transacaoAtualizada.tipo = transacao.tipo
    transacaoAtualizada.valor = transacao.valor
    transacaoAtualizada.descricao = transacao.descricao

   
    db.commit()
    db.refresh(transacaoAtualizada)

  
    return transacaoAtualizada

def deletar_transacao_service(db: Session, transacao_id: int):
    transacao = db.query(Transacoes).filter(Transacoes.TransacoesId == transacao_id).first()
    if not transacao:
        return {"error": "Transação não encontrada"}
    
    transacao.ativo = False
    db.commit()
    return {"message": "Transação desativada com sucesso"}

def reativar_transacao_service(db: Session, transacao_id: int):
    transacao = db.query(Transacoes).filter(Transacoes.TransacoesId == transacao_id).first()
    if not transacao:
        return {"error": "Transação não encontrada"}
    
    transacao.ativo = True
    db.commit()
    return {"message": "Transação reativada com sucesso"}
