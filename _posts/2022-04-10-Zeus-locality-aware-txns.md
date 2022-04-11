---
title: 'Zeus: locality aware distributed transactions'
date: 2022-04-07
permalink: /posts/2022/04/zeus-locality-aware-txns/
tags:
  - Locality
  - Transactions
  - Dynamic sharding
  - Availability
  - Strict serializability
  - pipelining
  - replication
---


Typical databases have distributed transactions that update multiple objects. These objects are updated by transactions that span multiple shards and require coordination for state reconciliation. Most popular protocol to reconcile the state is the two phase commit protocol. This distribution is an inherent problem since most transactions access multiple replicas and thus the communication latency between those replicas leads to a slowdown. The commit requiring coordination is also blocking. Zeus fetches the objects involved in a transaction's operations locally and then performs the reads and writes on the local versions of the objects. 

To ensure that the locality is not violated by concurrent transactions accessing the same object, there are protocols in place that ensure that the database as a whole is fault tolerant and strongly consistent. 

### Argument for Zeus

The authors argue that the high performance dynamic sharding of objects in a database benefits from locality. In essence, the benefits of local execution outweigh the cost of re-sharding the objects. They introduce two protocols. 
 - Ownership protocol for transferring objects to the locality of transaction execution.
 - Reliable commit to commit the changes made locally to the objects and replicating them across all the shards. 

### Agents in Zeus

- **Coordinator** : The typical transaction coordinator that handles execution, commits and aborts of the transaction. 

- **Follower** : All the nodes that keep a backup of the objects, which need to be informed of the updates by the coordinator during commit. 

- **Owner** : the node that possesses the rights for a specific object is called its owner. 

- **Reader** : Any node that has a copy of the object and is only allowed to perform read-only transactions on the object. 

- **Directory** : A node containing the ownership metadata of the objects. This directory contains the object state, object timestamp, the replicas that store the object. 


### Running transactions in Zeus (Updating and Reading objects)

A transaction in Zeus has 3 phases

- **Prepare and Execute** : Before the transaction accesses an object, it ensures that the proper ownership rights are present to perform operations on the object. If not, the proper rights are acquired via the ownership protocol. The transaction then creates a local copy of the objects to operate on. 

- **Local commit** : When the transaction is done performing the operations, it commits via a traditional single node commit.

- **Reliable commit** : Upon successfully committing the transaction locally, the coordinator pushes all the local updates for the followers.  


## Reliable Ownership
Each object in a Zeus based datastore has a single unique owner at any given time. These owners can change throughout the object's lifecycle. Zeus maintains an ownership directory that manages the ownership metadata about the object. This directory is replicated across three nodes for reliability.

### Failure and contention free operation:

- A node that starts the ownership request is called the ***requester***. This requester assigns a locally unique id to the object acquisition request and sets the object's local state to ***Request***.

- This request is then forwarded to an arbitrarily chosen directory node. This directory node becomes the ***driver*** of the request.

- The driver then assigns an ownership timestamp to the object and sets its local state to ***Drive***.

- The driver then sends an invalidation request for the object to the arbiters.

- If there is no contention for the object's acquisition, the arbiters set their local state of the object to ***Invalid*** ans also update their timestamps and replica information. The arbiters then acknowledge this and send an ACK to the requester. 

- When the requester receives all the expected ACK messages, it adds itself to the replica list of the object and sets the object state to ***Valid*** on it's own replica. 


### Contention and resolution:

If multiple requesters create an ownership request for the same object, these are resolved using the ownership timestamp. A deadlock is brocken using the lexicographic order on the timestamps assigned by the driver. A node only processes an invalidation message if it is greater than its own timestamp for the same object. 

For a driver that has its request denied, it sends back a NACK to the requester. The requester can then abort the request or decide to re-initiate. 

### Failure recovery
When a node dies, all the objects owned by that node become orphans. In this case, the directory node updates the list of replicas for the objects by removing any dead nodes. If an object is an orphan, it will be owned in the next write transaction request that comes along. 

If the node died after it had invalidated the object, the arbiters will have their object states as ***Invalid***. In this case, the arbiters can coordinate among themselves and unblock. A block arbiter drives the replay request by constructing and transmitting the same invalidation message using its local state. This is called as ***arb-replay***. During arb-replay, if an arbiter has already received an invalidation message, it responds with an ACK. 

During recovery the ACK message is sent back to the driver instead of the requester.  


## Reliable Commit

### Failure free operation

When the transaction locally commits its updates, it updates the ***data*** of the modified objects as well as their ***versions***. It then sets the state of the objects to ***Write*** to indicate them being pending for a reliable commit. 

The coordinator then broadcasts an ***invalidation*** message to all the followers along with the updated data and the version. When a follower receives this message, it checks if the epoch id matches with the epoch it is in, if it does, the objects' versions are matched with its local versions. If the versions are different and the version received in the invalidation message is newer, it is updated. The follower then marks the updated object as ***Invalid*** stating that it has a pending reliable commit and sends an acknowledgement back to the coordinator. 

When all the acknowledgement messages are received by the coordinator, it broadcasts a ***Validation*** message to the followers. This lets the followers know that the transaction can be committed. When the follower receives this validation message, it checks if it had received an invalidation message for the same transaction for the same version of the object. If it did, then the object is marked as valid and the transaction considered committed. If the version has changed, then the validation message is ignored. 


### Reliable replay under failures. 

When a node fails, the transactions under progress by that node fail too. Following this, the failed node will not be able to initiate a reliable commit. In this case, a reconfiguration happens. Following which, a live node replays it's own reliable commits and those from the failed nodes.

To do this, the node first updates the local invalidation messages with the new epoch Id and removes all the dead nodes from the followers. A reliable commit is re-initiated. When a follower receives the messages for invalidation and validation and it has previously stored these messages, it ignores them and responds with an acknowledgement. When there are no pending reliable commits, the node informs the ownership protocol that the routine operations can happen. 


## Discussion

Zeus reduces the need for round trips between nodes when committing a transaction. This is achieved by transferring the ownership of an object between the nodes. Unlike traditional commits, local commits in Zeus followed by reliable commits are faster. The need to transfer objects between nodes is observed (using real benchmarks) to have a non-significant impact on the performance. 