from services.consul_service.consul_connection import consul_client

import os
import socket


def get_service_identifier(service_name: str):
    """
    Pair (`service_name`, `IP address`) is unique.
    """
    host = socket.gethostname()
    return f"{service_name} | {host}"


def register_service(service_name: str) -> None:
    """
    `PORT` is assumed to be an env. variable. Can be set in the Dockerfile.
    """
    service_id = get_service_identifier(service_name)
    service_port = int(os.getenv("PORT"))

    service_address = socket.gethostname()

    consul_client.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=service_address,
        port=service_port,
        check={
            "http": f"http://{service_address}:{service_port}/health",
            "interval": "5s",
            "timeout": "1s",
        },
    )


def consul_cleanup(service_name: str):
    consul_client.agent.service.deregister(
        service_id=get_service_identifier(service_name)
    )
