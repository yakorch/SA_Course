import consul
import os
import atexit


def read_consul_address():
    host = os.getenv("CONSUL_HOST")
    port = int(os.getenv("CONSUL_PORT"))
    return {"host": host, "port": port}


def get_consul_client():
    return consul.Consul(**read_consul_address(), scheme="http")


def get_service_identifier(service_name: str):
    return f"{service_name} | {os.getenv('PORT')}"


def register_service(service_name: str) -> None:
    """
    `PORT` is assumed to be an env. variable. Can be set in the Dockerfile.
    """
    consul_client = get_consul_client()
    service_id = get_service_identifier(service_name)
    service_port = int(os.getenv("PORT"))

    # service name is routed to service IP thanks to Docker's internal DNS
    service_address = service_name

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
    consul_client = get_consul_client()
    consul_client.agent.service.deregister(
        service_id=get_service_identifier(service_name)
    )

