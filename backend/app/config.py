from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    database_url: str
    db_user: str
    db_password: str
    db_name: str
    environment: str = "development"
    port: int = 8000

    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", extra="ignore")

settings = Settings()