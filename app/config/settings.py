import os
from distutils.util import strtobool

from pydantic import BaseSettings


class Base(BaseSettings):
    # Banco de dados
    SQLALCHEMY_DATABASE_URL: str = os.environ["SQLALCHEMY_DATABASE_URL"]
    SQLALCHEMY_ECHO: bool = strtobool(os.getenv("SQLALCHEMY_ECHO", "false"))


class DevSettings(Base):
    ENVIRONMENT = "dev"


class TestSettings(DevSettings):
    ENVIRONMENT = "test"


def _get_settings(env: str) -> BaseSettings:
    envs = {
        "dev": DevSettings(),
        "test": TestSettings(),
    }
    return envs.get(env)


settings = _get_settings(env=os.getenv("ENVIRONMENT", "dev").lower())
