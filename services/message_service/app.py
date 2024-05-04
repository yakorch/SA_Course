import fastapi
from services.message import Message
from services.messaging_queue.mq_consumer import read_messages, subscribe_to_messages

app = fastapi.FastAPI()


subscribe_to_messages()


@app.get("/messages")
async def get_messages() -> list[str]:
    return read_messages()
