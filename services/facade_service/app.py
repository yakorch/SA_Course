import fastapi
import uuid
import requests
from services.message import Message
from services.endpoints import *

app = fastapi.FastAPI()


@app.post("/message")
async def post_message(text: str):

    message_id = str(uuid.uuid4())

    response = requests.post(f"{LOGGING_ENDPOINT}/log", json={"identifier": message_id, "text": text})
    if response.status_code != 201:
        return fastapi.Response(content="Failed to log message", status_code=500)
    
    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/messages")
async def get_messages() -> list[Message]:
    message_service_response = requests.get(f"{MESSAGE_ENDPOINT}/message")

    if message_service_response.status_code != 200:
        return fastapi.Response(content="Failed to get messages", status_code=500)
    
    logged_messages_response = requests.get(f"{LOGGING_ENDPOINTS[0]}/logs")
    if logged_messages_response.status_code != 200:
        return fastapi.Response(content="Failed to get messages", status_code=500)
    
    all_messages = [*logged_messages_response.json(), message_service_response.json()]

    return [Message(**message) for message in all_messages]
