---
permalink: /
title: "Raphtory - A practical system for the analysis of temporal graphs"
excerpt: "Raphtory Intro"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---



Raphtory is an open source Distributed Real-Time Temporal Graph Analytics Platforms funded by [The Alan Turing Institute](https://www.turing.ac.uk/research/research-projects/raphtory-practical-system-analysis-dynamic-graphs). This page follows the development of Raphtory including how the tool may be used, recent changes and improvements, the implemented algorithms, and use case examples for temporal graphs.

# Overview

Graph analytics is pivotal in understanding the modern world, especially for business and logistics planning. However, capturing and telling a story with data can be time-consuming and often requires the user to manually refresh the output for an update.   
**Raphtory is the answer to creating dynamic temporal graphs** that could be used anywhere at any time. The goal is to make it easy for you to access accurate, time-sensitive graphs without the burden of reloading the results when you want the latest information. The system is designed with extensibility in mind so that new data types and analysis algorithms can be added to support different use cases.   

## How does the system work?

<p align="center">
  <img src="https://raphtory.github.io/images/overview.png" alt="Figure 1"/>
</p>

<p align="center">
  <em>Figure 1</em>
</p>

Raphtory takes stored or real-time data to create graphs which automatically update without interference of the user. Functions for graph analysis can be defined and then executed across the cluster nodes. The system keeps the history of the graphs as updates come in, which can be accessed later. 

The core components for ingestion and modelling (left rectangle of Figure 1) consist of _Spouts, Graph Routers and Graph Partition Managers (GPMs)_.
Spouts pull tuples from external data that a user specifies and pushes it into the system. The Graph Routers then receive the tuples and update accordingly through a user defined parsing function such as adding, removing, or updating vertices and edges. Next, the GPMs handling the affected entity (the graph) gets the update that needs to be made. 
By dividing these processes (1) a set of data may be modelled into many different graphs by connecting the same Spout to Routers with unique parsing functions or (2) multiple independent sets of data can be joined into one graph by having the same Router connected to various Spouts.  

GPMs handle all operations such as getting graph updates, synchronising with one another, and performing analysis. As updates arrive, GPMs will create entity objects and insert updates into the histories of the affected entities at the correct chronological position. This process allows the system to maintain the same history and removes the need for centralised synchronisation as updates between GPMs may be executed in any order depending on when data arrives. Additionally, messages between routers and GPMs can track the time when the live graph is most recently updated and when the history is synchronised for analysis. 


# Analysis

Once Raphtory is established and ingesting the selected input, analysis of the graph may begin. Analysis Tasks are created when a user submits a query via the Analysis Managers’ REST API (see right of Figure 1 above) and controls the analysis process. Analysis Tasks contain a vertex-centric algorithm defined by the user and also coordinate with the GPMs to execute the algorithm synchronously on the entities they control. These algorithms are implemented via Raphtory’s analysis API which gives the user access to the structural and property histories of the graph. Users may then explore the local neighbourhood of vertices, paths and sub-graphs, and perform analytics across the entire graph. This can be seen in figure 2. 

<p align="center">
  <img src="https://raphtory.github.io/images/analysis.png" alt="Figure 2"/>
</p>

<p align="center">
  <em>Figure 2</em>
</p>

All algorithms in Raphtory are executed on graph flattenings, meaning it takes the temporal graph and views it as a normal graph at a chosen point in time. These can be created at the most recent time (the live real-time graph), or for any point in the graph’s history. Tasks may be set to (1) run over ranges of the history, creating flattenings at set increments, or (2) may run continuously on the live graph, periodically creating flattenings as it updates.  

<p align="center">
  <img src="https://raphtory.github.io/images/windowflattening.png" alt="Figure 3"/>
</p>

<p align="center">
  <em>Figure 3</em>
</p>


In both instances the user may optionally specify a batch of windows which must all be applied at each point in time (see Figure 3). The output from this is a set of windowed flattenings which will show the differing result of the algorithm when varying temporal depth once analysed. To simplify this process for the user, algorithms only require implementing once as they interact with the temporal graph through a Flattening Lens which only returns the entities present once the zenith (point directly above a particular area) and horizon have been applied. 


# Internals

<p align="center">
  <img src="https://raphtory.github.io/images/internals.png" alt="Figure 4"/>
</p>

<p align="center">
  <em>Figure 4</em>
</p>


Raphtorys architecture is based on the actor model, with all components working as actors in an Akka Framework (see Figure 4). Akka provides the foundation for implementing component behaviour and handles both local and remote messaging. A Watchdog actor is present within Raphtory which assigns universally unique identifiers (UUIDs) as Graph Routers and GPMs connect and block ingestion and analysis until the deployment is fully online.  

To simplify the deployment process, Raphtory is packaged as a [docker](https://hub.docker.com/repository/docker/miratepuffin/raphtory) image, allowing it to be distributed as a set of containers over any machines that have docker installed. A deployment will then consist of one main actor per container and Akka/Docker will handle the discovery phase, connecting all actors together. **The user only needs to configure the number/type of partitions, routers and spouts and Raphtory will handle everything else.** This and any other deployment configuration (such as which machines to use) may be orchestrated by either Docker Swarm or Kubernetes with both exposing the system and Raphtory specific metrics to the user via Prometheus, a system that processes time series metric data.  
