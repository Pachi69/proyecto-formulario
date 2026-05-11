from fastapi import FastAPI

from app.routers import formulario


app = FastAPI(
    title="API - Formulario de ISP",
    version="1.0.1",
    description="Endpoints accesibles para el rol de usuario y administrador.",
)

app.include_router(formulario.router)