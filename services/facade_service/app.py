import fastapi
import uuid
import random
import requests

from services.message import Message

from services.messaging_queue import mq_producer

from services.logging_setup import *

from services.facade_service.facade_discovery import *
from services.consul_service.service_discovery import extract_URLs


app = fastapi.FastAPI()


@app.post("/message")
async def post_message(text: str) -> fastapi.Response:

    message_id = str(uuid.uuid4())
    message_json = {"identifier": message_id, "text": text}
    message = Message(**message_json)

    logging_URLs = extract_URLs(discover_logging_services())

    if not logging_URLs:
        logging.error("Failed to log message. URLs list's empty")
        return fastapi.Response(
            content="FACADE: Failed to log message. URLs list's empty", status_code=500
        )

    chosen_logging_URL = random.choice(logging_URLs)

    logging.info(f"Logging URL chosen: {chosen_logging_URL}")

    logger_response = requests.post(f"{chosen_logging_URL}/log", json=message_json)

    if logger_response.status_code != 201:
        logging.error(
            f"Encountered status code {logger_response.status_code} while logging message: {logger_response.text}"
        )
        return fastapi.Response(
            content="FACADE: Failed to log message", status_code=500
        )

    mq_producer.produce(message)
    logging.info(f"Message {message_json} sent to MQ")

    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/messages")
async def get_messages() -> tuple[list[str], list[str]]:

    messaging_URLs = extract_URLs(discover_message_services())
    chosen_messaging_URL = random.choice(messaging_URLs)

    message_service_response = requests.get(f"{chosen_messaging_URL}/messages")

    if message_service_response.status_code != 200:
        return fastapi.Response(
            content=f"MESSAGES: Failed to get messages {message_service_response.status_code}",
            status_code=500,
        )

    logging_URLs = extract_URLs(discover_logging_services())
    if not logging_URLs:
        logging.error("Failed to get messages. URLs list's empty")
        return fastapi.Response(
            content="FACADE: Failed to get messages. URLs list's empty", status_code=500
        )

    chosen_logging_URL = random.choice(logging_URLs)
    logged_messages_response = requests.get(f"{chosen_logging_URL}/logs", timeout=0.25)
    if logged_messages_response.status_code != 200:
        return fastapi.Response(
            content="LOGGER: Failed to get messages", status_code=500
        )

    return logged_messages_response.json(), message_service_response.json()


@app.get("/health")
async def health_check() -> fastapi.Response:
    return fastapi.Response(content="Facade service is running", status_code=200)
