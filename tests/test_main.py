import sys
import os
from fastapi.testclient import TestClient
from main import app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

client = TestClient(app)

def test_bola8():
    pergunta = "Vou passar de semestre?"
    response = client.get("/bola8", params={"pergunta": pergunta})
    data = response.json()
    assert response.status_code == 200
    assert "pergunta" in data
    assert "resposta" in data
    assert data["pergunta"] == pergunta

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_teste1():
    response = client.get("/teste1")
    data = response.json()
    assert response.status_code == 200
    assert "num_aleatorio" in data
    assert isinstance(data["num_aleatorio"], int)
    assert data["teste"] is True

def test_cadastro_estudante():
    estudante = {
        "name": "Victor",
        "curso": "ADS",
        "ativo": True
    }
    response = client.post("/estudantes/cadastro", json=estudante)
    assert response.status_code == 200
    assert response.json() == estudante

def test_update_estudante_valido():
    response = client.put("/estudantes/update/1")
    assert response.status_code == 200
    assert response.json() is True
