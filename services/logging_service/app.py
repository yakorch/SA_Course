import fastapi
from services.message import Message
from services.endpoints import *


app = fastapi.FastAPI()

logged_messages = []

@app.post("/log")
async def log(message: Message):
    logged_messages.append(message)
    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/logs")
async def get_logs() -> list[Message]:
    return logged_messages
