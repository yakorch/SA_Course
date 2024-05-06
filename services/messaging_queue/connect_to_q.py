from hazelcast import HazelcastClient
import os
from services.logging_setup import *
from services.consul_service.KV_lookup import get_consul_value



client = HazelcastClient(
    cluster_members=[os.getenv("HZ_NETWORK_PUBLICADDRESS")],
    cluster_name=get_consul_value("hz_mq_cluster_name"),
)

messaging_queue = client.get_queue(get_consul_value("mq_name")).blocking()
