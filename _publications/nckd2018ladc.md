---
title: "Using weaker consistency models with monitoring and recovery for improving performance of key-value stores"
collection: publications
permalink: /publications/nckd2018ladc
venue: "Proceedings of The 8th Latin-American Symposium on Dependable Computing, LADC 2018"
excerpt: 'This paper investigates the benefits of weak consistency settings in key-value stores. We quantify the performance improvement as well as the cost for monitoring the correctness of the computation when using weaker consistencies. Our experiments show that the performance is improved significantly while overhead of monitoring is small.'
date: 2018-10-08
paperurl: https://ieeexplore.ieee.org/document/8671598
citation: 'Duong N. Nguyen, Aleksey Charapko, Sandeep S. Kulkarni, and Murat Demirbas. Using weaker consistency models with monitoring and recovery for improving performance of key-value stores. In The 8th Latin-American Symposium on Dependable Computing, LADC 2018, Foz do Iguacu, Brazil, October 08-10, 2018.'
---

## Abstract
Limitations of the CAP theorem imply that if availability is desired in the presence of faults - especially that create network partitions (or substantial delays), one must sacrifice sequential consistency, a consistency model that is more natural for system design. We focus on the problem of what a designer should do if he/she has an algorithm that works correctly with sequential consistency but is faced with an underlying key-value store that provides a weaker (e.g., eventual or causal) consistency. We propose a detect-rollback based approach: The designer identifies a correctness predicate, say P, and continues to run the protocol, as our system monitors P. If P is violated (because the underlying key-value store provides a weaker consistency), the system rolls back and resumes the computation at a state where P holds. We evaluate this approach with practical graph applications running on the Voldemort key-value store. Our experiments, deployed on Amazon AWS EC2 instances, show that using eventual consistency with monitoring can provide a 50 - 80% increase in throughput when compared with sequential consistency. We also show that the overhead of the monitoring itself is low (typically less than 4%) and the latency of detecting violations is small. In particular, more than 99.9% of violations are detected in less than 50 milliseconds in regional AWS networks, and in less than 5 seconds in global AWS networks. In turn, this makes it possible to provide efficient recovery from such faults with a minimal amount of work wasted due to rollbacks.

## Keywords
predicate detection, distributed debugging, distributed monitoring, distributed snapshot, distributed key-value stores
