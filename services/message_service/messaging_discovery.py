import atexit
from services.consul_service.service_registration import (
    register_service,
    consul_cleanup,
)
from services.consul_service.service_discovery import discover_service

from services.service_names import (
    MESSAGE_SERVICE_NAME,
)

register_service(service_name=MESSAGE_SERVICE_NAME)
atexit.register(consul_cleanup, MESSAGE_SERVICE_NAME)
