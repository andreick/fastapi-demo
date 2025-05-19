from functools import lru_cache

from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = "db"
    db_port: int = 5432
    db_name: str = "demo"
    db_user: str = "postgres"
    db_password: str = "postgres"

    @property
    def database_url(self) -> str:
        url = MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_name,
        )
        return str(url)

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
