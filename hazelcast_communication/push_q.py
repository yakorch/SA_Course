from .hazel_connection import connect_to_cluster
import tqdm


def main():
    client = connect_to_cluster(cluster_name="dev", cluster_ports=[5701, 5702, 5703])
    queue = client.get_queue("my-bounded-queue").blocking()

    for i in tqdm.trange(1, 100 + 1):
        queue.put(i)
        print("produced: ", i)
    # poisson pill
    queue.put(-1)
    
    client.shutdown()



if __name__ == "__main__":
    main()