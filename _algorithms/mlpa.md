---
title: 'Multi-Layer Dynamic Community Detection'
collection: algorithms
type: "Algorithms"
permalink: /algorithms/mlpa/
tags:
  - algorithms
  - dynamic community-detection
  - multi-layer graph
  - cross-time detection

---


<p style="margin-left: 1.5em;"> Returns the communities of a multi-layer graph as detected by synchronous label propagation.</p>

  This transforms the temporal network into a multi-layer graph by flattening the network into snapshots (layers); the temporal instances of the same vertex on different layers are handled as distinct vertices. The algorithm then runs a version of LPA on this view of the graph and returns communities that
  share the same label. These communities can span vertices on the same layer (spatial grouping) and other layers (temporal grouping).

### Parameters
* `top` _(Int)_ -- The number of top largest communities to return. (_Default: 0_)
                      If not specified, Raphtory will return all detected communities.
* `weight` _(String)_ -- Edge property (_Default: `""`_). To be specified in case of weighted graph.
* `maxIter` _(Int)_ -- Maximum iterations for algorithm to run. (_Default: 500_)
* `start` _(Long)_   -- Oldest time in the graph events.
* `end` _(Long)_     -- Newest time in the graph events.
* `layerSize` _(Long)_ -- Size of a single layer that spans all events occurring within this period.
* `omega` _(Long)_    -- Weight of inter-layer coupling. This is the weight of temporal edges linking two persisting instances of a node between layers. (_Default: 1_) 
					If "average", the weights are assigned based on an average weight of the neighborhood of a node.

### Returns
* `total` _(Int)_ -- Number of detected communities.
* `communities` _(List[List[Long]])_ -- Communities sorted by their sizes where every member is in the form `vID_layerID`. Returns largest `top` communities if specified.


#### See also
<button onclick="location.href='/algorithms/lpa/'" type="button" class="btn btn-default">
         Label Propagation Algorithm</button>

## Examples
The temporal network in the figure is a weighted dynamic graph spanning a time period $t \in [1,3]$ with edge property `weight`; and is built into (3) snapshots of window size 1.
 
<p align="center">
	<img src="../../images/mlpa-eg
	.png" style="width: 30vw;" alt="mlpa example"/>
</p>


Running the algorithm with a weak inter-layer coupling ($\omega = 1$);
```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.MultilayerLPA",
	"timestamp":3,
	"args":["0", "weight", "10", "1", "3", "1", "1"]
}
EOF
```

Returns communities of every layer as if the layers are disconnected: 

```json
{"time":3,"top5":[4,3,2],"total":3,"totalIslands":0,"communities": [[3_3,4_3,1_3,2_3],[3_1,1_1,2_1],[1_2,2_2]], "viewTime":47}
```

Running again with `average` as method for inter-layer coupling;
```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF 
{
	"jsonrpc":"2.0",
	"analyserName":"com.raphtory.algorithms.MultilayerLPA",
	"timestamp":3,
	"args":["0", "weight", "10", "1", "3", "1", "average"]
}
EOF
```

Returns communities that span multiple layers:

```json
{"time":3,"top5":[4,3,2],"total":3,"totalIslands":0,"communities": [[1_2,1_3,2_2,2_3],[3_1,1_1,2_1],[3_3,4_3]], "viewTime":95}
```