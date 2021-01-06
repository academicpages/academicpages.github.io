---
title: 'Meaning of Shuffle Write and Shuffle Read in Spark UI'
date: 2021-01-06
permalink: /posts/spark/
tags:
  - spark
---

Shuffle Write is the sum of all written serialized data on all executors before transmitting.
Shuffle Read is the sum of all read serialized data on all executors at the beginning of a stage.
