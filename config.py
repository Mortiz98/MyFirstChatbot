# app/config.py

from dotenv import load_dotenv
from pydantic import BaseSettings, Field
from functools import lru_cache

# Cargar el archivo .env al entorno
load_dotenv()

class Settings(BaseSettings):
    # Info general del proyecto
    APP_NAME: str = Field(default="LangChain FastAPI Chatbot")
    ENVIRONMENT: str = Field(default="development")  # o "production"
    DEBUG: bool = Field(default=True)
    API_VERSION: str = Field(default="v1")

    # Configuración del servidor
    HOST: str = Field(default="127.0.0.1")
    PORT: int = Field(default=8000)

    # Claves de API
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")

    # Configuración opcional de LangChain
    LANGCHAIN_VERBOSE: bool = Field(default=False)

    # (Opcional) Configuración para logging
    LOG_LEVEL: str = Field(default="INFO")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Singleton para usar en cualquier parte
@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
