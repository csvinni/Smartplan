from pydantic import BaseModel
from typing import List, Optional

# ------------------------------------

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

# ------------------------------------

class Conteudo(BaseModel):
    nome: str
    disciplina: str  # Ex: Matemática, História

# ---------------------------------

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

# ------------------------------------

class ListasQuestoes(BaseModel):
    titulo: str
    questoes_ids: List[int]

# ------------------------------------

class NotaCorteSimulacao(BaseModel):
    curso: str
    campus: str
    nota_usuario: float
