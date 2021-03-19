---
title: 'Temporal Motif Counting'
collection: algorithms
type: "Algorithms"
permalink: /algorithms/tmotifcount/
tags:
  - algorithms
  - temporal motifs
  - motif counting

---


<p style="margin-left: 1.5em;"> Returns the number of 2-edge temporal motifs for every node in the graph.</p>

 The algorithms identifies 2-edge-1-node temporal motifs; It detects two types of motifs:

 	_Type-1_: Detects motifs that exhibit incoming flow followed by outgoing flow in the form;

<p align="center">
	<img src="../../images/mc1.png" style="width: 11vw;" alt="mc type 1"/>
</p>
    
_Type-2_: Detects attribute-based motifs that exhibit a non-negative balance while maintaining the temporal pattern of Type-1 i.e. on average, a larger incoming weight is followed by a lesser outgoing weight in the form;
<p align="center">
	<img src="../../images/mc2.png" style="width: 16vw;" alt="mc type 2"/>
</p>

### Parameters
* `top` _(Int)_ -- The number of nodes with highest number of motifs to return. (_Default: 0_)
                      If not specified, Raphtory will return the motif count of all nodes that observe the motifs.
* `weight` _(String)_ -- Edge property (_Default: `"weight"`_). To be specified for type-2 motifs.
* `delta` _(Long)_ -- The size of the window in time to search for motifs where the length of the motif must be `< delta`.

### Returns
* `total` _(Int)_ -- Number of nodes that exhibit a temporal motif.
 * `motifs` _(Map)_ -- A dictionary of average number of motifs for _Type-1_ and _Type-2_ per node.


## Examples
Given the data table below, a temporal graph spanning three time periods can be constructed.
 
<table style="width:30%"><thead><tr><th>time</th><th>source</th><th>target</th><th>weight</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>2</td><td>1</td><td>2</td><td>7</td></tr><tr><td>3</td><td>1</td><td>3</td><td>5</td></tr><tr><td>3</td><td>2</td><td>3</td><td>3</td></tr><tr><td>3</td><td>3</td><td>4</td><td>9</td></tr></tbody></table>

Running the algorithm on the temporal network at $t=3$ with a $\delta = 3$;
```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.MotifCounting",
	"timestamp":3,
	"args":["0", "weight", "3"]	
}
EOF
```

Returns two nodes that observe temporal motifs of type T-1/T-2: 

```json
{"time":3,"total": 2, "motifs":{ "2":{"mc1":0.4, "mc2":1.0},"3":{"mc1":0.3333333333333333, "mc2":0.0} },"viewTime":10168}
```