import fastapi
from services.message import Message
from services.endpoints import *
from services.logging_service.logging import log_message, read_messages, clean_logs

app = fastapi.FastAPI()


@app.post("/log")
async def log(message: Message) -> fastapi.Response:
    print(f"Received message: {message}")
    try:
        log_message(message)
    except Exception as e:
        return fastapi.Response(content=f"LOGGER: Failed to log message. Error: {e}", status_code=500)

    return fastapi.Response(content="Message logged", status_code=201)


@app.get("/logs")
async def get_logs() -> list[str]:
    return read_messages()


@app.delete("/logs")
async def delete_logs() -> fastapi.Response:
    try:
        clean_logs()
    except Exception as e:
        return fastapi.Response(content=f"LOGGER: Failed to delete logs. Error: {e}", status_code=500)
    return fastapi.Response(content="Logs deleted", status_code=200)