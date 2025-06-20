from pydantic import BaseModel

from .app import AppConfig
from .database import DatabaseConfig


class Settings(BaseModel):
    app: AppConfig = AppConfig()
    database: DatabaseConfig = DatabaseConfig()


settings = Settings()
