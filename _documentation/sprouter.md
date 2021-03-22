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

The first step to getting your first temporal graph analysis up and running is to tell Raphtory how to read your datafile and how to build it into a graph. 

Two classes help with this:
- Spout helps with reading the data file
-	Graph builder helps build the graph  

Once these are built, they can be passed to `RaphtoryGraph` which will use both components to build the temporal graph.  

If you have downloaded the [example](https://github.com/Raphtory/Examples.git) folder from the [installation](https://raphtory.github.io/documentation/install) guide, then the below LOTR example is already set up. If not, please download it.  

The examples are found within the path `src/main/scala/examples`.  

For this example, we will use a dataset that tells us when two characters show up at the same time in the Lord of the Rings books. The `csv` file (comma-separated values) in the examples folder can be found [here](https://github.com/Raphtory/Examples/blob/main/src/main/scala/examples/lotr/lotr.csv), and each line contains two characters that appeared in the same sentence in the book, along with which sentence they appeared as indicated by a number. In the example, the first line of the file is `Gandalf,Elrond,33` which tells us that Gandalf and Elrond appears together in sentence 33.  

Also, in the examples folder you will find `LOTRSpout.scala`, `LOTRGraphBuilder.scala` and `LOTRDeployment.scala` which we will go through in detail.


## Spout

Let's continue with the LOTR example.  

There are three main functions that can be inherited and implemented in the Spout class: `setupDataSource`, `generateData`, `closeDataSource`. First, prepare the data by letting the spout know where to get the data. There are two ways to do this.  

We can get the location with environment variables,

```scala
val directory = System.getenv().getOrDefault("LOTR_DIRECTORY", "/absolute/path/to/LOTR/folder").trim
val file_name = System.getenv().getOrDefault("LOTR_FILE_NAME", "lotr.csv").trim
```

**Or**, specify `directory` as a string pointing to `"/absolute/path/to/LOTR/folder"` and likewise with `file_name`. Next, we implement `setupDataSource` in order to extract the data and put it into a queue.

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

    addVertex(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character"))
    addVertex(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character"))
    addEdge(timeStamp,srcID,tarID, Type("Character Co-occurence"))
  }
}
```

First, we break up the line that has just been ingested by the spout into the relevant components; so, for example, the line `Gandalf,Elrond,33` becomes a tuple `(Gandalf, Elrond, 33)`. For each of the characters seen, we give them an ID of type `Long`. Finally, we send an update adding both of the vertices to the graph as well as the edge joining them, each with a timestamp of when that update occurred.

There are a few things worth pointing out here.

* We added a `name` property to each of the nodes. If we had reason to, we could have added any other property that might be appropriate. We set this as an `ImmutableProperty` in this case, as character names are treated as fixed, but this could be a mutable property if it were required to change later.

* We didn't check whether either vertices exist before sending a `addVertex` update. Another class deals with this so that we don't have to worry about that.

* The spout wasn't doing much heavy lifting here, just reading in the file line by line. The spout is used for pulling data from external sources (potentially streams) or extracting the useful parts of less structured data to send as a record to the graph builder.

To summarise, the spout takes an external source of data and turns it into a _stream of records_ and the graph builder converts each item from this stream of records into a _graph update_.

## Raphtory Graph
Now that we have a way to ingest and parse the data we can create a graph. To do this we can first create a scala app. `Extends App` is a short hand for creating a main function for Java.

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

Once we are able to ingest our data and build graphs from it, the next thing is to run analysis on it. Head to [Write your own analysis](/documentation/analysis-qs) for how to do the _Six Degrees of Gandalf_ for this dataset!
