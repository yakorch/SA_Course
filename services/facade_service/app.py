import fastapi
import uuid
import requests
from services.message import Message
from services.endpoints import *


app = fastapi.FastAPI()


@app.post("/message")
async def post_message(text: str) -> fastapi.Response:

    message_id = str(uuid.uuid4())

    response = requests.post(f"{get_random_logging_endpoint()}/log", json={"identifier": message_id, "text": text})
    if response.status_code != 201:
        print(f"Encountered status code {response.status_code} while logging message: {response.text}")
        return fastapi.Response(content="FACADE: Failed to log message", status_code=500)
    
    # TODO: send the message to the messages service
    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/messages")
async def get_messages() -> list[str]:
    # TODO: read the messages from the messages service properly
    message_service_response = requests.get(f"{get_random_message_endpoint()}/message")

    if message_service_response.status_code != 200:
        return fastapi.Response(content="Failed to get messages", status_code=500)
    
    logged_messages_response = requests.get(f"{get_random_logging_endpoint()}/logs")
    if logged_messages_response.status_code != 200:
        return fastapi.Response(content="Failed to get messages", status_code=500)
    
    all_messages = [*logged_messages_response.json(), message_service_response.json()["text"]]

    return all_messages
