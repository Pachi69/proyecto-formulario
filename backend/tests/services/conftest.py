import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.repositories.form import FormRepository
from app.schemas.form import FormRequest, FormApproval
from app.models.enum import Status as EnumStatus


engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def repo(db):
    return FormRepository(db)

@pytest.fixture
def valid_form_data(valid_form_request):
    return FormRequest(**valid_form_request)

@pytest.fixture
def valid_form_data2(valid_form_request2):
    return FormRequest(**valid_form_request2)

@pytest.fixture
def form_accepted():
    return FormApproval(status=EnumStatus.ACCEPTED)

@pytest.fixture
def invalid_form_accepted():
    return FormApproval(status=EnumStatus.PENDING)
