---
title: "Installation"
collection: documentation
type: "Documentation"
permalink: /documentation/install
order: 1
tags:
  - quick-start
  - install
---


In this section, you're going to go through the steps to have Raphtory up and running on your local machine.
To make it as easy as possible, an example Raphtory project is available [here](https://github.com/Raphtory/Examples). 

Installing this example requires downloading both the example project and adding(or building) the latest release of Raphtory.

## Clone the example project
This example project can be downloaded by opening your terminal and performing a git clone:
 `git clone https://github.com/Raphtory/Examples.git`


## Adding the latest Raphtory release
The latest release of Raphtory is available [here](https://github.com/Raphtory/Raphtory/releases/latest). Follow the link and download the [raphtory.jar](https://github.com/Raphtory/Raphtory/releases/latest/download/raphtory.jar). Place this within the `lib` directory of the Example project you cloned in the previous step.

Alternatively, both of the above steps can be performed with a single command

`git clone https://github.com/Raphtory/Examples.git raphtory_example && wget https://github.com/Raphtory/Raphtory/releases/latest/download/raphtory.jar -P raphtory_example/lib/`

## Compiling the project 
The example project utilises SBT (scala build tool) to compile the source code. SBT can be installed via this [guide](https://www.scala-sbt.org/1.x/docs/Setup.html). For those who do not want to directly install a working version of SBT is included in the project, just prepend `sbt/bin/` to all of the following commands.

Once installed you can run `sbt compile` to build the project. This should produce an output as below to show it is working correctly:

```
[info] Loading settings for project global-plugins from idea.sbt ...
[info] Loading global plugins from /Users/Mirate/.sbt/1.0/plugins
[info] Loading project definition from /Users/Mirate/github/Examples/project
[info] Loading settings for project examples from build.sbt ...
[info] Set current project to RaphtoryExamples (in build file:/Users/Mirate/github/Examples/)
[info] Executing in batch mode. For better performance use sbt's shell
[info] Compiling 41 Scala sources to /Users/Mirate/github/Examples/target/scala-2.12/classes ...
[warn] there were two feature warnings; re-run with -feature for details
[warn] one warning found
[success] Total time: 12 s, completed 08-Dec-2020 22:35:31

```

## Test run to make sure its all working
To test that you have Raphtory working properly on your machine, run:

```sh
sbt/bin/sbt run examples.lotr.LOTRDeployment
```

This will run the Lord of the Rings example that we shall rebuild over the next couple of tutorials and give some example output as follows:


This is the system starting up and is mostly unimportant unless there are any errors reported.

````
[info] Loading settings for project global-plugins from idea.sbt ...
[info] Loading global plugins from /Users/Mirate/.sbt/1.0/plugins
[info] Loading project definition from /Users/Mirate/github/Examples/project
[info] Loading settings for project examples from build.sbt ...
[info] Set current project to RaphtoryExamples (in build file:/Users/Mirate/github/Examples/)
[info] running examples.lotr.LOTRDeployment
22:36:41.706 [run-main-0] WARN  kamon.Init - Failed to attach the instrumentation because the Kamon Bundle is not present on the classpath
22:36:41.855 [run-main-0] INFO  kamon.prometheus.PrometheusReporter - Started the embedded HTTP server on http://0.0.0.0:11600
22:36:42.207 [Citation-system-akka.actor.default-dispatcher-3] INFO  akka.event.slf4j.Slf4jLogger - Slf4jLogger started
22:36:42.229 [Citation-system-akka.actor.default-dispatcher-3] INFO  akka.remote.Remoting - Starting remoting
22:36:47.389 [Citation-system-akka.actor.default-dispatcher-2] INFO  akka.remote.Remoting - Remoting started; listening on addresses :[akka.tcp://Citation-system@192.168.2.2:1600]
22:36:47.390 [Citation-system-akka.actor.default-dispatcher-2] INFO  akka.remote.Remoting - Remoting now listens on addresses: [akka.tcp://Citation-system@192.168.2.2:1600]
22:36:47.406 [Citation-system-akka.actor.default-dispatcher-2] INFO  a.c.Cluster(akka://Citation-system) - Cluster Node [akka.tcp://Citation-system@192.168.2.2:1600] - Starting up, Akka version [2.5.26] ...
22:36:47.455 [Citation-system-akka.actor.default-dispatcher-4] INFO  a.c.Cluster(akka://Citation-system) - Cluster Node [akka.tcp://Citation-system@192.168.2.2:1600] - Registered cluster JMX MBean [akka:type=Cluster]
22:36:47.456 [Citation-system-akka.actor.default-dispatcher-4] INFO  a.c.Cluster(akka://Citation-system) - Cluster Node [akka.tcp://Citation-system@192.168.2.2:1600] - Started up successfully
22:36:47.495 [Citation-system-akka.actor.default-dispatcher-19] INFO  a.c.Cluster(akka://Citation-system) - Cluster Node [akka.tcp://Citation-system@192.168.2.2:1600] - No seed-nodes configured, manual cluster join required, see https://doc.akka.io/docs/akka/current/cluster-usage.html#joining-to-seed-nodes
22:36:47.501 [Citation-system-akka.actor.default-dispatcher-3] WARN  akka.cluster.AutoDown - Don't use auto-down feature of Akka Cluster in production. See 'Auto-downing (DO NOT USE)' section of Akka Cluster documentation.
````

This shows that the ingestion components of Raphtory have come online and as such the system is ready for analysis to be performed. The `All data sent` message comes from the spout informing us that it has finished ingesting the input file.


````
22:36:49.678 [Citation-system-akka.actor.default-dispatcher-18] INFO  c.r.c.a.C.RaphtoryReplicator - Router 0 has come online.
22:36:49.678 [Citation-system-akka.actor.default-dispatcher-18] INFO  c.r.c.a.C.RaphtoryReplicator - Partition Manager 0 has come online.
22:37:09.665 [Citation-system-akka.actor.default-dispatcher-62] INFO  c.r.c.a.ClusterManagement.WatchDog - Partition managers and min. number of Routers have joined cluster.
Number of routers: 1
Number of partitions: 1
Cluster ready for Analysis
All data sent
````

This is confirmation that our analysis jobs have been submitted (We will come back to this soon don't worry) and that the times they are requesting are yet to be available (and shall be retried soon).


````
Range Analysis Task received, your job ID is com.raphtory.algorithms.ConnectedComponents_1607467033414, running com.raphtory.algorithms.ConnectedComponents, between 1 and 32674 jumping 100 at a time.
Range Analysis Task received, your job ID is com.raphtory.algorithms.ConnectedComponents_1607467033423, running com.raphtory.algorithms.ConnectedComponents, between 1 and 32674 jumping 100 at a time.
View Analysis Task received, your job ID is com.raphtory.algorithms.DegreeBasic_1607467033424
Range Analysis Task received, your job ID is com.raphtory.algorithms.ConnectedComponents_1607467033426, running com.raphtory.algorithms.ConnectedComponents, between 1 and 32674 jumping 100 at a time.
View Analysis Task received, your job ID is com.raphtory.algorithms.DegreeBasic_1607467033428
View Analysis Task received, your job ID is com.raphtory.algorithms.DegreeBasic_1607467033430
10000 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
1 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
10000 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
1 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
1 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
10000 is yet to be ingested, currently at 0. Retrying analysis in 10 seconds and retrying
````

Finally, output for the example queries should begin streaming to the terminal such as below. Don't worry too much about this at the moment as again it will be covered later, this does mean though that Raphtory is working correctly and you can move on to creating your first graph to analyse.


````
{"time":10000,"vertices":84,"edges":262,"degree":3.119047619047619}
View Analysis manager for com.raphtory.algorithms.DegreeBasic_1607467033424 at 10000 finished
{"time":10000,"windowsize":100,"vertices":4,"edges":3,"degree":0.75},
View Analysis manager for com.raphtory.algorithms.DegreeBasic_1607467033430 at 10000 finished
{"time":10000,"windowsize":100,"vertices":4,"edges":3,"degree":0.75},
{"time":10000,"windowsize":50,"vertices":2,"edges":1,"degree":0.5},
{"time":10000,"windowsize":10,"vertices":0,"edges":0,"degree":NaN},
View Analysis manager for com.raphtory.algorithms.DegreeBasic_1607467033428 at 10000 finished
{"time":1,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":10205},
{"time":1,"windowsize":100,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":10215},
{"time":1,"windowsize":100,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":10219},
{"time":1,"windowsize":50,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":10219},
{"time":1,"windowsize":10,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":10219},
{"time":101,"top5":[2],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":0,"viewTime":74},
{"time":101,"windowsize":100,"top5":[2],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":0,"viewTime":65},
{"time":101,"windowsize":100,"top5":[2],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":0,"viewTime":69},
{"time":101,"windowsize":50,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":69},
{"time":101,"windowsize":10,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":69},
{"time":201,"top5":[2,2,2],"total":3,"totalIslands":0,"proportion":0.33333334,"clustersGT2":0,"viewTime":23},
{"time":201,"windowsize":100,"top5":[2,2],"total":2,"totalIslands":0,"proportion":0.5,"clustersGT2":0,"viewTime":27},
{"time":201,"windowsize":100,"top5":[2,2],"total":2,"totalIslands":0,"proportion":0.5,"clustersGT2":0,"viewTime":25},
{"time":201,"windowsize":50,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":25},
{"time":201,"windowsize":10,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":25},
{"time":301,"top5":[6,2],"total":2,"totalIslands":0,"proportion":0.75,"clustersGT2":1,"viewTime":31},
{"time":301,"windowsize":100,"top5":[5],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":1,"viewTime":30},
{"time":301,"windowsize":100,"top5":[5],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":1,"viewTime":43},
{"time":301,"windowsize":50,"top5":[4],"total":1,"totalIslands":0,"proportion":1.0,"clustersGT2":1,"viewTime":43},
{"time":301,"windowsize":10,"top5":[0],"total":0,"totalIslands":0,"proportion":0.0,"clustersGT2":0,"viewTime":43},
{"time":401,"top5":[8,4,2,2,2],"total":6,"totalIslands":0,"proportion":0.4,"clustersGT2":2,"viewTime":42},

````


---
Now that you have Raphtory set up, the next step is to learn to build a spout and router to ingest data. Check the next entry: [Write your first Spout/Router](/documentation/sprouter)
