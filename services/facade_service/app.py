import fastapi
import uuid
import requests
from services.message import Message
from services.endpoints import *

from services.messaging_queue import mq_producer
from services.logging_setup import *

app = fastapi.FastAPI()


@app.post("/message")
async def post_message(text: str) -> fastapi.Response:

    message_id = str(uuid.uuid4())

    message_json = {"identifier": message_id, "text": text}
    message = Message(**message_json)

    logger_response = requests.post(
        f"{get_random_logging_endpoint()}/log", json=message_json
    )
    if logger_response.status_code != 201:
        logging.error(
            f"Encountered status code {logger_response.status_code} while logging message: {logger_response.text}"
        )
        return fastapi.Response(
            content="FACADE: Failed to log message", status_code=500
        )

    mq_producer.produce(message)
    logging.info(f"Message {message} sent to MQ")

    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/messages")
async def get_messages() -> tuple[list[str], list[str]]:
    message_service_response = requests.get(f"{get_random_message_endpoint()}/messages")

    if message_service_response.status_code != 200:
        return fastapi.Response(
            content=f"MESSAGES: Failed to get messages {message_service_response.status_code}",
            status_code=500,
        )

    logged_messages_response = requests.get(f"{get_random_logging_endpoint()}/logs")
    if logged_messages_response.status_code != 200:
        return fastapi.Response(
            content="LOGGER: Failed to get messages", status_code=500
        )

    return logged_messages_response.json(), message_service_response.json()
