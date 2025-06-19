from pydantic import SecretStr, root_validator
from sqlalchemy import URL

from .base import BaseConfig


class DatabaseConfig(BaseConfig):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    @root_validator(skip_on_failure=True)
    def generate_database_url(cls, v):
        v["DATABASE_URL"] = (
            f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}"
        )
        return v