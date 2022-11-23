---
title: 'views on education'
date: 2022-10-19
permalink: /posts/2022/10/views-on-education/
tags:
  - English
---

# Background
There are some APIs that have been designed and implemented, which provided secure computing(via some algorithm about `k-anonymity` and `differential privacy`) API for JD retail data. eg

```python
# calculate monthly sales for apple watch in 2022
orders = spark.read.csv("s3://path/to/order/data")
apple_watch_order=orders.filter("orders.product_name='apple_watch'")
monthly_sales = apple_watch_order.group_by("date_month").sum("price")

```

However, the user may not be familiar with the program, but they know SQL as a Data Analyst. Therefore, we design a new SDK called SQLparser to convert SQL into computing API. 

The case we mentioned above could be converted to a simple SQL
```pyhton
spark.sql("""select sum('price') from orders where product_name='apple_watch'  group by('data_month')""")
```

> ANTLR, Pyspark, SQL, Python

# Design and implement	



SQL->plan->codegeneration



This stage is generated after a first check that verifies everything is correct on the syntactic field. Next, the semantic analysis is executed and will produce the first version of a logical plan where the relation name and columns are not specifically resolved. 

When the unresolved plan has been generated, it will use metastore to verify data structures, schemas, types, etc. 

Now we have a plan(which is an abstract syntax tree) to represent how the data will be processed.

Finally, we just recursive this AST to generate API code.

