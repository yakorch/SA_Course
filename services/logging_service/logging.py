from services.message import Message

from hazelcast import HazelcastClient
from services.consul_service.KV_lookup import get_consul_value
import os


client = HazelcastClient(
    cluster_members=[os.getenv("HZ_NETWORK_PUBLICADDRESS")],
    cluster_name=get_consul_value("hz_logging_cluster_name"),
)

hz_map = client.get_map(get_consul_value("logging_mapping_name")).blocking()


def log_message(message: Message) -> None:
    hz_map.put(message.identifier, message.text)


def clean_logs() -> None:
    hz_map.clear()


def read_messages() -> list[str]:
    return list(hz_map.values())
