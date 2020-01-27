---
title: "Benefit of selfstabilizing protocols in eventually consistent key-value stores: a case study"
collection: publications
permalink: /publications/nkd2019icdcn
venue: "Proceedings of the 20th International Conference on Distributed Computing and Networking, ICDCN 2019"
excerpt: 'In this paper, we investigated the benefit of self-stabilization in recovering faults caused by consistency violation faults. When a key-value store employs a weak consistency model (e.g. eventual consistency), the data at different replicas could be inconsistent. Application reading inconsistent data could execute incorrect computation transitions. Such incorrect transitions are denoted as consistency violation faults.'
date: 2019-01-04
paperurl: https://dl.acm.org/doi/10.1145/3288599.3288609
citation: 'Duong N. Nguyen, Sandeep S. Kulkarni, and Ajoy K. Datta. Benefit of selfstabilizing protocols in eventually consistent key-value stores: a case study. In Proceedings of the 20th International Conference on Distributed Computing and Networking, ICDCN 2019, Bangalore, India, January 04-07, 2019, pages 148--157, 2019.'
---

## Abstract
In this paper, we focus on the implementation of distributed programs in using a key-value store where the state of the nodes is stored in a replicated and partitioned data store to improve performance and reliability. 
Applications of such algorithms occur in weather monitoring, social media, etc. 
We argue that these applications should be designed to be stabilizing so that they recover from an arbitrary state to a legitimate state. 
Specifically, if we use a stabilizing algorithm then we can work with more efficient implementations that provide eventual consistency rather than sequential consistency where the data store behaves as if there is just one copy of the data. 
We find that, although the use of eventual consistency results in consistency violation faults (\cvf) where some node executes its action incorrectly because it relies on an older version of the data, the overall performance of the resulting protocol is better. We use experimental analysis to evaluate the expected improvement. We also identify other variations of stabilization that can provide additional guarantees in the presence of eventual consistency. 
Finally, we note that if the underlying algorithm is not stabilizing, even a single \cvf may cause the algorithm to fail completely, thereby making it impossible to benefit from this approach.

## Keywords
Self-stabilization, Distributed key-value store, Consistency models
