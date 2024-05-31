import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from typing import List

from base import settings, db

from func import insert_messages
from models import Message, Email, Text


app = FastAPI(title="mail_log_analyse_api")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    # Возвращаем HTML-файл из статической папки
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.on_event("startup")
async def startup_event():
    await db.set_bind(settings.pg_url)
    await db.gino.create_all()
    await insert_messages(settings.file_path)


@app.get("/emails", response_model=List[str])
async def read_emails():
    emails = await Email.query.gino.all()
    return [email.email for email in emails]


class MessageRequest(BaseModel):
    email: str
    page: int
    itemsPerPage: int


class MessageResponse(BaseModel):
    created: str
    text: str
    size: int
    id: str


@app.post("/messages", response_model=List[MessageResponse])
async def read_messages(request: MessageRequest):
    messages = (
        await Message.load(email=Email, text=Text)
        .query.where(Email.email == request.email)
        .order_by(Message.created.desc())
        .gino.all()
    )
    return [
        {"created": str(_.created), "text": _.text.text, "size": _.size, "id": _.id}
        for _ in messages[
            request.itemsPerPage
            * request.page : request.itemsPerPage
            * (request.page + 1)
        ]
    ]


if __name__ == "__main__":
    uvicorn_process = uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8027,
        reload=True,
        workers=2,
    )
