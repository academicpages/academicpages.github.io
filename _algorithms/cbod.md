---
title: 'Outlier Detection'
collection: algorithms
type: "Algorithms"
permalink: /algorithms/cbod/
tags:
  - algorithms
  - community-detection
  - outlier-detection

---


<p style="margin-left: 1.5em;"> Returns outliers detected based on the community structure of the graph. </p>

  The algorithm detects nodes that don't have a particular strong connection to their assigned community and rather tend to connect multiple communities. The algorithm runs an instance of LPA on the graph, initially, and then defines an outlier score based on a node's community membership and how it compares to its neighbors community memberships.



### Parameters
* `top`	_(Int)_	-- 	Defines number of nodes with high outlier score to be returned. (_Default: 0_)
                   	If not specified, Raphtory will return the outlier score for all nodes.
* `weight`	_(String)_	-- 	Edge property (_Default: `""`_). To be specified in case of weighted LPA.
* `cutoff`	_(Double)_	-- 	Outlier score threshold. (_Default: 0.0_) 
							Identifies the outliers with an outlier score > `cutoff`.
* `maxIter`	_(Int)_	-- 	Maximum iterations for algorithm to run. (_Default: 500_)

### Returns
* `total` _(Int)_ -- Number of detected outliers.
* `outliers`	_Map(Long, Double)_ 	-- Map of _(node, outlier score)_ sorted by their outlier score.
                  						If specified, returns `top` nodes with outlier score higher than `cutoff`.

#### See also
<button onclick="location.href='/algorithms/lpa/'" type="button" class="btn btn-default">
         Label Propagation Algorithm</button>