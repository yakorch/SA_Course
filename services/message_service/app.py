import fastapi
from services.message import Message


app = fastapi.FastAPI()


@app.get("/message")
async def root() -> Message:
    return Message(text="A boring message.", identifier="00000000-0000-0000-0000-000000000000")
