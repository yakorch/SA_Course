from .hazel_connection import connect_to_cluster
import os
import tqdm


def main():
    hazel_lock = int(os.environ["HAZEL_LOCK"])

    assert hazel_lock in [0, 1, 2]

    client = connect_to_cluster(cluster_name="dev", cluster_ports=[5701, 5702, 5703])
    map = client.get_map("my-distributed-map").blocking()

    n_times_to_increment = 10_000
    counter_key = 0
    map.put_if_absent(counter_key, 0)

    if hazel_lock == 0:
        def increment():
            current_value = map.get(counter_key)
            map.put(counter_key, current_value + 1)
    elif hazel_lock == 1:
        def increment():
            map.lock(counter_key)

            current_value = map.get(counter_key)
            map.put(counter_key, current_value + 1)

            map.unlock(counter_key)
    else:
        def increment():
            while True:
                current_value = map.get(counter_key)
                updated_value = current_value + 1

                if map.replace_if_same(counter_key, current_value, updated_value):
                    break

    for _ in tqdm.trange(n_times_to_increment):
        increment()

    client.shutdown()


if __name__ == "__main__":
    main()
