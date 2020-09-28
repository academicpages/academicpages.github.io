---
title: "Installation"
collection: documentation
type: "Documentation"
permalink: /documentation/sprouter
tags:
  - reading-data
  - graph
---

Now that you have a working version of Raphtory on your machine, the first step to getting your first temporal graph analysis up and running is to tell Raphtory how to read in your datafile and how to build it into a graph. This is done by the Spout and Router classes respectively.

For this example, we will use a dataset of co-occurrences in the Lord of the Rings books which can be downloaded from LINK. This is a csv file where each line contains two characters who appeared in the same sentence, along with the number of the sentence in which they appeared.

## Spout

Firstly we will tell Raphtory where to find the datafile with the following few lines to be placed within the Spout class.

```scala
val directory = System.getenv().getOrDefault("LOTR_DIRECTORY", "/path/to/LOTR/folder").trim
val file_name = System.getenv().getOrDefault("LOTR_FILE_NAME", "lotr.csv").trim
val fileLines = io.Source.fromFile(directory + "/" + file_name).getLines.drop(1).toArray
```

---
