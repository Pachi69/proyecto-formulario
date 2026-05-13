from app.models.form import FormModel
from app.repositories.form import FormRepository
from app.schemas.form import FormRequest, FormApproval

from app.storage.fake_storage import FakeStorage


def create_form(
        form_data: FormRequest,
        repo: FormRepository
) -> FormModel:
    
    return repo.create(form_data)


def get_form_by_email(email: str, repo: FormRepository) -> FormModel | None:
    return repo.get_by_email(email)


def get_by_id(id: int, repo: FormRepository) -> FormModel | None:
    return repo.get(id)

def get_all_by_status(status: str, repo: FormRepository) -> list[FormModel]:
    return repo.get_all_by_status(status)

def get_all(repo: FormRepository) -> list[FormModel] | None:
    return repo.get_all()

def upload_attachment(file, storage: FakeStorage) -> str:
    return storage.upload_file(file)

def update_status(form_id: int, approval: FormApproval, repo: FormRepository) -> FormModel | None:
    return repo.update_status(form_id, approval)