from dotenv import main
from dataclasses import dataclass
from os import getenv


# файл конфигурации
main.load_dotenv(".conf")


@dataclass
class Settings:
    pg_url: str
    file_path: str
    SSL_KEYFILE: str
    SSL_CERTFILE: str


settings = Settings(
    pg_url=getenv("PG_URL", default=""),
    file_path=getenv("FILE_PATH", default=""),
    SSL_KEYFILE=getenv("SSL_KEYFILE", default=""),
    SSL_CERTFILE=getenv("SSL_CERTFILE", default=""),
)
