from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, AnyUrl
from app.models.enum import FormType, Status


class FormRequest(BaseModel):
    name: str
    last_name: str
    dni: str
    phone: str
    email: EmailStr
    dniImage: AnyUrl
    taxImage: AnyUrl
    form_type: FormType


class FormResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    last_name: str
    dni: str
    phone: str
    email: EmailStr
    dniImage: AnyUrl
    taxImage: AnyUrl
    status: Status
    form_type: FormType
    created_at: datetime


class FormApproval(BaseModel):
    status: Status