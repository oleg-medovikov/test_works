import requests
import pandas as pd
from pydantic import BaseModel, Field
from datetime import datetime


# Определяем модель для валидации данных
class Document(BaseModel):
    key1: int = Field(alias="document_id")
    key2: datetime = Field(alias="document_dt")
    key3: str = Field(alias="document_name")


def main():
    to_day = datetime.now()
    to_day = to_day.replace(hour=0, minute=0, second=0, microsecond=0)

    response = requests.get(
        "https://api.gazprombank.ru/very/important/docs?documents_date={to_day.timestamp()}"
    )
    data = response.json()

    # создаем список объектов Document
    documents = [Document(**row) for row in data["Rows"]]

    # не совсем уверен в данном шаге, но вродь из пудантика в пандас напрямую нельзя
    df = pd.DataFrame(data=[doc.dict() for doc in documents])
    # Переименовываем столбцы
    df.rename(
        columns={"key1": "document_id", "key2": "document_dt", "key3": "document_name"},
        inplace=True,
    )

    # Добавляем столбец с текущей датой и временем
    df["load_dt"] = datetime.now()

    print(df)


if __name__ == "__main__":
    main()
