from services.messaging_queue.connect_to_q import messaging_queue
import logging
from threading import Thread, Lock
from services.message import Message

in_memory_messages: dict[str, str] = {}
in_memory_messages_lock = Lock()


def read_messages():
    with in_memory_messages_lock:
        return in_memory_messages.values()


def message_consumer():
    while True:
        try:
            message: Message = messaging_queue.take()
            logging.info(f"Received and removed message from MQ: {message}")
            with in_memory_messages_lock:
                in_memory_messages[message.identifier] = message.text
        except Exception as e:
            logging.error(f"Failed to take message from the queue: {e}")


def start_message_consumer():
    consumer_thread = Thread(target=message_consumer)
    consumer_thread.daemon = True
    consumer_thread.start()
