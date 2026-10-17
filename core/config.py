import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_MONGO_URI = "mongodb+srv://Vercel-Admin-Pet-Manager:eKJqcx1LbR6kJwzg@pet-manager.ivylnti.mongodb.net/?retryWrites=true&w=majority"
DEFAULT_DB_NAME = "Pet-Manager"

class Settings(BaseSettings):
    """Settings (lee variables de entorno / .env)"""
    PROJECT_NAME: str = "Pet-Manager API"
    MONGODB_URI: str = DEFAULT_MONGO_URI
    DATABASE_NAME: str = DEFAULT_DB_NAME
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def effective_mongo_uri(self) -> str:
        """Retorna la URI real si .env contiene la plantilla de ejemplo."""
        if "<cluster>" in self.MONGODB_URI or "<usuario>" in self.MONGODB_URI or not self.MONGODB_URI:
            return DEFAULT_MONGO_URI
        return self.MONGODB_URI

    @property
    def effective_db_name(self) -> str:
        if not self.DATABASE_NAME:
            return DEFAULT_DB_NAME
        return self.DATABASE_NAME

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
