from pydantic_settings import BaseSettings
from typing import ClassVar, Dict, Any
from dotenv import load_dotenv 
import os 


## Load environment variables from .env file
class Settings:
    PROJECT_NAME:str = "APP"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")

    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    EMAIL_CONFIG : ClassVar[Dict[str, Any]] = {

        "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
        "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
        "MAIL_FROM": os.getenv("MAIL_FROM"),
        "MAIL_PORT": int(os.getenv("MAIL_PORT", 587)),
        "MAIL_SERVER": os.getenv("MAIL_SERVER"),
        "MAIL_TLS": os.getenv("MAIL_TLS", "True").lower() == "true",
        "MAIL_SSL": os.getenv("MAIL_SSL", "False").lower() == "true",
        "USE_CREDENTIALS": os.getenv("USE_CREDENTIALS", "True").lower() == "true"
    }


settings = Settings()