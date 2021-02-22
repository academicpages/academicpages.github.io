---
title: 'Minor Router API updates'
date: 2021-02-18
permalink: /blog/2020/02/minor-router-api-updates/
tags:
  - minor update
  - development
  - api update

---

We have updated the Router API to make it cleaner. This applies to Raphtory version 0.11 onwards that will be live from 1st March. Previously the coder needed to say SendUpdate and wrap this around the type of update that was being performed. The API now simply allows the user to directly make the update.

The new API looks like this. To add a vertex or edge, optionally with properites or types.
```
addVertex(updateTime: Long, srcId: Long)
addVertex(updateTime: Long, srcId: Long, properties: Properties)
addVertex(updateTime: Long, srcId: Long, vertexType: Type)
addVertex(updateTime: Long, srcId: Long, properties: Properties, vertexType: Type)
addEdge(updateTime: Long, srcId: Long, dstId: Long)
addEdge(updateTime: Long, srcId: Long, dstId: Long, properties: Properties)
addEdge(updateTime: Long, srcId: Long, dstId: Long, edgeType: Type)
addEdge(updateTime: Long, srcId: Long, dstId: Long, properties: Properties, edgeType: Type)
```
To remove a vertex or edge:
```
deleteVertex(updateTime: Long, srcId: Long)
deleteEdge(updateTime: Long, srcId: Long)
```

Here's some examples of how they might look in practice:
```
addVertex(timeStamp1,srcNode)
addEdge(timeStamp1,srcNode,dstNode)
addVertex(timeStamp2,nodeA,ImmutableProperty("Vertex Property",srcName))
addVertex(timeStamp2,nodeB,Type("Vertex Type"))
addVertex(timeStamp2,nodeB,ImmutableProperty("Another Vertex Property",srcName), Type("Another Vertex Type"))
addEdge(timeStamp2, nodeA, nodeB)
addEdge(timeStamp2, nodeA, nodeC, ImmutableProperty("Edge Property",srcName), Type("Edge Type"))
deleteVertex(timeStamp3, srcId)
deleteEdge(timeStamp3, nodeA, nodeB)
```

So previously your code might look like this:
```
sendUpdate(VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character")))
sendUpdate(VertexAddWithProperties(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character")))
sendUpdate(EdgeAdd(timeStamp,srcID,tarID, Type("Character Co-occurence")))
```

Your updated code should look like this:
```
addVertex(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character"))
addVertex(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character"))
addEdge(timeStamp,srcID,tarID, Type("Character Co-occurence"))
```

Hopefully code updates should be extremely simple. 
