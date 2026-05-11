import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_formulario_repo
from app.main import app
from app.repositories.formulario import FormularioRepository


@pytest.fixture
def repo():
    return FormularioRepository()

@pytest.fixture
def client(repo):
    app.dependency_overrides[get_formulario_repo] = lambda: repo    
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture
def solicitud_valida():
    return {
        "nombre": "Tupu",
        "apellido": "Tamadre",
        "dni": "12345678",
        "telefono": "1144556677",
        "email": "tupu@tamadre.com",
        "dniImage": "https://example.com/dni.jpg",
        "taxImage": "https://example.com/tax.jpg",
        "tipo": "Alta",
    }