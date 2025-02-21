from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

string_conexao = "mssql+pyodbc://DESKTOP-58UEHOH\\SQLEXPRESS02/BancoPy?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

conexao_banco = create_engine(string_conexao, connect_args={"trust_host": "yes"}) # confiança trust, yes

Base = declarative_base()

secao_banco = sessionmaker(autocommit = False, autoflush=False, bind=conexao_banco)

def criar_tabelas():
 Base.metadata.create_all(bind=conexao_banco)


def get_db():
    db = secao_banco()
    try:
        yield db # permito que outras funções usem essa sessão 

        #motivo de yield gerencia a conexão automaticamente e feche ao inves do return
    finally:
        db.close()
        
try:
    conexao_banco.connect()
    print("Conectado ao banco")
except Exception as e:
    print(f"Erro ao conectar {e}")