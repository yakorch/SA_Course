consul agent -dev -server -ui -node=server -bootstrap-expect=1 -client=0.0.0.0 &

echo "Waiting for consul initialization..."
sleep 5

echo "Starting KV Population"

consul kv put hz_logging_cluster_name "dev"
consul kv put logging_mapping_name "messages"
consul kv put hz_mq_cluster_name "mq"
consul kv put mq_name "messaging_queue"

echo "KV Population Ended!"

# let the container run
wait