---
title: 'Connected Components'
permalink: /algorithms/connectedComponents/
tags:
  - algorithms
  - partition
  - connectivity
  - components

---

<p style="margin-left: 1.5em;"> Returns the number of connected components.</p>

A connected component of an undirected graph is a set of vertices all of which are connected by paths to each other. This algorithm calculates the number of connected components in the graph and the size of each, and returns some statisics of these.

## Implementation
The algorithm is similar to that of GraphX and fairly straightforward:

1. Each node is numbered 1 to N (N the number of nodes in the graph), and takes this as an initial connected components label.

2. Each node forwards its own label to each of its neighbours.

3. Having received a list of labels from neighbouring nodes, each node relabels itself with the smallest label it has received (or stays the same if its starting label is smaller than any received).

4. The algorithm iterates over steps 2 and 3 until no nodes change their label within an iteration.

## Returns
* `top5`: the sizes of the largest 5 connected components in descending order. This is returned as an array of integers, of size 5 or the number of components if this is less than 5.
* `total`: the number of connected components, as an integer.
* `totalIslands`: the number of connected components of size 1, an integer.
* `proportion`: the proportion of the graph's vertices that are in the largest connected component, a float.
* `clustersGT2`: the number of connected components of size strictly greater than two, an integer.

## Notes

* Edges here are treated as undirected, a future feature may be to calculate weakly/strongly connected components for directed networks.
