import atexit
from services.consul_service.service_registration import (
    register_service,
    consul_cleanup,
)
from services.consul_service.service_discovery import discover_service
from services.consul_service.KV_lookup import get_consul_value
from services.service_names import (
    FACADE_SERVICE_NAME,
    LOGGING_SERVICE_NAME,
    MESSAGE_SERVICE_NAME,
)

register_service(service_name=FACADE_SERVICE_NAME)
atexit.register(lambda: consul_cleanup(service_name=FACADE_SERVICE_NAME))


def discover_logging_services():
    return discover_service(LOGGING_SERVICE_NAME)


def discover_message_services():
    return discover_service(MESSAGE_SERVICE_NAME)
