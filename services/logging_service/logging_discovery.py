import atexit
from services.consul_service.service_registration import (
    register_service,
    consul_cleanup,
)
from services.consul_service.service_discovery import discover_service, extract_URLs
from services.consul_service.KV_lookup import get_consul_value

from services.service_names import (
    LOGGING_SERVICE_NAME,
)

register_service(service_name=LOGGING_SERVICE_NAME)
atexit.register(consul_cleanup, LOGGING_SERVICE_NAME)
