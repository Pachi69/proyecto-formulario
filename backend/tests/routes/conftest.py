import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from datetime import datetime

from app.main import app
from app.database import get_db, get_storage
from app.storage.fake_storage import FakeStorage
from app.models import FormModel
from app.models.enum import Status as EnumStatus, FormType


@pytest.fixture
def client():
    app.dependency_overrides[get_db] = lambda: MagicMock()
    app.dependency_overrides[get_storage] = lambda: FakeStorage()
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture
def mock_form():
    return FormModel(
        id=1,
        name="Tupu",
        last_name="Tamadre",
        dni="12345678",
        phone="1144556677",
        email="tupu@tamadre.com",
        dniImage="https://example.com/dni.jpg",
        taxImage="https://example.com/tax.jpg",
        status=EnumStatus.PENDING,
        form_type=FormType.REGISTER,
        created_at=datetime.now(),
    )

@pytest.fixture
def mock_form_accepted():
    return FormModel(
        id=1,
        name="Tupu",
        last_name="Tamadre",
        dni="12345678",
        phone="1144556677",
        email="tupu@tamadre.com",
        dniImage="https://example.com/dni.jpg",
        taxImage="https://example.com/tax.jpg",
        status=EnumStatus.ACCEPTED,
        form_type=FormType.REGISTER,
        created_at=datetime.now(),
    )

@pytest.fixture
def mock_form2():
    return FormModel(
        id=2,
        name="Tupu",
        last_name="Tamadre",
        dni="12345678",
        phone="1144556677",
        email="tupu@tamadre2.com",
        dniImage="https://example.com/dni.jpg",
        taxImage="https://example.com/tax.jpg",
        status=EnumStatus.PENDING,
        form_type=FormType.REGISTER,
        created_at=datetime.now(),
    )


@pytest.fixture
def mock_fake_url():
    return "https://fake-url.com/file.jpg"