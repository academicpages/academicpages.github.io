---
title: "Building a graph from your data"
collection: documentation
type: "Documentation"
permalink: /documentation/sprouter
order: 2
tags:
  - reading-data
  - graph
---

Now that you have a working version of Raphtory on your machine, the first step to getting your first temporal graph analysis up and running is to tell Raphtory how to read in your datafile and how to build it into a graph. This is done by the Spout and Graph Builder classes respectively. Once these are build they can be passed to a `RaphtoryGraph` which will use the both components to build up the temporal graph.

For this example, we will use a dataset of co-occurrences in the Lord of the Rings books which can be found from [here](https://github.com/Raphtory/Examples/tree/main/src/main/scala/examples/lotr/lotr.csv). This is a `csv` file where each line contains two characters who appeared in the same sentence, along with the number of the sentence in which they appeared. The first line of the file, for example, is `Gandalf,Elrond,33`. However, as you may have guessed from your job in the pervious tutorial running, this is already present in the LOTR example directory `src/main/scala/examples/lotr`. Also in here you will find `LOTRSpout.scala`, `LOTRGraphBuilder.scala` and `LOTRDeployment.scala` which we will go through below.

## Spout

There are three main functions that can be inherited and implemented in the Spout class: `setupDataSource`, `generateData`, `closeDataSource`. With our lotr example, we shall first prepare the data by letting the spout know where to get the data.

```scala
val directory = System.getenv().getOrDefault("LOTR_DIRECTORY", "/absolute/path/to/LOTR/folder").trim
val file_name = System.getenv().getOrDefault("LOTR_FILE_NAME", "lotr.csv").trim
```

We could have just specified `directory` as a string pointing to `"/absolute/path/to/LOTR/folder"` and likewise with `file_name` but wanted to highlight that it is possible to specify these instead as environment variables `LOTR_DIRECTORY` and `LOTR_FILE_NAME`. Next, we implement `setupDataSource` in order to extract the data and it into a queue.

```scala
val fileQueue = mutable.Queue[String]()

  override def setupDataSource(): Unit = {
    fileQueue++=
      scala.io.Source.fromFile(directory + "/" + file_name)
        .getLines
  }
```

Finally, we implement a function `generateData` which sends each line of the file from the queue to the graph builder, using the following code block.

```scala
 override def generateData(): Option[String] = {
    if(fileQueue isEmpty){
      dataSourceComplete()
      None
    }
    else
      Some(fileQueue.dequeue())
  }
```

In this example, there is no need to develop the last function `closeDataSource` but know that it exists for cases where it's necessary.

## Graph Builder

Now we will write the graph builder class, which takes each ingested line of data and converts it to a graph update. The function which does this (and in this case is the only thing we need to define in this class) is `parseTuple`. Let's look at the code for it.

```scala
override def parseTuple(tuple: String) = {

    val fileLine = tuple.split(",").map(_.trim)
    val sourceNode = fileLine(0)
    val srcID = assignID(sourceNode)

    val targetNode = fileLine(1)
    val tarID = assignID(targetNode)

    val timeStamp = fileLine(2).toLong

    sendUpdate(VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character")))
    sendUpdate(VertexAddWithProperties(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character")))
    sendUpdate(EdgeAdd(timeStamp,srcID,tarID, Type("Character Co-occurence")))
  }
}
```

First, we break up the line that has just been ingested by the spout into the relevant components; so, for example, the line `Gandalf,Elrond,33` becomes a tuple `(Gandalf, Elrond, 33)`. For each of the characters seen, we generate them an ID of type `Long`. Finally, we send an update adding both of the vertices to the graph as well as the edge joining them, each with a timestamp of when that update occurred.

There are a few things worth pointing out here.

* We added a `name` property to each of the nodes. If we had reason to, we could have added any other property that might be appropriate. We set this as an `ImmutableProperty` in this case, as character names are treated as fixed, but this could be a mutable property if it were required to change later.

* We didn't check whether either vertices exist before sending a `VertexAdd` update. This is no trouble, another class deals with this so that we don't have to worry about that.

* The spout wasn't doing much heavy lifting here, just reading in the file line by line. Cases where the spout really shines is when it is pulling data from external sources (potentially streams) or extracting the useful parts of less structured data to send as a record to the graph builder.

To summarise, the spout takes an external source of data and turns it into a _stream of records_ and the graph builder converts each item from this stream of records into a _graph update_.

## Raphtory Graph
Now that we have a way to ingest and parse the data we can create a graph. To do this we can first create a scala App. This is a short hand for creating a main function for the Java folks.

````scala
object LOTRDeployment extends App{

}

````

Inside of this we can create a spout and graphbuilder from the classes we have defined above and combine them into a RaphtoryGraph:

````scala
  val source  = new LOTRSpout()
  val builder = new LOTRGraphBuilder()
  val rg = RaphtoryGraph[String](source,builder)

````
---

Once we are able to ingest our data and build graphs from it, the next thing is to actually run some analysis on it. Head onto [Write your own analysis](/documentation/analysis-qs) for how to do the _Six Degrees of Gandalf_ for this dataset!
