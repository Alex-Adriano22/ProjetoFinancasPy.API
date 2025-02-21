from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.Repositorio.Configuracoes import Usuario
from app.Services.Usuario_service import criar_usuario_service, UsuarioValido,reativar_usuario_service, obter_usuario_id_service, atualizar_usuario_service, deletar_usuario_service, listar_usuarios_service
from sqlalchemy.orm import Session

from app.Repositorio.Contexto.Data_Base import get_db






usuario_router = APIRouter()



@usuario_router.post("/usuario")
def criar_usuario (usuario: UsuarioValido, db: Session = Depends(get_db)):
    # teste = Usuario(nome, email, senha)
    return criar_usuario_service(db, usuario)

@usuario_router.get("/listar_usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = listar_usuarios_service(db)
    return jsonable_encoder(usuarios)

@usuario_router.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return obter_usuario_id_service(db, usuario_id)

@usuario_router.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: UsuarioValido, db: Session = Depends(get_db)):
    return atualizar_usuario_service(db, usuario_id, usuario)

@usuario_router.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return deletar_usuario_service(db, usuario_id)

@usuario_router.put("/usuarios/{usuario_id}/reativar")
def reativar_usuario(usuario_id: int, db: Session = Depends(get_db)):  
    return reativar_usuario_service(db, usuario_id)
