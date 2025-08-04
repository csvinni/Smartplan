from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import json

from models import UsuarioCriar, UsuarioLogin, UsuarioSair, QuestaoCrir, QuestaoOut, ListasQuestoes, NotaCorteSimulacao
from models import Usuario, Questao
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------- USUÁRIOS ----------------------------

@router.post("/cadastro", response_model=UsuarioSair)
def cadastrar(usuario: UsuarioCriar, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    novo_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        password=usuario.password
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return UsuarioSair(id=novo_usuario.id, username=novo_usuario.username, email=novo_usuario.email)

@router.post("/login", response_model=UsuarioSair)
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return UsuarioSair(id=usuario.id, username=usuario.username, email=usuario.email)

@router.get("/listar_usuarios", response_model=List[UsuarioSair])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

# ---------------------- QUESTÕES ---------------------------

@router.post("/criar_questoes", response_model=QuestaoOut)
def criar_questao(q: QuestaoCrir, db: Session = Depends(get_db)):
    nova = Questao(
        enunciado=q.enunciado,
        alternativas=json.dumps(q.alternativas), 
        correta=q.correta,
        disciplina=q.disciplina,
        assunto=q.assunto,
        dificuldade=q.dificuldade,
        ja_respondida=False
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)

    return QuestaoOut(
        id=nova.id,
        enunciado=nova.enunciado,
        alternativas=json.loads(nova.alternativas),
        disciplina=nova.disciplina,
        assunto=nova.assunto,
        dificuldade=nova.dificuldade,
        ja_respondida=nova.ja_respondida
    )

@router.get("/listar_questoes", response_model=List[QuestaoOut])
def listar_questoes(
    disciplina: str = Query(None),
    assunto: str = Query(None),
    dificuldade: str = Query(None),
    respondida: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Questao)
    if disciplina:
        query = query.filter(Questao.disciplina == disciplina)
    if assunto:
        query = query.filter(Questao.assunto == assunto)
    if dificuldade:
        query = query.filter(Questao.dificuldade == dificuldade)
    if respondida is not None:
        query = query.filter(Questao.ja_respondida == respondida)

    questoes = query.all()
    return [
        QuestaoOut(
            id=q.id,
            enunciado=q.enunciado,
            alternativas=json.loads(q.alternativas),
            disciplina=q.disciplina,
            assunto=q.assunto,
            dificuldade=q.dificuldade,
            ja_respondida=q.ja_respondida
        )
        for q in questoes
    ]

# ---------------------- SIMULADO ---------------------------

@router.post("/criarsimulado", response_model=List[QuestaoOut])
def criar_simulado(lista: ListasQuestoes, db: Session = Depends(get_db)):
    questoes = db.query(Questao).filter(Questao.id.in_(lista.questoes_ids)).all()
    return [
        QuestaoOut(
            id=q.id,
            enunciado=q.enunciado,
            alternativas=json.loads(q.alternativas),
            disciplina=q.disciplina,
            assunto=q.assunto,
            dificuldade=q.dificuldade,
            ja_respondida=q.ja_respondida
        )
        for q in questoes
    ]

@router.post("/simular")
def simular_nota(sim: NotaCorteSimulacao):
    if sim.nota_usuario >= 750:
        status = "Muita chance de passar"
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
