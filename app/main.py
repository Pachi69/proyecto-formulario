from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers import form, admin


app = FastAPI(
    title="API - Formulario de ISP",
    version="1.0.1",
    description="Endpoints accesibles para el rol de usuario y administrador.",
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )

app.include_router(form.router)
app.include_router(admin.router)