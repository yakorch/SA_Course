from services.consul_service.consul_connection import consul_client


def get_consul_value(key: str):
    _, data = consul_client.kv.get(key)
    if data:
        return data["Value"].decode("utf-8")
    return None
