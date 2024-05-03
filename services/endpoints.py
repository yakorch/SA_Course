import random

FACADE_ENDPOINT = "http://localhost:8000"


LOGGING_ENDPOINTS = [
    "http://localhost:8980",
    "http://localhost:8981",
    "http://localhost:8982",
]

def get_random_logging_endpoint():
    return LOGGING_ENDPOINTS[random.randint(0, 2)]


MESSAGE_ENDPOINT = "http://localhost:8181"
