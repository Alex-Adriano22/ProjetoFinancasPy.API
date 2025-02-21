from app.Repositorio.Configuracoes.Models_Usuario import Usuario
from pydantic import BaseModel
from sqlalchemy.orm import Session


class UsuarioValido(BaseModel):
    nome: str
    email: str
    


def criar_usuario_service(db: Session, usuario: UsuarioValido):
    usuario = Usuario(nome= usuario.nome, email = usuario.email)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"Usuario cirado com sucesso " }

def listar_usuarios_service(db: Session):
    usuarios = db.query(Usuario.nome, Usuario.email).filter(Usuario.ativo == True).all()

    return [{"nome": nome, "email": email} for nome, email in usuarios]

def obter_usuario_id_service(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.UsuarioId == usuario_id).first()
    if not usuario:
        return{"error": "Usuario não econtrado"}
    return usuario

def atualizar_usuario_service(db: Session, usuario_id: int, usuario: UsuarioValido):
    usuario = db.query(Usuario).filter(Usuario.UsuarioId == usuario_id).first()
    if not usuario:
        return{"error": "Usuario não econtrado"}
                
    
    usuario.Nome = usuario.Nome
    usuario.email = usuario.email
    
    db.commit()
    db.refresh(usuario)

    return {"message": "Usuário atualizado com sucesso"}

def deletar_usuario_service(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.UsuarioId == usuario_id).first()
    if not usuario:
      return {"error": "Usuario não econtrado"}
    
    usuario.ativo = False
    db.commit()
    return {"message": "Usuário desativado com sucesso"}

def reativar_usuario_service(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.UsuarioId == usuario_id).firt()
    if not usuario:
      return {"error": "Usuario não econtrado"}
    
    usuario.ativo = True
    db.commit()
    return {"message": "Usuário desativado com sucesso"}