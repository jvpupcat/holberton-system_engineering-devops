# 0x0F Load Balancer

<img src="https://cdn.haproxy.com/static/img/docs/an-0047-en-_dns_services_load-balancing/an-0047-en-_dns_services_load-balancing_1_new.png">

## Overview

A load balancer distributes the work-load of your system to multiple individual systems, or group of systems to reduce the amount of load on an individual system, which increases the reliability, efficiency and availability of your application.

There are advantages of load balancing your application such as:
```
* Reduced the work-load on an individual server.
* Large amount of work done in same time due to concurrency.
* Increased performance of your application because of faster response.
* No single point of failure. If a server crashes, there are other servers the load balancer direct requests to. However, the load balancer is a single point of failure.
* When appropriate load balancing algorithm is used, it brings optimal and efficient utilization of the resources, as it eliminates the scenario of some server's resources are getting used than others.
* Scalability
* Increased reliability and security
```

There are two types of load balancers - software and hardware. A software load balancer generally implement a combination of one or more scheduling algorithms.
