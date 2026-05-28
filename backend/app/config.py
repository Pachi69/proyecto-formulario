from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    db_user: str
    db_password: str
    db_name: str
    environment: str = "development"
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()