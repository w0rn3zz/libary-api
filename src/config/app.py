from .base import BaseConfig


class AppConfig(BaseConfig):
    SECRET_KEY: str
    ALGORITHM: str
