from .hazel_connection import connect_to_cluster



def main():
    client = connect_to_cluster(cluster_name="dev", cluster_ports=[5701, 5702, 5703])
    queue = client.get_queue("my-bounded-queue").blocking()

    while True:
        try:
            item = queue.poll()
            
            if item is None:
                print(f"Found the queue empty.")
            elif item != -1:
                print(f"consumed: {item}")
            else:
                print("poisson pill encountered. Exiting...")
                queue.put(-1)
                break
        except Exception as e:
            print(f"encountered an error: {e}. \nexiting...")
            break

    client.shutdown()


if __name__ == "__main__":
    main()