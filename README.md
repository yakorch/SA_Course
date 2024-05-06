# Consul for Service Discovery and Config Server

Start all the services with:
```bash
docker-compose up -d
```
## Motivation
Messaging and Logging services are implemented so that they can be easily scaled horizontally.
Also, the number of services may vary for different load or because of networking issues.

The services that rely on such dynamic service instances need a robust way to get the currently healthy endpoints and use them.

Consul solves this problem. Whenever the service is created, it registers itself in the services registry. From time to time Consul checks whether the registered services are still healthy by running a quick health check. I used REST API for this.

Consul allows to store Key-Value (KV) pairs for services configuration. This allows to read the necessary config information rather than hard-code it. For example, Logging service uses a Hazelcast distributed map, which name is saved in KV consul pairs.

Each service is identified based on the [service name](./services/service_names.py) and the port it uses.

## Consul service implementation | Python
The consul interactions are stored [here](./services/consul_service). Consul connection, KV lookup, service discovery, and service registration are defined there.
Every service uses this API.

## Consul service implementation | Docker
The [population script](consul-population.sh) is run at the start of consul service. It waits until the consul has initialized, populates KV dictionary, and then puts `CONSUL_ESSENTIAL_KEY` to let other services know that the initialization has completed. From now on, the service is considered **healthy** and this is marked in [`docker-compose`](./docker-compose.yaml#L233).

## Testing
...

## Cleanup

```bash
docker-compose down
docker rmi facade-service messages-service logging-service
```