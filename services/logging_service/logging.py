from services.message import Message

from hazelcast import HazelcastClient

client = HazelcastClient(
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ]
)

hz_map = client.get_map("messages").blocking()


def log_message(message: Message) -> None:
    hz_map.put(message.identifier, message.text)


def clean_logs() -> None:
    hz_map.clear()


def read_messages() -> list[str]:
    return list(hz_map.values())