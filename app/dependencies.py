from app.repositories.formulario import FormularioRepository


_repo = FormularioRepository()

def get_formulario_repo() -> FormularioRepository:
    return _repo