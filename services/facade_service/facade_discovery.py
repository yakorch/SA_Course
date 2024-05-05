import atexit
from services.consul_service.service_registration import register_service, consul_cleanup

FACADE_SERVICE_NAME = "facade-service"

register_service(service_name=FACADE_SERVICE_NAME)
atexit.register(lambda: consul_cleanup(service_name=FACADE_SERVICE_NAME))
