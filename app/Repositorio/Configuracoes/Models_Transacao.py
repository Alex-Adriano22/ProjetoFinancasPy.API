from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.Repositorio.Contexto.Data_Base import Base


class Transacoes(Base):
    __tablename__ = "Transacoes"  

    TransacoesId = Column(Integer, primary_key=True, autoincrement=True)  
    tipo = Column(String)  
    valor = Column(Float) 
    descricao = Column(String) 
    ativo = Column(Boolean, default=True)


    usuario_id = Column(Integer, ForeignKey('Usuario.UsuarioId'))  

    # def __init__(self, tipo, valor, descricao):
    #     self.tipo = tipo,
    #     self.valor = valor
    #     self.descricao = descricao
    #     self.ativo = True
        
   
    usuario = relationship("Usuario", backref="transacoes")  