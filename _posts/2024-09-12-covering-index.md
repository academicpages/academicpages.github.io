---
title: 'Covering Index'
date: 2024-09-12
permalink: /posts/covering-index/
tags:
  - SQL
  - SQL Server
  - Indexes
  - Covering Index
  - DBMS
---

When it comes to improving query performance in the different DBMS, Covering Indexes are one of the most effective — yet often overlooked — tools at your disposal. In this blog, I'll break down what they are, how they work, and why they matter.

## What is a Covering Index?

A Covering Index is a special kind of non-clustered index that contains all the columns required by a specific query. Because the index `covers` everything the query needs, the DBMS can retrieve the data without accessing the underlying table, eliminating the need for extra lookups.

---
As we know, indexes help the DBMS access data more efficiently. There are two main types:

- **Clustered Index**: Defines the physical order of data in the table. Each table can have only one clustered index.
- **Non-Clustered Index**: Stored separately from the table data and contains a copy of selected columns along with a reference to the actual data row.

---

### Example

Let’s say we have a table called `Student` with the following columns:

```sql
(Id, FirstName, LastName, Email, GPA)
```
Assume `Id` is the Primary Key, and there's a Clustered Index on it.

If you run:
```sql
SELECT * FROM Student WHERE Id = 287
```
The DBMS uses the clustered index on `Id` to directly fetch and return the full row — fast and efficient.

Now imagine you want to run a query like this:
```sql
SELECT * FROM Student WHERE GPA > 2.8
```

You create a Non-Clustered Index on `GPA`:
```sql
CREATE NONCLUSTERED INDEX IX_Student_GPA ON Student(GPA);
```

The DBMS will use the index to quickly find students with `GPA > 2.8`. 
However, since the index only includes GPA and not the rest of the columns, the DBMS has to go back to the table using the clustered key (Id) to fetch the remaining column data.

This process is called a Key Lookup. 

---

## Using the Covering Index
To avoid the additional lookup, you can modify the index to include all the columns your query needs:
```sql
CREATE NONCLUSTERED INDEX IX_Student_GPA_Covering
ON Student(GPA)
INCLUDE (Id, FirstName, LastName, Email);
```

Now, when you run:
```sql
SELECT * FROM Student WHERE GPA > 2.8
```
The DBMS finds everything it needs inside the index — no need to touch the base table. This significantly reduces I/O and improves performance.

---
### Key Benefits of Covering Indexes
1. **Performance Boost**: By eliminating key lookups, Covering Indexes can drastically reduce query execution time.
2. **Reduced I/O**: Less data needs to be read from the disk, which is especially beneficial for large tables.
3. **Efficient Use of Indexes**: We can include columns without making them part of the index key.