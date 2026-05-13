from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from app.models.enum import FormType, Status


class FormRequest(BaseModel):
    name: str
    last_name: str
    dni: str
    phone: str
    email: EmailStr
    dniImage: str
    taxImage: str
    form_type: FormType


class FormResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    last_name: str
    dni: str
    phone: str
    email: EmailStr
    dniImage: str
    taxImage: str
    status: Status
    form_type: FormType
    created_at: datetime


class FormApproval(BaseModel):
    status: Status