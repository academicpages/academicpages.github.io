---
title: 'Paxos Made Simple'
date: 2022-03-12
permalink: /posts/2022/03/paxos-made-simple/
tags:
  - Paxos
  - Consensus
  - Distributed
---

There is no denying that the paxos algorithm for consensus is difficult.
Not only that but there are so many variants of paxos that comprehending them becomes overwhelming.
Leslie Lamport's original paper [The part-time parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) is,
in his words, "Greek to many readers". I would not deny that. Here is a simple summary of it.

Why is distributed consensus difficult?
======
For the sake of simplicity, let's limit ourselves to a consensus on values. The processes 
propose a value which is either accepted or rejected based on the consensus reached. To ensure correctness, 
we need to maintain the following:

* A value that has been accepted/chosen should be one that was proposed by at-least one process.
* The consensus should lead to a single value being selected
* A process involved in the consensus does not choose a value unless a consensus has been reached on it. 


You can have many headings
======

Aren't headings cool?
------