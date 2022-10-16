---
title: "Precision, recall, and sensitivity of monitoring partially synchronous distributed systems."
collection: publications
permalink: /publications/ynvkd2016rv
venue: "Proceedings of 16th International Conference on Runtime Verification, RV 2016"
excerpt: 'This paper examines the sensitivity of the monitors in distributed systems that employ hybrid vector clocks.'
date: 2016-09-23
paperurl: https://link.springer.com/chapter/10.1007/978-3-319-46982-9_26
citation: 'Sorrachai Yingchareonthawornchai, Duong N. Nguyen, Vidhya Tekken Valapil, Sandeep S. Kulkarni, and Murat Demirbas. Precision, recall, and sensitivity of monitoring partially synchronous distributed systems. In Runtime Verification - 16th International Conference, RV 2016, Madrid, Spain, September 23-30, 2016, Proceedings, pages 420-435, 2016.'
---

## Abstract
Runtime verification focuses on analyzing the execution of a given program by a monitor to determine if it is likely to violate its specifications. There is often an impedance mismatch between the assumptions/model of the monitor and that of the underlying program. This constitutes problems especially for distributed systems, where the concept of current time and state are inherently uncertain. A monitor designed with asynchronous system model assumptions may cause false-positives for a program executing in a partially synchronous system: the monitor may flag a global predicate that does not actually occur in the underlying system. A monitor designed with a partially synchronous system model assumption may cause false negatives as well as false positives for a program executing in an environment where the bounds on partial synchrony differ (albeit temporarily) from the monitor model assumptions.

In this paper we analyze the effects of the impedance mismatch between the monitor and the underlying program for the detection of conjunctive predicates. We find that there is a small interval where the monitor assumptions are hypersensitive to the underlying program environment. We provide analytical derivations for this interval, and also provide simulation support for exploring the sensitivity of predicate detection to the impedance mismatch between the monitor and the program under a partially synchronous system.

## Keywords
False Positive Rate, Linear Temporal Logic, Clock Synchronization, Impedance Mismatch, Asynchronous System 
