---
title: 'Relational Database Modeling'
date: 2021-12-04
permalink: /posts/2021/12/data-modeling-relational/
tags:
  - RDBMS
  - ACID
  - PostgreSQL
  - OLAP
  - OLTP
---

Relational Database Modeling in PostgreSQL

The Many Advantages of a Relational Database
------

* Flexibility for writing in SQL queries

* Smaller data volumes: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.

* Ability to do JOINS, aggregations and analytics in SQL

* Secondary Indexes availability: adding another index can help with faster search performance.

* **ACID** Transactions: an RDBMS will allow you to meet a set of properties of database transactions intended to safeguard against errors and failures, maintaining data integrity and validity. ACID in a few quick sentences:

    * Atomicity: either the whole transaction is processed or none of it at all.

    * Consistency: If the transaction does not adhere to constraints and rules written into the database, then the previous state will be kept. The data must be correct across all rows and tables.

    * Isolation: Transactions are processed independently, securely, and without regard to transaction order. There is a trade-off between low and high levels of isolation.

    * Durability: transactions are saved to a database once they're committed, even in the event of a system failure.


OLAP vs OLTP
======

OLAP and OLTP are two processes that
[vary distinctly from each other](https://stackoverflow.com/questions/21900185/what-are-oltp-and-olap-what-is-the-difference-between-them).

Online Transactional Processing (OLTP):
------
These workloads allow for large volumes of less complex queries (read, insert, update, and delete).

Online Analytical Processing (OLAP):
------
These workloads allow for complex analytical and ad-hoc queries, including *aggregations*. These type of databases are optimized strictly for reads.

Denormalization
------
Denormalization is done to speed up the database read time by adding data redundancy. Normalized DBs allow for joins, but joins slow down the read time, even if they do minimize data redundancy. Since the cost of storage space has gone down, multiple copies of data is not a big concern.

Star Schema: Fact and Dimension Tables
------
The multiple dimension tables surround the one centered [fact table](https://en.wikipedia.org/wiki/Fact_table),
forming a star shaped schema that one can visualize.
This is the conceptual arrangement; the physical modeling (DDL) of these tables do not change.
The fact table contains transactional data, normally just numbers.

A dimension table categorizes the facts and measures to answer business questions. 
Dimension tables contain people, products, places and times.

PostgreSQL RDMBS
======

PostgreSQL is an open-source object-relational database.
The PostgreSQL syntax is different from other SQL dialects.
