---
title: 'Data Modeling'
date: 2021-12-04
permalink: /posts/2021/12/data-modeling/
tags:
  - test
  - text
---

Data Modeling in the Data Engineering Context

What Data Modeling is about
======
It's not about building a model in the way that Data Scientists do. In Data Engineering,
modeling is about structuring data so that various scientists and analysts can access it.
A standard approach is to begin with conceptual data modeling, continue over to logical data modeling,
and then to physical data modeling.

conceptual -> logical -> physical
------
In the concept phase, the ERD maps those highest-level relationships. Then in logical modeling,
tables, schemas, and columns are defined. More details are specified. Lastly, physical modeling is where
the logical model is translated into the DDL (Data Definition Language), so that the database can be constructed.
