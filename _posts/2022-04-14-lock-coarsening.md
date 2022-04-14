---
title: 'Lock Coarsening: Eliminating Lock Overhead in Automatically Parallelized Object-Based Programs'
date: 2022-04-14
permalink: /posts/2022/04/lock_coarsening/
tags:
  - Transactions
  - Lock Contention
  - Granularity
  - Locking
---


Atomic operations are a key primitive in parallel computing. Typically atomic ownership is provided via mutual exclusion which is achieved in the simplest way through locking. A lock is said to be finely grained if it exclusively locks only a small part of the data structure and thus suffers from low contention. The question still remains. What should we lock and how fine can the lock granularity be without sacrificing on performance? At what point does the cost of maintaining locks override the benefit achieved from the finer locking. 

The paper on [Lock Coarsening](https://doi.org/10.1007/BFb0017259) describes a static analysis technique that can be used to automatically increase the lock granularity in object oriented programs that use atomic operations. 

### Issues with Locks

Locking typically leads to two sources of performance loss:

- **Lock overhead** which is the cost of acquiring, maintaining and releasing the lock.
- **Lock Contention** which is the performance degradation observed when multiple processes try to acquire the same lock leading to either denial and retries or spin-waiting. 

Both these costs can be significant if the locking mechanism is not carefully designed. Typically, lock contention is inversely related to lock overhead. Coarser locks have a smaller overall overhead but suffer from higher contention and vice a versa. The algorithms described in the following sections, thus, tru to maintain a balance between the two. 



### Techniques of Coarsening

**Data Lock Coarsening** : Data lock coarsening is a technique in which the compiler associates one lock with multiple objects that tend to be accessed together. The operations that affect these data objects are then executed together under a single lock. This helps in two ways. First, it reduces the number of locks required to execute the same set of operations. Second, the number of acquire and release phases for the locks are reduced because of fewer lock handovers. 

The issue is that an overly aggressive data lock coarsening algorithm can lead to false contention. 


**Computation Lock Coarsening** : When a single computation acquires and releases a lock on the same set of objects, it makes sense to acquire the lock for all these objects simultaneously. Computation lock coarsening focusses on this. It transforms the computation sot acquire the lock, perform the operations and then release the lock at once when the whole set of operations is complete. 

An overly aggressive computation lock coarsening leads to false exclusion. This is when a process holds a lock for an object that it does not access for some time.


### Lock coarsening in practice

- For an object oriented application that access a set of objects and has an inheritance hierarchy, the lock can be inherited too which allows the lock acquired by the parent class to be used by the children. This is a simple transformation that can be applied to most object oriented programs, reducing the overhead. This is an implementation example of ***data lock coarsening***.

- Another way to coarsen the lock is to maintain a hierarchy of method calls. A single call stack uses one lock regardless of the data accessed in that method call sequence. The lock is acquired once when the top level method is invoked and subsequently reused. This is a simple implementation example of ***computation lock coarsening***


