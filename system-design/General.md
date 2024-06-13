# Overview

This is a document covering the basic components of system design interviews. More content will be added and linked as we go forward.

## CAP Theorem

CAP (Consistency, Availability, Partition-Tolernance) theorem states that a distributed system can't guarantee C, A and P simultaneously.

Usually only 2 things at a time can be guaranteed. Examples:

1. RDBMS DBs guarantee consistency and availability.
2. Redis, MongoDB, HBase guarantee consistency and partition tolerance
3. Casssandra, CouchDB guarantee availability and partition tolerance.