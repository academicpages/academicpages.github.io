---
# layout: single
title:  "SLURM queue management"
date: "2021-10-12"
permalink: /posts/2021/10/slurm-queue
tags: 
  - slurm
  - ubuntu
# tags:
#   - edge case
---

The following have to be set in `slurm.conf` in order to manage the queue with memory limits and CPU limits:
<pre>
MaxMemPerNode=48500
SchedulerType=sched/backfill
SelectType=select/cons_res
SelectTypeParameters=CR_Core_Memory
</pre>

If you only need CPU limits, this is the solution:
<pre>
SchedulerType=sched/backfill
SelectType=select/cons_res
SelectTypeParameters=CR_Core
</pre>

Full compute node setup at the end of the file:
<pre>
# COMPUTE NODES
# Threadripper 3960X
NodeName=hpc-9000 CPUs=24 RealMemory=48500 Sockets=8 CoresPerSocket=3 ThreadsPerCore=1 State=UNKNOWN
PartitionName=batch Nodes=hpc-9000 Default=YES MaxTime=INFINITE State=UP
</pre>