---
permalink: /
title: "Raphtory - A practical system for the analysis of temporal graphs"
excerpt: "Raphtory Intro"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---



Raphtory is an open source Distributed Real-Time Temporal Graph Analytics Platforms funded by [The Alan Turing Institute](https://www.turing.ac.uk/research/research-projects/raphtory-practical-system-analysis-dynamic-graphs). This page follows the developement of Raphtory posting about how the tool may be used, recent changes and improvments, the implemented algorithms and example usecases for temporal graphs.


# Raphtory Overview

Raphtory is a distributed system that takes any source of data (either previously stored, or a real time stream), and creates a dynamic temporal graph that is partitioned over multiple machines. In addition to maintaining this model, graph analysis functions can be defined that will be executed across the cluster nodes, and will have access to the full history of a graph. Raphtory is designed with extensibility in mind; new types of data, as well as new analysis algorithms can be added to the base project, in order to support additional use cases. 

<p align="center">
  <img src="https://raphtory.github.io/images/overview.pdf" alt="Raphtory diagram"/>
</p>

Raphtorys core components for modelling and ingestion consist of Spouts, Graph Routers and Graph Partition Managers. These can be seen on the left of the overview above. Spouts attach to a user specified data source external to Raphtory. Tuples are then pulled from this source and pushed into the system. These raw data tuples are received by the Graph Routers which convert each into graph updates via a user defined parsing function; adding, removing or updating vertices and edges. Updates are then forwarded to the Graph Partition Manager handling the affected entity. By decoupling these processes the same data may be modelled as many different graphs by connecting the same Spout to Routers with unique parsing functions or, alternatively, the same Router may be connected to various Spouts pulling from independent data sources to join them into one graph.

Graph Partition Managers, as their name suggests, handle all operations of the partition, ingesting graph updates, synchronising with peers and performing analysis. As updates arrive via the pool of Graph Routers the Manager will  create entity objects as required and insert updates into the histories of affected entities at the correct chronological position. This removes the need for centralised synchronisation as updates and inter-manager messages may be executed in any given arrival order whilst still resulting in the same history. However, messages between routers and partition managers are additionally watermarked to track the most recent update time (the live graph) and to know when in the graphs history is synchronised and, therefore, safe to analyse.

# Raphtory Analysis

Once Raphtory is established and ingesting the selected input, analysis of the graph may begin. This is controlled via Analysis Tasks which are spawned when a user submits a query via the Analysis Managers REST API; seen on the right of the overview above. Analysis Tasks contain a user defined vertex centric algorithm and coordinate with the Partition Managers to execute this in bulk synchronous parallel supersteps on the entities they control. These
algorithms are implemented via Raphtorys analysis API which gives the user access to the structural and property histories of all entities. Through this they may explore the local neighbourhood of a vertex, paths and sub-graphs and perform analytics across the entire graph. This can be seen in the image below. 

<p align="center">
  <img src="https://raphtory.github.io/images/analysis.pdf" alt="Raphtory diagram"/>
</p>

All algorithms in Raphtory are executed on graph flattenings, taking the temporal graph and viewing a normal graph at a chosen point in time. These can be created at the the most recent time (the live real-time graph), or for any point back through the graphs history. Tasks may be set to run over ranges of the history, creating flattenings at set increments, or may run continuously on the live graph, periodically creating flattenings as it updates. 
In both instances the user may optionally specify a batch of windows which must all be applied at each point in time. The output from this being a set of windowed flattenings which once analysed will show the differing result of the algorithm when varying temporal depth. To simplify this process for the user, algorithms only require implementing once as they interact with the temporal graph through a Flattening Lens which only returns the entities present once the zenith and horizon have been applied. This may be seen at the bottom of the figure above and in more detail in the picture below.

<p align="center">
  <img src="https://raphtory.github.io/images/windowflattening.pdf" alt="Raphtory diagram"/>
</p>


# Raphtory Internals

<p align="center">
  <img src="https://raphtory.github.io/images/internals.pdf" alt="Raphtory diagram"/>
</p>

Raphtorys architecture is based on the actor model, with all components implemented as actors utilising the Akka Framework; as can be seen at the top of figure above. Akka provides the foundation for implementing component behaviour and handles all messaging both local and remote. An additional Watchdog actor is then also present within Raphtory which assigns UUIDs as Graph Routers and Partition Managers connect and blocks ingestion/analysis until the deployment is fully online. 

To simplify the deployment process, Raphtory is packaged as a [docker image](https://hub.docker.com/repository/docker/miratepuffin/raphtory), allowing it to be distributed as a set of containers over any machines which have docker installed. A deployment will then consist of one main actor per container and Akka/Docker will handle the discovery phase, connecting all actors together. This means the user just needs to configure the number/type of partitions, routers and spouts and Raphtory will handle everything else. This and any other deployment configuration (such as which machines to use) may be orchestrated by either Docker Swarm or Kubenetes with both exposing the system and Raphtory specific metrics to the user via Prometheus.  