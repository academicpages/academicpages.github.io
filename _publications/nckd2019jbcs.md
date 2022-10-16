---
title: "Using weaker consistency models with monitoring and recovery for improving performance of key-value stores"
collection: publications
permalink: /publications/nckd2019jbcs
venue: "Journal of the Brazilian Computer Society, volume 25"
excerpt: 'This paper is the journal version of the paper published at LADC 2018.'
date: 2019-10-30
paperurl: https://doi.org/10.1186/s13173-019-0091-9
citation: 'Duong N. Nguyen, Aleksey Charapko, Sandeep S. Kulkarni, and Murat Demirbas. Using weaker consistency models with monitoring and recovery for improving performance of key-value stores. J Braz Comput Soc 25, 10 (2019).'
---

## Abstract
Consistency properties provided by most key-value stores can be classified into sequential consistency and eventual consistency. The former is easier to program with but suffers from lower performance whereas the latter suffers from potential anomalies while providing higher performance. We focus on the problem of what a designer should do if he/she has an algorithm that works correctly with sequential consistency but is faced with an underlying key-value store that provides a weaker (e.g., eventual or causal) consistency. We propose a detect-rollback based approach: The designer identifies a correctness predicate, say P, and continues to run the protocol, as our system monitors P. If P is violated (because the underlying key-value store provides a weaker consistency), the system rolls back and resumes the computation at a state where P holds.We evaluate this approach with graph-based applications running on the Voldemort key-value store. Our experiments with deployment on Amazon AWS EC2 instances show that using eventual consistency with monitoring can provide a 50–80% increase in throughput when compared with sequential consistency. We also observe that the overhead of the monitoring itself was low (typically less than 4%) and the latency of detecting violations was small. In particular, in a scenario designed to intentionally cause a large number of violations, more than 99.9% of violations were detected in less than 50 ms in regional networks (all clients and servers in the same Amazon AWS region) and in less than 3 s in global networks.We find that for some applications, frequent rollback can cause the program using eventual consistency to effectively stall. We propose alternate mechanisms for dealing with re-occurring rollbacks. Overall, for applications considered in this paper, we find that even with rollback, eventual consistency provides better performance than using sequential consistency.

## Keywords
Predicate detection, Distributed debugging, Distributed monitoring, Distributed snapshot, Distributed key-value stores, Rollback
