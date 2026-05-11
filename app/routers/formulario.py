from fastapi import APIRouter, Depends, status

from app.dependencies import get_formulario_repo
from app.repositories.formulario import FormularioRepository
from app.schemas import FormularioSolicitud
from app.services import formulario as service

router = APIRouter(tags=["Formulario"])


@router.post("/formulario", status_code=status.HTTP_204_NO_CONTENT)
def enviar_formulario(
    solicitud: FormularioSolicitud,
    repo: FormularioRepository = Depends(get_formulario_repo),
) -> None:
    service.create_formulario(solicitud, repo)