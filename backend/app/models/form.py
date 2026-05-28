from datetime import datetime

from sqlalchemy import String, DateTime, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.enum import FormType, Status



class FormModel(Base):
    __tablename__ = "formularios"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    dni: Mapped[str] = mapped_column(String(20), nullable=False)
    phone: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, index=True)
    dniImage: Mapped[str] = mapped_column(String(500), nullable=False)
    taxImage: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[Status] = mapped_column(SQLEnum(Status), default=Status.PENDING)
    form_type: Mapped[FormType] = mapped_column(SQLEnum(FormType), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())