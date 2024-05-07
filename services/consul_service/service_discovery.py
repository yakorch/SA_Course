from services.consul_service.service_registration import consul_client
import logging


def discover_service(service_name: str) -> list[dict]:
    _, services = consul_client.health.service(service_name, passing=True)
    return services


def extract_URLs(services: list[dict]) -> list[str]:
    """
    Returns the list of URLs from the services.
    """

    URLs = []

    for service in services:
        if "Service" in service:
            service_details = service["Service"]
            ip_address = service_details["Address"]
            port = service_details["Port"]
            url = f"http://{ip_address}:{port}"
            URLs.append(url)

    logging.info(f"Extracted URLs: {URLs}")

    return URLs
