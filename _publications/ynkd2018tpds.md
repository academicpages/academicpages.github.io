---
title: "Analysis of bounds on hybrid vector clocks"
collection: publications
permalink: /publications/ynkd2018tpds
venue: "IEEE Transaction on Parallel and Distributed Systems, volume 29, 2018"
excerpt: 'This paper investigate the effectiveness of using hybrid vector clocks (HVC) to keep track of causality in distributed systems. The analytical analysis and experimental results show that hybrid vector clocks can effectively determine causality with the overhead of a couple of entries and substantially less than n (the number of processes).'
date: September 2018
paperurl: https://www.computer.org/csdl/journal/td/2018/09/08323242/13rRUwh80GS
citation: 'Sorrachai Yingchareonthawornchai, Duong N. Nguyen, Sandeep S. Kulkarni, and Murat Demirbas. Analysis of bounds on hybrid vector clocks. IEEE Transaction on Parallel and Distributed Systems, 29(9):1947-1960, 2018'
---

## Abstract
Hybrid vector clock(s) (HVC) provide a mechanism to combine the theory and practice of distributed systems. Improving on traditional vector clock(s) (VC), HVC utilizes synchronized physical clocks to reduce the size by focusing only on causality where the physical time associated with two events is within a given uncertainty window ε and letting physical clock alone determine the order of events that are outside the uncertainty window. In this paper, we develop a model for determining the bounds on the size of HVC. Our model uses four parameters, ε: uncertainty window, 8: message delay, a: communication frequency and n: number of nodes in the system. We derive the size of HVC in terms of a delay differential equation, and show that the size predicted by our model is almost identical to the results obtained by simulation. We also identify closed form solutions that provide tight lower and upper bounds for useful special cases. We show that for many practical applications and deployment environments in Amazon EC2, the size of HVC remains only as a couple entries and substantially less than n. Finally, although the analytical results rely on a specific communication pattern they are useful in evaluating size of HVC in different communication scenarios.

## Keywords
Vector Clocks, Physical Clocks, Logical Clocks, Distributed Systems.
