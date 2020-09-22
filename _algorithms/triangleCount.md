---
title: 'Triangle Count'
date: 2020-08-26
permalink: /algorithms/triangleCount/
tags:
  - algorithms
  - clustering
  - triangle

---

## Description
The triangle count algorithm counts the number of triangles (triplet of nodes which all pairwise share a link) that each vertex is a member of, from which additionally the global graph triangle count and clustering coefficient can be realised.

## Implementation
The algorithm is similar to that of GraphX and fairly straightforward:

1. Each vertex compiles a list of neighbours with ID strictly greater than its own, and sends this list to all neighbours as an array.

2. Each vertex, starting from a triangle count of zero, looks at the lists of ID sets it has received, computes the intersection size of each list with its own list of neighbours, and adds this to the count.

3. The total triangle count of the graph is calculated as the sum of the triangle counts of each vertex, divided by 3 (since each triangle is counted for each of the 3 vertices involved).

4. The clustering coefficient for each node is \\(C_i =  \\)

## Returns

## Notes


------
