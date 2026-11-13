from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_inicio():
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json()["projeto"] == "Saúde Antes da Emergência"
    assert resposta.json()["mensagem"] == "API atualizada automaticamente pelo GitHub Actions!"


def test_health():
    resposta = client.get("/api/health")

    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ok"
    assert resposta.json()["api"] == "online"
