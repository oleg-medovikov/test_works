from datetime import datetime
import os

from models import Message, Email, Text


async def insert_messages(file_path: str):
    if not os.path.isfile(file_path):
        return

    with open(file_path, "r") as file:
        for row in file:
            if "<=" not in row:
                continue

            created = datetime.strptime(row[:19], "%Y-%m-%d %H:%M:%S")
            int_id = row[20:36]
            row = row[40:]
            email_text = row.split(" ", 1)[0]

            if "@" not in email_text:
                continue

            email = await Email.get_or_create(email_text)

            row = row.split(" ", 1)[1]

            try:
                id = row.split("id=", 1)[1]
            except IndexError:
                id = None

            row = row.split("id=", 1)[0]

            try:
                size = row.split("S=", 1)[1]
            except IndexError:
                size = None
            else:
                try:
                    size = int(size)
                except ValueError:
                    size = None

            text = await Text.get_or_create(row.split("S=", 1)[0])

            await Message.insert_or_update(created, int_id, email.id, text.id, size, id)
