from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()



class Settings(BaseSettings):
    # Основные настройки


    # Настройки бота
    BOT_TOKEN: str = os.getenv("BOT_TOKEN") # Токен бота
    ADMINS: int = os.getenv("ADMINS") # ID администраторов
    CHANEL: str = os.getenv("CHANEL") # ID канал !!! в будущем список по регионам

    # Настройки базы данных
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10

    @property
    def DATABASE_URL_ASYNC(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_SYNC(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

Config = Settings()
