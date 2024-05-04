import random

FACADE_ENDPOINT = "http://localhost:8000"


LOGGING_ENDPOINTS = [
    "http://localhost:8980",
    "http://localhost:8981",
    "http://localhost:8982",
]


def get_random_logging_endpoint():
    return LOGGING_ENDPOINTS[random.randint(0, 2)]


MESSAGE_ENDPOINTS = [
    "http://localhost:8180",
    "http://localhost:8181",
]


def get_random_message_endpoint():
    return MESSAGE_ENDPOINTS[random.randint(0, 1)]
