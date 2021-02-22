---
title: 'Write your own analysis'
collection: documentation
type: "Documentation"
permalink: /documentation/analysis-qs
order: 3
tags:
  - quick-start
  - analysis
---

In the previous entry, you learnt how to write your own spout and router to ingest the data. In here, we will show you how to write an analyser that will run algorithms that you could test with your data. 

Depending on the type of algorithm that you want to implement, a set of modules need to be defined:

`setup` -- runs only for the first superstep and generally implements initial conditions and states of the graph entities;  
`analyse` -- implements the main block of you algorithm;  
`returnResults` -- returns the result of every partition and formats it for the final stage;  
`processresults` -- processes all returned results of the partitions to be displayed, stored or transferred;  
`defineMaxSteps` -- defines the maximum number of supersteps the algorithms iterates over.


Since Raphtory is vertex-centric, a good intuition to keep when building algorithms in Raphtory is to view the process from a vertex perspective.

## Six Degrees of Gandalf
To continue with the LOTR example done previously in the [spout tutorial](https://raphtory.github.io/documentation/sprouter), we're going to go over how to write an analyser for the LOTR data that will get the size of the _six degrees of separation_ network for a character; in this case,`Gandalf`. Six degrees of separation is "the idea that all people on average are six, or fewer, social connections away from each other." ([wiki here in case you want to know more](https://en.wikipedia.org/wiki/Six_degrees_of_separation)).

The example file can be found in the path `src/main/scala/examples` in the example directory cloned in the [installation guide](https://raphtory.github.io/documentation/install).

### Pre-step
First, we need to create a property to store the state of _separation_ and initialize it in `setup`.

```scala
override def setup(): Unit = {
    var sep_state = 0
    view.getVertices().foreach{vertex =>
      val name = vertex.getPropertyValue("name").getOrElse("")
      if (name == "Gandalf"){
        sep_state = SEP //user-defined parameter to determine degree of separation
      }else{
        sep_state = 0
      }
      vertex.setState("separation", sep_state)
      vertex.messageAllNeighbours(sep_state)
    }
}
```
`view` represents the graph that is currently in _view_, meaning the graph that incorporates all updates in the time period of the specified analysis window. So, if a character appears outside of this window, the function `view.getVertices()` will exclude it. Once a vertex state is initialized, it sends its state to its neighbours through `messageAllNeighbours`.

### The bulk
As mentioned before, the `analyse` module implements the bulk of the algorithm. In here, the state of the source is viewed as a resource that is spread throughout the network and depletes every time it reaches a node until it vanishes (`state = 0`). The process starts by filtering the vertices that got messages through `getMessagedVertices()`. Every vertex then processes its messages `vertex.messageQueue[Int]` to get the state of its neighbours. Comparing that with its own state, it updates it and sends out the update if necessary.

```scala
override def analyse(): Unit = {
    view.getMessagedVertices().foreach { vertex =>
      val sep_state = vertex.messageQueue[Int].max -1
      if ((sep_state > 0) & (sep_state > vertex.getState[Int]("separation"))) {
        vertex.setState("separation", sep_state)
        vertex.messageAllNeighbours(sep_state)
      }
    }
  }
```
The above code runs until no more messages are sent (or the number of steps reaches `defineMaxSteps`).This means that all nodes in the _six degrees of separation_ network have updated their states with how far they are from the source.

### The Return of The King
Now that the algorithm has converged, we need to get the results back and process them if necessary. The following filters the results by only returning the vertices that have their states updated and are reachable in under a number of hops to `Gandalf`. It also groups the results by their separation degree and returns the size of each group.

```scala
override def returnResults(): Any =
    view.getVertices()
      .filter(vertex => vertex.getState[Int]("separation") > 0)
      .map(v => (v.ID(), v.getState[Int]("separation")))
      .groupBy(f => f._2)
      .map(f => (f._1, f._2.size))
```
Remember that Raphtory is a distributed platform and runs the algorithms in parallel with multiple workers (see [overview](https://raphtory.github.io/) for more detail). This means that the module `returnResults` only returns the results for the vertices that are stored in every partition.

To put it all together, in the final module `processResults`, the results of every partition are grouped together and some extra processing is performed if necessary. In this case, we group the results to get the size of the network as well as the number of characters that have directly interacted with `Gandalf`.

```scala
override def processResults(results: ArrayBuffer[Any], timestamp: Long, viewCompleteTime: Long): Unit = {
    val endResults = results.asInstanceOf[ArrayBuffer[immutable.ParHashMap[Int, Int]]]
    try {
      val grouped = endResults.flatten.groupBy(f => f._1).mapValues(x => x.map(_._2).sum)
      val direct = if (grouped.size>0) grouped(SEP-1) else 0
      val total = grouped.values.sum
      val text = s"""{"time":$timestamp,"total":${total},"direct":${direct},"viewTime":$viewCompleteTime}"""
      println(text)
    } catch {
      case e: UnsupportedOperationException => println("null")
    }
  }
```

## Running Analysis
To run your implemented analyser or any of the algorithms included in the most recent Raphtory Release ([See here](https://github.com/Raphtory/Raphtory/tree/master/mainproject/src/main/scala/com/raphtory/algorithms)), you must submit them to the graph. You can either request a `viewQuery` to look at a single point in time or a range query over a subset of the history of the graph.

Some example view queries are found within the `LOTRDeployment` App we created in the previous tutorial:

View queries take the Analyser you wish to run, a timestamp specifying the time of interest and any arguments (which can be an empty array). You may additionally specify a window which will filter the graph to only include entities which have been updated within that period from the time point chosen. This may be expanded to a batch of windows which will do the same for all sizes provided. An example of all three of these running a `DegreeBasic` function on line 10000 can be seen below:

````scala
  rg.viewQuery(DegreeBasic(),timestamp = 10000,arguments)
  rg.viewQuery(DegreeBasic(),timestamp = 10000,window=100,arguments)
  rg.viewQuery(DegreeBasic(),timestamp = 10000,windowBatch=Array(100,50,10),arguments)
````

Range queries are similar to this, but take a start time, end time (inclusive) and increment with which it moves between these two points. An example of range queries over the full history (all pages) running `ConnectedComponents` can be seen below:

````scala
  rg.rangeQuery(ConnectedComponents(),start = 1,end = 32674,increment = 100,arguments)
  rg.rangeQuery(ConnectedComponents(),start = 1,end = 32674,increment = 100,window=100,arguments)
  rg.rangeQuery(ConnectedComponents(),start = 1,end = 32674,increment = 100,windowBatch=Array(100,50,10),arguments)
  rg.viewQuery(SixDegreesOfGandalf(),timestamp = 5000,arguments)
````

Finally we can see an Implemented version of the `SixDegreesOfGandalf` run as a range query over all pages. Running this on line 5000 of the books, returns the following JSON data.

```json
{"time":5000,"total":24,"direct":9,"viewTime":316}
```
This data tells us that there are a total of 24 nodes: 14 nodes are connected to the 9 nodes that are directly connected to Gandalf. This gives a degree of separation of 3.  

Delete the queries that are in the file and write your own to get this output. Once you are happy with this you should have all the tools needed to create graphs for your own datasets. If you have any questions, come join the Raphtory Slack and get involved with the discussion! :) 

