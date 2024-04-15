from .hazel_connection import connect_to_cluster
import tqdm


def main():
    client = connect_to_cluster(cluster_name="dev", cluster_ports=[5701, 5702, 5703])
    map = client.get_map("my-distributed-map").blocking()

    n_values_to_put = 1_000
    for i in tqdm.trange(n_values_to_put):
        map.put(i, i)
    client.shutdown()


if __name__ == "__main__":
    main()
