from app.models.form import FormModel
from app.repositories.form import FormRepository
from app.schemas.form import FormRequest


def create_form(
        form_data: FormRequest,
        repo: FormRepository
) -> FormModel:
    
    return repo.create(form_data)