from pydantic import BaseModel
import uuid


class Message(BaseModel):
    text: str
    identifier: str
