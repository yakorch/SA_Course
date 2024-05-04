import fastapi
from services.message import Message

from services.messaging_queue.mq_consumer import read_messages, start_message_consumer

app = fastapi.FastAPI()


start_message_consumer()


@app.get("/messages")
async def get_messages() -> list[str]:
    return read_messages()
