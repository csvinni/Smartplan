from models import UsuarioCriar, UsuarioLogin, UsuarioSair, QuestaoCrir, QuestaoOut, ListasQuestoes, NotaCorteSimulacao
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

usuarios = []
questoes = []

#   -------------------------------------------------

@router.post("/cadastro", response_model=UsuarioSair)
def cadastrar(usuario: UsuarioCriar):

    if any(u.email == usuario.email for u in usuarios):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    novo_usuario = UsuarioSair(id=len(usuarios)+1, username=usuario.username, email=usuario.email)
    usuarios.append(novo_usuario)
    return novo_usuario

@router.post("/login", response_model=UsuarioSair)
def login(dados: UsuarioLogin):
    for u in usuarios:
        if u.email == dados.email:
            return u
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@router.get("/listar_usuarios", response_model=List[UsuarioSair])
def listar_usuarios():
    return usuarios

#   -------------------------------------------------

@router.post("/criar_questoes", response_model=QuestaoOut)
def criar_questao(q: QuestaoCrir):
    nova = QuestaoOut(id=len(questoes)+1, **q.dict())
    questoes.append(nova)
    return nova

@router.get("/listar_questoes", response_model=List[QuestaoOut])
def listar_questoes(
    disciplina: str = Query(None),
    assunto: str = Query(None),
    dificuldade: str = Query(None),
    respondida: Optional[bool] = Query(None)
):
    resultado = questoes
    if disciplina:
        resultado = [q for q in resultado if q.disciplina == disciplina]
    if assunto:
        resultado = [q for q in resultado if q.assunto == assunto]
    if dificuldade:
        resultado = [q for q in resultado if q.dificuldade == dificuldade]
    if respondida is not None:
        resultado = [q for q in resultado if q.ja_respondida == respondida]
    return resultado

#   -------------------------------------------------

@router.post("/criarsimulado", response_model=List[QuestaoOut])
def criar_simulado(lista: ListasQuestoes):
    return [q for q in questoes if q.id in lista.questoes_ids]

@router.post("/simular")
def simular_nota(sim: NotaCorteSimulacao):
    if sim.nota_usuario >= 750:
        status = "Muito chance de passar"
    elif sim.nota_usuario >= 650:
        status = "Chances medianas"
    else:
        status = "Chances baixas"
    return {
        "curso": sim.curso,
        "campus": sim.campus,
        "nota": sim.nota_usuario,
        "resultado": status
    }

#   -------------------------------------------------
