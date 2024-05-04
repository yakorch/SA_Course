import random

FACADE_ENDPOINT = "http://facade-service:8000"


LOGGING_ENDPOINTS = [
    "http://logging-service-1:8980",
    "http://logging-service-2:8981",
    "http://logging-service-3:8982",
]


def get_random_logging_endpoint():
    return random.choice(LOGGING_ENDPOINTS)


MESSAGE_ENDPOINTS = [
    "http://messages-service-1:8180",
    "http://messages-service-2:8181",
]


def get_random_message_endpoint():
    return random.choice(MESSAGE_ENDPOINTS)
