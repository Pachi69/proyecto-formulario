from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db, get_storage
from app.repositories.form import FormRepository
from app.schemas.form import FormRequest, FormResponse
from app.models.form import FormModel
from app.services import form as service

router = APIRouter(tags=["Formulario"])


@router.post("/form", status_code=status.HTTP_204_NO_CONTENT)
def create_form(
    form_data: FormRequest,
    db: Session = Depends(get_db)
):
    repo = FormRepository(db)
    service.create_form(form_data, repo)


@router.get("/form/user/{userEmail}", status_code=status.HTTP_200_OK, response_model=FormResponse)
def get_form_by_email(userEmail: str, db: Session = Depends(get_db)) -> FormModel:
    repo = FormRepository(db)
    response = service.get_form_by_email(userEmail, repo)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Formulario no encontrado")
    
    return response

@router.post("/form/attachment", status_code=status.HTTP_200_OK)
def upload_file(image: UploadFile = File(...), storage = Depends(get_storage)) -> str:
    
    allowed_types = ["image/jpeg", "image/png"]
    
    if image.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten archivos JPEG, PNG"
        )
    
    response = service.upload_attachment(image, storage)
    return response