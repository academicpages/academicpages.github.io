---
title: 'Blog Post number 1'
date: 2012-08-14
permalink: /posts/2012/08/blog-post-1/
tags:
  - cool posts
  - category1
  - category2
---

The following have to be set in `slurm.conf` in order to manage the queue with memory limits and CPU limits:
```
<!-- TaskPlugin=task/affinity
TaskPluginParam=Sched -->
MaxMemPerNode=48500
SchedulerType=sched/backfill
SelectType=select/cons_res
SelectTypeParameters=CR_Core_Memory
```

If you only need CPU limits, this is the solution:
```
SchedulerType=sched/backfill
SelectType=select/cons_res
SelectTypeParameters=CR_Core
```

Full compute node setup at the end of the file:
```
# COMPUTE NODES
# Threadripper 3960X
NodeName=hpc-9000 CPUs=24 RealMemory=48500 Sockets=8 CoresPerSocket=3 ThreadsPerCore=1 State=UNKNOWN
PartitionName=batch Nodes=hpc-9000 Default=YES MaxTime=INFINITE State=UP
```