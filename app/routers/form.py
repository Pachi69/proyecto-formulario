from fastapi import APIRouter, Depends, status
from slqalchemy.orm import Session

from app.database import get_db
from app.repositories.form import FormRepository
from app.schemas.form import FormRequest
from app.services import form as service

router = APIRouter(tags=["Formulario"])


@router.post("/form", status_code=status.HTTP_204_NO_CONTENT)
def create_form(
    form_data: FormRequest,
    db: Session = Depends(get_db)
) -> None:
    
    repo = FormRepository(db)
    service.create_form(form_data, repo)