import atexit
from services.consul_service.service_registration import (
    register_service,
    consul_cleanup,
)
from services.service_names import LOGGING_SERVICE_NAME


register_service(service_name=LOGGING_SERVICE_NAME)
atexit.register(consul_cleanup, LOGGING_SERVICE_NAME)
