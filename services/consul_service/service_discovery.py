from services.consul_service.service_registration import consul_client


def discover_service(service_name: str):
    return consul_client.catalog.service(service_name)
