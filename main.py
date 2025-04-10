import random
from fastapi import FastAPI
import random

from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


#127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}


#127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    numero_aleatorio = random.randint(1, 100000)
    return {
        "teste": True,
        "num_aleatorio": numero_aleatorio
    }


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante


@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0


@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

@app.get("/bola8")
async def bola_magica(pergunta: str = ""):
    respostas = [
        "Sim, com certeza!",
        "Não conte com isso.",
        "Pergunte novamente mais tarde.",
        "As chances são boas.",
        "Definitivamente não.",
        "Pode apostar nisso!",
        "Ainda é incerto.",
        "Sim, mas se esforce!"
    ]
    return {
        "pergunta": pergunta,
        "resposta": random.choice(respostas)
    }