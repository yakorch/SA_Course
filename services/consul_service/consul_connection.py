import consul
import os


def read_consul_address():
    host = os.getenv("CONSUL_HOST")
    port = int(os.getenv("CONSUL_PORT"))
    return {"host": host, "port": port}


def get_consul_client():
    return consul.Consul(**read_consul_address(), scheme="http")

consul_client = get_consul_client()