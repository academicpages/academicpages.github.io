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

Now that you have a working version of Raphtory on your machine, the first step to getting your first temporal graph analysis up and running is to tell Raphtory how to read in your datafile and how to build it into a graph. This is done by the Spout and Router classes respectively.

For this example, we will use a dataset of co-occurrences in the Lord of the Rings books which can be downloaded from [here](https://github.com/Raphtory/Raphtory/blob/6836d23f0ca1da4f2f8354f0d648bfe249241761/mainproject/cluster/src/main/scala/com/raphtory/examples/lotr/lotr.csv). This is a `csv` file where each line contains two characters who appeared in the same sentence, along with the number of the sentence in which they appeared. The first line of the file, for example, is `Gandalf,Elrond,33`.

## Spout

Firstly, we will tell Raphtory where to find the datafile with the following few lines to be placed within the Spout class.

```scala
val directory = System.getenv().getOrDefault("LOTR_DIRECTORY", "/absolute/path/to/LOTR/folder").trim
val file_name = System.getenv().getOrDefault("LOTR_FILE_NAME", "lotr.csv").trim
val fileLines = io.Source.fromFile(directory + "/" + file_name).getLines.toArray
```

We could have just specified `directory` as a string pointing to `"/absolute/path/to/LOTR/folder"` and likewise with `file_name` but wanted to highlight that it is possible to specify these instead as environment variables `LOTR_DIRECTORY` and `LOTR_FILE_NAME`. In any case, these lines of code will take our datafile and extract from it all the lines, as an array of strings `fileLines`.

The next few lines of code;
```scala
var position    = 0
var linesNumber = fileLines.length
println("Start: " + LocalDateTime.now())
```
set up some variables prior to ingesting the file lines.

Finally, we implement a function `ProcessSpoutTask` which ingests each line of the file, using the following code block.

```scala
protected def ProcessSpoutTask(message: Any): Unit = message match {
  case StartSpout => AllocateSpoutTask(Duration(1, NANOSECONDS), "newLine")
  case "newLine" =>
    if (position < linesNumber) {
      var line = fileLines(position)
      sendTuple(line)
      position += 1
      AllocateSpoutTask(Duration(1, NANOSECONDS), "newLine")
    }
  case _ => println("message not recognized!")
}
```

This goes through each line of the file and sends it to the Router via `sendTuple` where it will be translated into an update to the graph (e.g. adding a node or edge).

## Router

Now we will write the router class, which takes each ingested line of data and converts it to a graph update. The function which does this (and in this case is the only thing we need to define in this class) is `parseTuple`. Let's look at the code for it.

```scala
def parseTuple(record: Any): Unit = {

  val fileLine = record.asInstanceOf[String].split(",").map(_.trim)

  val sourceNode = fileLine(0)
  val srcID = assignID(sourceNode)

  val targetNode = fileLine(1)
  val tarID = assignID(targetNode)

  val timeStamp = fileLine(2).toLong

  sendGraphUpdate(VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character")))
  sendGraphUpdate(VertexAddWithProperties(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character")))
  sendGraphUpdate(EdgeAdd(timeStamp,srcID,tarID, Type("Character Co-occurence")))
}
```

First, we break up the line that has just been ingested by the spout into the relevant components; so, for example, the line `Gandalf,Elrond,33` becomes a tuple `(Gandalf, Elrond, 33)`. For each of the characters seen, we generate them an ID of type `Long`. Finally, we send an update adding both of the vertices to the graph as well as the edge joining them, each with a timestamp of when that update occurred.

There are a few things worth pointing out here.

* We added a `Name` property to each of the nodes. If we had reason to, we could have added any other property that might be appropriate. We set this as an `ImmutableProperty` in this case, as character names are treated as fixed, but this could be a mutable property if it were required to change later.

* We didn't check whether either vertices exist before sending a `VertexAdd` update. This is no trouble, another class deals with this so that we don't have to worry about that.

* The spout wasn't doing much heavy lifting here, just reading in the file line by line. Cases where the spout really shines is when it is pulling data from external sources (potentially streams) or extracting the useful parts of less structured data to send as a record to the router.

To summarise, the spout takes an external source of data and turns it into a _stream of records_ and the router converts each item from this stream of records into a _graph update_.

---

Once we are able to ingest our data and build graphs from it, the next thing is to actually run some analysis on it. Head onto [Write your own analysis](/documentation/analysis-qs) for how to do the Six Degrees of Gandalf for this dataset!
