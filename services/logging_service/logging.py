from services.message import Message

from hazelcast import HazelcastClient

import os


client = HazelcastClient(cluster_members=[os.getenv("HZ_NETWORK_PUBLICADDRESS")])

hz_map = client.get_map("messages").blocking()


def log_message(message: Message) -> None:
    hz_map.put(message.identifier, message.text)


def clean_logs() -> None:
    hz_map.clear()


def read_messages() -> list[str]:
    return list(hz_map.values())
