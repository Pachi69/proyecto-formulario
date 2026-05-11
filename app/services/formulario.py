from app.repositories.formulario import FormularioRepository
from app.schemas import Formulario, Estado, FormularioSolicitud


def create_formulario(
        solicitud: FormularioSolicitud,
        repo: FormularioRepository
) -> Formulario:
    formulario = Formulario(
        id=repo.next_id(),
        estado=Estado.PENDIENTE,
        **solicitud.model_dump(),
    )
    return repo.create(formulario)