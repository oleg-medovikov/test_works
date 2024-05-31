from base import db


class Email(db.Model):
    __tablename__ = "email"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)

    @classmethod
    async def get_or_create(cls, email: str):
        obj = await cls.query.where(cls.email == email).gino.first()
        if not obj:
            obj = await cls.create(email=email)
        return obj
