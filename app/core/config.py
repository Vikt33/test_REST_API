from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
from pathlib import Path

# Определяем базовый путь
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Загружаем .env из корня проекта
env_path = BASE_DIR / '.env'
if env_path.exists():
    print(f"Loading .env from {env_path}")
    load_dotenv(env_path)
else:
    print(f".env file not found at {env_path}")

class Settings(BaseSettings):
    API_KEY: str = Field("default_secret_key", env="API_KEY")
    DATABASE_URL: str = Field(
        "postgresql+asyncpg://user:password@localhost/dbname",
        env="DATABASE_URL"
    )
    DEBUG: bool = False

settings = Settings()