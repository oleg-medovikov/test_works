from base import db


class Text(db.Model):
    __tablename__ = "text"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)

    @classmethod
    async def get_or_create(cls, text: str):
        obj = await cls.query.where(cls.text == text).gino.first()
        if not obj:
            obj = await cls.create(text=text)
        return obj
