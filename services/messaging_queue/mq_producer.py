from services.messaging_queue.connect_to_q import messaging_queue


def produce(item) -> None:
    messaging_queue.put(item)
