from sqlalchemy import Column, Integer, String, Boolean
from app.Repositorio.Contexto.Data_Base import Base

class Usuario(Base):
    __tablename__ = "Usuario"
    
    UsuarioId = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    senha = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)

    # def __init__(self, nome, email, senha):
    #     self.nome = nome,
    #     self.email = email
    #     self.senha = senha
    #     self.ativo = True