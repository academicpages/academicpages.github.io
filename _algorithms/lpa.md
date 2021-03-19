---
title: 'Label Propagation Algorithm'
collection: algorithms
type: "Algorithms"
permalink: /algorithms/lpa/
tags:
  - algorithms
  - community-detection
  - lpa

---


<p style="margin-left: 1.5em;"> Returns the communities of the constructed graph as detected by synchronous label propagation.</p>

Every vertex is assigned an initial label at random. Looking at the labels of its neighbours, a probability is assigned to observed labels following an increasing function then the vertex's label is updated with the label with the highest probability. If the new label is the same as the current label, the vertex votes to halt. This process iterates until all vertice labels have converged. The algorithm is synchronous since every vertex updates its label at the same time.


### Parameters
* `top` _(Int)_ -- The number of top largest communities to return. (_Default: 0_)
                      If not specified, Raphtory will return all detected communities.
* `weight` _(String)_ -- Edge property (_Default: `""`_). To be specified in case of weighted graph.
* `maxIter` _(Int)_ -- Maximum iterations for algorithm to run. (_Default: 500_)

### Returns
* `total` _(Int)_ -- Number of detected communities.
* `communities` _(List[List[Long]])_ -- Communities sorted by their sizes. Returns largest `top` communities if specified.


#### Notes
* This implementation of LPA incorporated probabilistic elements which makes it non-deterministic; The returned communities may differ on multiple executions.

#### See also
<button onclick="location.href='/algorithms/cbod/'" type="button" class="btn btn-default">
         Outlier Detection</button>
<button onclick="location.href='/algorithms/mlpa/'" type="button" class="btn btn-default">
         Multi-Layer Dynamic Community Detection</button>

## Examples
In this example, the temporal network spans a time period $t \in [1,3]$ and is built into (3) snapshots of window size 1.
 
<p align="center">
	<img src="../../images/lpa-ex.png" style="width: 30vw;" alt="lpa example"/>
</p>


Running LPA on all snapshots;
```scala
curl -X POST 127.0.0.1:8081/RangeAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.LPA",
	"start":1,
	"end":3,
	"jump":1,
	"windowType":"true",
	"windowSize": 1
}
EOF
```

This returns: 

```json
{"time":1,"windowsize":0,"top5":[4],"total":1,"totalIslands":0,"communities": [[1,2,6,5]],"proportion":1.0, "viewTime":36}
{"time":2,"windowsize":0,"top5":[4,2],"total":2,"totalIslands":0,"communities": [[4,3,1,2],[6,5]],"proportion":0.6666667, "viewTime":29}
{"time":3,"windowsize":0,"top5":[3,3],"total":2,"totalIslands":0,"communities": [[5,6,7],[4,1,3]],"proportion":0.5, "viewTime":33}
```
Running LPA on the aggregated graph;
```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.LPA",
	"timestamp":3
}
EOF
```

This returns:

```json
{"time":3,"top5":[4,3],"total":2,"totalIslands":0,"proportion":0.5714286, "communities":[[4,3,2,1],[6,7,5]],"viewTime":30}
```

Specifying that only the largest community be returned (as specified by `top`)

```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.LPA",
	"timestamp":3,
	"args":["1"]
}
EOF
```
This returns:
```json
{"time":3,"top5":[4,3],"total":2,"totalIslands":0,"proportion":0.5714286, "communities":[[3,2,1,4]],"viewTime":33}
```