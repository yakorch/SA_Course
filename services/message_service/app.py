import fastapi
from services.message import Message

from services.messaging_queue.mq_consumer import read_messages, start_message_consumer
from services.message_service.messaging_discovery import *


app = fastapi.FastAPI()


start_message_consumer()


@app.get("/messages")
async def get_messages() -> list[str]:
    return read_messages()


@app.get("/health")
async def health_check() -> fastapi.Response:
    return fastapi.Response(content="Messages service is running", status_code=200)
