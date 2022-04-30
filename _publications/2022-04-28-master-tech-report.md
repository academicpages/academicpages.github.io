---
title: "Persisting the AntidoteDB Cache: Design and Implementation of a Cache for a CRDT Datastore"
collection: publications
permalink: /publication/2022-04-28-master-tech-report
excerpt: 'This report presents the design and implementation of a caching, indexing and object checkpoint library for AntidoteDB. '
date: 2022-01-28
venue: 'HAL-Inria'
paperurl: 'https://hal.inria.fr/hal-03654003/document'
citation: 'Ayush Pandey, Annette Bieniusa, Marc Shapiro. Persisting the AntidoteDB Cache: Design and Implementation of a Cache for a CRDT Datastore. [Research Report] RR-9470, TU Kaiserslautern; LIP6, Sorbonne Université. 2022.'
---
Many services, today, rely on Geo-replicated databases. Geo-replication
improves performance by moving a copy of the data closer to its usage site. High availability
is achieved by maintaining copies of this data in several locations. Performance is gained by
distributing the data and allowing multiple requests to be served at once. But, replicating
data can lead to an inconsistent global state of the database when updates compete with
each other.
In this work, we study how a cache is designed and implemented, for a database that
prevents state inconsistencies by using CRDTs. Further, we study how this cache can be
persisted into a checkpoint store and measure the performance of our design with several
benchmarks. The implementation of the system is based on AntidoteDB. An additional
library is implemented to realise the discussed design

[Download paper here](https://hal.inria.fr/hal-03654003v2)