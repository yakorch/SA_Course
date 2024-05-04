from hazelcast import HazelcastClient
import os


client = HazelcastClient(
    cluster_members=[os.getenv("HZ_CLUSTER_MEMBER")]
)

messaging_queue = client.get_queue("messaging_queue").blocking()

in_memory_messages: dict[str, str] = {}


def read_messages():
    return in_memory_messages.values()


def save_message(message):
    print("Received message:", message)


def subscribe_to_messages() -> None:
    messaging_queue.add_listener(save_message)
