from fastapi import FastAPI
from models import criar_tabelas
from api import router

app = FastAPI()

criar_tabelas() 

app.include_router(router)
