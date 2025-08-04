from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def criar_tabelas():
    Base.metadata.create_all(bind=engine)

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# ------------------- MODELOS SQLALCHEMY (Banco) -------------------

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Questao(Base):
    __tablename__ = "questoes"

    id = Column(Integer, primary_key=True, index=True)
    enunciado = Column(String, nullable=False)
    alternativas = Column(String, nullable=False)
    correta = Column(Integer, nullable=False)
    disciplina = Column(String, nullable=False)
    assunto = Column(String, nullable=False)
    dificuldade = Column(String, nullable=False)
    ja_respondida = Column(Boolean, default=False)

# ------------------- MODELOS Pydantic (Validação API) -------------------

# Usuários

class UsuarioCriar(BaseModel):
    username: str
    email: str
    password: str

class UsuarioLogin(BaseModel):
    email: str
    password: str

class UsuarioSair(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

# Questões

class QuestaoCrir(BaseModel):
    enunciado: str
    alternativas: List[str]
    correta: int  # índice da alternativa correta (0 a 4)
    disciplina: str
    assunto: str
    dificuldade: str  # Fácil, Médio, Difícil

class QuestaoOut(BaseModel):
    id: int
    enunciado: str
    alternativas: List[str]
    disciplina: str
    assunto: str
    dificuldade: str
    ja_respondida: Optional[bool] = False

    class Config:
        orm_mode = True

# Listas de questões

class ListasQuestoes(BaseModel):
    titulo: str
    questoes_ids: List[int]

# Simulação

class NotaCorteSimulacao(BaseModel):
    curso: str
    campus: str
    nota_usuario: float
