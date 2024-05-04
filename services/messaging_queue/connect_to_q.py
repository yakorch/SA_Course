from hazelcast import HazelcastClient
import os
from services.logging_setup import *


client = HazelcastClient(
    cluster_members=[os.getenv("HZ_NETWORK_PUBLICADDRESS")], cluster_name="mq"
)

messaging_queue = client.get_queue("messaging_queue").blocking()
