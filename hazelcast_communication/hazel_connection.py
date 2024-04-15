import hazelcast
import os



def connect_to_cluster(cluster_name: str = "dev", cluster_ports: list[int] = [5701, 5702, 5703]) -> hazelcast.HazelcastClient:
    """
    `HOST_IP` is assumed to be stored in the process environment variables. Throws otherwise.
    """
    HOST_IP = os.environ["HOST_IP"]
    assert cluster_ports, "`cluster_ports` should be non-empty"

    cluster_members = [f"{HOST_IP}:{port}" for port in cluster_ports]
    
    client = hazelcast.HazelcastClient(
        cluster_name=cluster_name,
        cluster_members=cluster_members,
    )
    return client
