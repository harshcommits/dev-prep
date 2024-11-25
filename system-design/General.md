-# Overview

This is a document covering the basic components of system design interviews. More content will be added and linked as we go forward.

## Good system design

There are a few parameters that any good system should abide by:

1. Scalable
2. Maintainable
3. Reliable
4. Efficient

There's 3 key elements for system:

1. Moving data
2. Storing data (access patterns, indexing strategies come into play here)
3. Transforming data (log aggregation etc.)

## CAP Theorem

CAP (Consistency, Availability, Partition-Tolernance) theorem states that a distributed system can't guarantee C, A and P simultaneously.

Usually only 2 things at a time can be guaranteed. Examples:

1. RDBMS DBs guarantee consistency and availability.
2. Redis, MongoDB, HBase guarantee consistency and partition tolerance
3. Casssandra, CouchDB guarantee availability and partition tolerance.

### Availability parameters

1. Reliability
2. Fault-tolerance
3. Redundancy

Following parameters are usually followed as markers for speed in systems:

1. Throughput - quantity of requests a system can handle
2. Latency - time taken to process a single request

### HTTP Headers

Following are the status code with brief details:

1. 20x - success
2. 30x - redirection
3. 40x - client error
4. 50x - server error

Following are the methods used: 

GET - fetch data
POST - add data
PUT/PATCH - update data
DELETE - remove data
HEAD - get header details (maybe)

## Websockets

1. Push realtime updates to clients
2. Usually used for chat/stock or sports updates

### Realtime communication protocols

1. WebRTC - browser-based communication for voice calling, video chats etc.
2. MQTT (Message Queue Telemetry Transport) - lightweight protocol; mostly is used for things like IoT
3. AMQP (Advanced Message Queueing Protocol) - message-oriented middleware, eg. RabbitMQ
4. RPC(Remote Procedure Call) - Remotely invoke function from one machine to another machine

## API Design

We can take something like Shopify as an instance. Basic CRUD(Create, Read, Update, Delete) operations would look like this:

1. READ -------------> /api/products (GET)
2. CREATE -------------> /api/products (POST)
3. UPDATE -----------------> /api/products/id (PUT/PATCH)

Some decisions involve:

1. Satting up the communication protcol. It can be either:

* HTTP
* Websockets

2. Data transfer management. Here the options can be:

* JSON
* XML
* ProtoBuf

### API Paradigm

There are quite a few options to design your APIs. Some are as follows:

1. REST - stateless, is the standard way to handle requests. Limitations include under-fetching and over-fetching
2. GraphQL - 
3. gRPC - developed by Google, based on HTTP/2. Uses protobuf with things like mutliplexing or server push. More suitable for microservices.

### Best Practices:

1. A good request should be idempotent(calling it multiple times does not change the result)
2. API should involve versioning
3. Implement rate-limiting to avoid issues like DDoS
4. Set up CORS to enable certain endpoints to view your website.

## Caching

Caching is storing the copy of data in some temporary storage to allow easier access over distances(mostly to improve latency). There are 4 ways to implement caching:

1. Browser cache - X-Cache header achieves that
2. Server caching - usually done for DB queries using options like **Redis**. There are different writing strategies to achieve this:
    * Write-around - Written in permanent storage
    * Write-through - Written both to permanent and temporary storage
    * Write-back - First written to temporary cache, then to permanent cache.

    Eviction Polices dictate how cache is cleaned
3. DB caching
4. CDN caching - used for static content like HTML, CSS, images. Here also, there are multiple ways to achieve it:
    * Pull-based - user checks the CDN server which in turn pulls from original server
    * Push-based - original server has content which then pushes to CDN servers.

