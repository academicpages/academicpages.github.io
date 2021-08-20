---
title: 'Two-Hop Network'
collection: algorithms
cat: "static"
permalink: /algorithms/twohopnetwork
tags:
  - algorithms

---


<p style="margin-left: 1.5em;"> Returns the 2-hop network of a node `n`.</p>




### Parameters
* `node` _(String)_ -- The name of node `n`.
* `name` _(String)_ -- Node name (_Default: `""`_). If not specified, node will be matched with its assigned ID.
* `neiSize` _(Int)_ -- Number of top neighbors sorted by a `property` to return for every node. If not specified, the full 2-hop network is returned.
* `property` _(String)_ -- Edge property (_Default: `""`_).


### Returns
* `network` _(Map[String, List[String]])_ -- Map of nodes and their neighbor list starting with node `n`.

## Examples
Reading the [LoTR](/documentation/sprouter) dataset, we send a query for a 2hop-network for `Aragorn` and a limit of (3) neighbors.

```scala
curl -X POST 127.0.0.1:8081/ViewAnalysisRequest \
-H "Content-Type: application/json" \
--data-binary @- << EOF
{
  "jsonrpc":"2.0",
  "analyserName":"com.raphtory.algorithms.twoHopNeighbors",
  "serialiserName":"com.raphtory.serialisers.DefaultSerialiser",
  "timestamp":10000,
  "args":["Aragorn","name","3"]
}
EOF
```
This returns the following network;
<p align="center">
  <img src="../../images/2hop-ex.png" style="width: 18vw;" alt="2hop-network example"/>
</p>

 ```json
{"time":10000,
"Aragorn":["Arwen","Denethor","Boromir"],
"Arwen":["Frodo","Elrond","Lúthien"],
"Denethor":["Elendil","Isildur","Gollum"],
"Boromir":["Frodo","Sam","Gimli"],
"viewTime":55}
```