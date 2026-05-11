from enum import Enum
from pydantic import BaseModel, EmailStr, AnyUrl


class Tipo(str, Enum):
    ALTA = "Alta"
    BAJA = "Baja"

class Estado(str, Enum):
    PENDIENTE = "Pendiente"
    ACEPTADO = "Aceptado"
    RECHAZADO = "Rechazado"

class EstadoAprobacion(str, Enum):
    ACEPTADO = "Aceptado"
    RECHAZADO = "Rechazado"

class Formulario(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    telefono: str
    email: EmailStr
    dniImage: AnyUrl
    taxImage: AnyUrl
    tipo: Tipo
    estado: Estado

class FormularioAprobacion(BaseModel):
    estado: EstadoAprobacion


class FormularioSolicitud(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    email: EmailStr
    dniImage: AnyUrl
    taxImage: AnyUrl
    tipo: Tipo