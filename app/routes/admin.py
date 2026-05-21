from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.form import FormRepository
from app.schemas.form import FormResponse, FormApproval
from app.models.form import FormModel
from app.services import form as service
from app.models.enum import Status

router = APIRouter(tags=["Admin"], prefix="/admin")


@router.get("/forms/{id}", status_code=status.HTTP_200_OK, response_model=FormResponse)
def get_by_id(id: int, db: Session = Depends(get_db)) -> FormModel:
    repo = FormRepository(db)
    response = service.get_by_id(id, repo)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Formulario no encontrado")
    return response


@router.get("/forms", status_code=status.HTTP_200_OK, response_model=list[FormResponse])
def get_all(status_filter: Status | None = None, db: Session = Depends(get_db)) -> list[FormModel]:
    repo = FormRepository(db)

    if status_filter:
        response = service.get_all_by_status(status_filter, repo)
        if not response:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Formularios no encontrados")
    else:
        response = service.get_all(repo)
        if not response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Formularios no encontrados")
    
    return response


@router.patch("/forms/{id}/approve", status_code=status.HTTP_200_OK, response_model=FormResponse)
def approve(id: int, approve: FormApproval, db: Session = Depends(get_db)) -> FormModel:
    repo = FormRepository(db)
    response = service.update_status(id, approve, repo)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Formulario no encontrado")
    return response
    