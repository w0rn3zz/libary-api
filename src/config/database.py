from pydantic import SecretStr, model_validator,  Field
from sqlalchemy import URL

from .base import BaseConfig


class DatabaseConfig(BaseConfig):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    DATABASE_URL: str = Field(default=None)

    @model_validator(mode="before")
    def generate_database_url(cls, values: dict) -> dict:
        values["DATABASE_URL"] = (
            f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@{values['DB_HOST']}:"
            f"{values['DB_PORT']}/{values['DB_NAME']}"
        )
        return values
