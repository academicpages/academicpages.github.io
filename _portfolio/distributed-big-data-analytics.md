---
title: "Distributed Big Data Analytics System"
excerpt: "Spark and Hive pipeline on HDFS, a Spark MLlib model for missing features, and natural-language queries translated to Spark SQL with the Gemini API. Course project, Big Data Systems."
collection: portfolio
---

Course project for Big Data Systems at UW–Madison.

**Tools:** Apache Spark (PySpark), Hive, HDFS, Spark MLlib, Gemini API, gRPC, Docker, Parquet

## What I built

- **Data pipeline:** A Spark (PySpark) and Hive pipeline on a distributed HDFS cluster for analyzing large datasets. I used bucketing and caching to speed up queries.
- **Machine learning:** A Spark MLlib decision-tree pipeline that predicts missing values in dataset features.
- **Natural-language queries:** An integration with the Gemini API that converts natural-language questions into Spark SQL that runs on the cluster.
- **Fault tolerance:** Microservices built with gRPC and Docker, using Parquet columnar storage to reduce I/O, with automated recovery logic for data-node failures.
