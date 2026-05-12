import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.main import app
from app.database import Base, get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)

    connection = TestingSessionLocal()

    try:
        yield connection
    finally:
        connection.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):

    app.dependency_overrides[get_db] = lambda: db

    yield TestClient(app)

    app.dependency_overrides.clear()


@pytest.fixture
def valid_form_request():
    return {
        "name": "Tupu",
        "last_name": "Tamadre",
        "dni": "12345678",
        "phone": "1144556677",
        "email": "tupu@tamadre.com",
        "dniImage": "https://example.com/dni.jpg",
        "taxImage": "https://example.com/tax.jpg",
        "form_type": "Alta",
    }