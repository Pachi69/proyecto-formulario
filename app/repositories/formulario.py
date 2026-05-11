from app.schemas import Formulario


class FormularioRepository:
    def __init__(self):
        self._data: dict[int, Formulario] = {}
        self._next_id: int = 1

    def create(self, formulario: Formulario) -> Formulario:
        self._data[formulario.id] = formulario
        return formulario
    
    def get(self, id: int) -> Formulario | None:
        return self._data.get(id)
    
    def get_by_email(self, email: str) -> Formulario | None:
        for f in self._data.values():
            if f.email == email:
                return f
        return None
    
    def list(self) -> list[Formulario]:
        return list(self._data.values())
    

    def next_id(self) -> int:
        current = self._next_id
        self._next_id += 1
        return current