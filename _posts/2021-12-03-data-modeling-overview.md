---
title: 'Overview of Database Modeling'
date: 2021-12-03
permalink: /posts/2021/12/data-modeling/
tags:
  - RDBMS
  - ACID
  - non-relational databases
  - NoSQL
---

Data Engineering will involve modeling relational and non-relational data. These tasks require a very particular conceptual understanding of these two forms. As an overview, here are some notes on what it may involve...

What Data Modeling is about
======

Data modeling in the Data Engineering Context is not about building a model in the way that Data Scientists do.
Rather, in Data Engineering, modeling is about structuring data so that various scientists and analysts can access it.
A standard approach is to begin with conceptual data modeling, continue over to logical data modeling,
and then to physical data modeling.

Conceptual -> Logical -> Physical
------

In the concept phase, the ERD maps those highest-level relationships. Then in logical modeling,
tables, schemas, and columns are defined. More details are specified. Lastly, physical modeling is where
the logical model is translated into the DDL (Data Definition Language), so that the database can be constructed.

Characteristics of a Data Modeling Process
------

Iterative: It is not a one-and-done process. One may return to the model repeatedly to tweak it as needed.

Organized: This will determined how well the data is used by applications or queries by analysts.

Modeling a Relational Database
======

There are many scenarios in which the relational database model will be the right solution.

Advantages of Using a Relational Database
------

* Flexibility for writing in SQL queries

* Smaller data volumes: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.

* Ability to do JOINS, aggregations and analytics in SQL

* Secondary Indexes availability: adding another index can help with faster search performance.

* **ACID** Transactions: an RDBMS will allow you to meet a set of properties of database transactions intended to safeguard against errors and failures, maintaining data integrity and validity. (I explain ACID later.)

Non-Relational (NoSQL) Database Modeling
======

"Not only SQL" databases come in many forms. A couple examples of these are MongoDB and Apache Cassandra.

Non-Relational Database Advantages
------

unstructured data: when different data types and formats need to be stored in a field, NoSQL can handle this well.

large data volumes: distributed databases allow for more machines to be added to process big data volumes.

HA (high availability): protected with more than a single point of failure.

high throughput and fast reads: The drawback of ACID transactions is their slow speed when reading and writing data.

Flexible schemas: NoSQL DBs allow engineers to add columns, which don't need data in every row. This saves disk space tremendously.
