from dotenv import main
from dataclasses import dataclass
from os import getenv


# файл конфигурации
main.load_dotenv(".conf")


@dataclass
class Settings:
    pg_url: str
    file_path: str


settings = Settings(
    pg_url=getenv("PG_URL", default=""),
    file_path=getenv("FILE_PATH", default=""),
)
