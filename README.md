# System Architecture Course Tasks
This repo stores the learning curve of system architecture principles I have learned throughout System Architecture course.

In the end, micro-services are wrapped with Dockerfiles and their dependence is managed in `docker-compose.yaml`. Health checks are performed on the running containers.

The branches store key changes made when developing a final app. Completed roadmap:
- [`micro_basics` branch](https://github.com/yakorch/SA_Course/tree/micro_basics?tab=readme-ov-file) implements 3 service skeletons in `Flask`, which is later replaced with `FastAPI`.
- [`hazelcast` branch](https://github.com/yakorch/SA_Course/tree/hazelcast?tab=readme-ov-file) explores `Hazelcast` cluster capabilities. I have acquainted myself with:
	- distributed maps
	- distributed message queues:
		- one publisher and multiple subscribers methodology
		- poisson pill paradigm.
	- 3 ways to interact with shared resources:
		- no lock (data race occurs)
		- pessimistic lock (explicit mutex lock)
		- optimistic lock (CAS -- compare-and-swap, which turned out to be the fastest.)

- [`micro_hazelcast` branch](https://github.com/yakorch/SA_Course/tree/hazelcast?tab=readme-ov-file) combines the previous two branches and shows the independence of the Logging service instances on the message-receiving node thanks to the `Hazelcast`'s distributed map.
- [`micro_mq` branch](https://github.com/yakorch/SA_Course/tree/micro_mq) shows how the messaging queue can be used to implement a publisher-subscriber methodology. The Facade service pushes the message to the queue, and one of the Messaging service instances pops it.
- [micro_consul branch](https://github.com/yakorch/SA_Course/tree/micro_consul)  uses a consul -- the service that acts as a proxy for inter-service communication.
	Each service registers itself via consul, and from time to time sends its health status to know whether the service is responsive.
	Whenever one service needs to send a request to another service, it asks the Consul service for healthy services at the moment.
	Consul server provides the way to save Key-Value pairs (shared between all connected services) in a safe environment.

## Conclusion
Throughout these tasks, I practiced with:
- `Docker`
- `Docker Compose`
- `FastAPI`
- Interprocess communication
	- Distributed queue
	- Distributed map
	- HTTP Requests
- Service registration and configuration
	- Consul service
	- `.env` management
- Clean code ;)