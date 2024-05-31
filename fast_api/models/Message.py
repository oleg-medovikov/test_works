from base import db
from datetime import datetime
from sqlalchemy import and_
from typing import Optional


class Message(db.Model):
    __tablename__ = "message"
    __table_args__ = (
        db.PrimaryKeyConstraint("created", "int_id", name="message_id_pk"),
    )

    created = db.Column(db.DateTime)
    int_id = db.Column(db.String(length=16))
    email_id = db.Column(db.Integer, db.ForeignKey("email.id"))
    text_id = db.Column(db.Integer, db.ForeignKey("text.id"))
    size = db.Column(db.Integer, nullable=True)
    id = db.Column(db.String, nullable=True)

    @property
    def email(self):
        """The email property."""
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def text(self):
        """The text property."""
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @classmethod
    async def insert_or_update(
        cls,
        created: datetime,
        int_id: str,
        email_id: int,
        text_id: int,
        size: Optional[int],
        id: Optional[str],
    ):
        obj = await cls.query.where(
            and_(cls.created == created, cls.int_id == int_id)
        ).gino.first()
        if not obj:
            await cls.create(
                created=created,
                int_id=int_id,
                email_id=email_id,
                text_id=text_id,
                size=size,
                id=id,
            )
        else:
            await obj.update(
                cls.email_id == email_id,
                cls.text_id == text_id,
                cls.size == size,
                cls.id == id,
            ).apply()
